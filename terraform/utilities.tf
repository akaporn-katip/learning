resource "azurerm_network_security_group" "utilities" {
  name                = "rvp-utils-sec-g"
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name

  security_rule {
    name                       = "SSH"
    priority                   = 1000
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "JENKINS"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "8080"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "Gitea"
    priority                   = 1002
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "3000"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "Nexus-Repository"
    priority                   = 1003
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "9091"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# Create utils public ip
resource "azurerm_public_ip" "utilities" {
  name                = "rvp-utils-public-ip"
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name
  allocation_method   = "Dynamic"
}

# Create network interface
resource "azurerm_network_interface" "utilities" {
  name                = "rvp-net-utils-inc"
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name

  ip_configuration {
    name                          = "rvp-net-utils-inc-config"
    subnet_id                     = azurerm_subnet.rvp.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.utilities.id
  }
}

# Assign security group to network
resource "azurerm_network_interface_security_group_association" "utilities" {
  network_interface_id      = azurerm_network_interface.utilities.id
  network_security_group_id = azurerm_network_security_group.utilities.id
}

# Create storage account for boot diagnostics
resource "azurerm_storage_account" "utilities" {
  name                     = "util${random_id.random_id.hex}"
  location                 = azurerm_resource_group.rvp.location
  resource_group_name      = azurerm_resource_group.rvp.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
}


# Create virtual machine
resource "azurerm_linux_virtual_machine" "utilities" {
  name                  = "utilities-server-vm"
  location              = azurerm_resource_group.rvp.location
  resource_group_name   = azurerm_resource_group.rvp.name
  network_interface_ids = [azurerm_network_interface.utilities.id]
  size                  = "Standard_DS1_v2"

  os_disk {
    name                 = "utilities-disk"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts-gen2"
    version   = "latest"
  }

  computer_name  = "utilities-server"
  admin_username = var.username

  admin_ssh_key {
    username   = var.username
    public_key = file("~/.ssh/id_rsa.pub")
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.utilities.primary_blob_endpoint
  }
}
