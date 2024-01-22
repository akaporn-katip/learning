resource "azurerm_network_security_group" "devapp" {
  name                = "rvp-sec-g"
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name

  security_rule {
    name                       = "RDP"
    priority                   = 1000
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "3389"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "application"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "WinRM"
    priority                   = 1002
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "5985"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# Create network interface
resource "azurerm_network_interface" "devapp" {
  name                = "rvp-net-inc"
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name

  ip_configuration {
    name                          = "rvp-net-inc-config"
    subnet_id                     = azurerm_subnet.rvp.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.rvp.id
  }
}

# Assign security group to network
resource "azurerm_network_interface_security_group_association" "devapp" {
  network_interface_id      = azurerm_network_interface.devapp.id
  network_security_group_id = azurerm_network_security_group.devapp.id
}

# Create storage account for boot diagnostics
resource "azurerm_storage_account" "devapp" {
  name                     = "diag${random_id.random_id.hex}"
  location                 = azurerm_resource_group.rvp.location
  resource_group_name      = azurerm_resource_group.rvp.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Create virtual machine
resource "azurerm_windows_virtual_machine" "devapp" {
  name                  = "dev-server-vm"
  admin_username        = "rvpadmin"
  admin_password        = random_password.password.result
  location              = azurerm_resource_group.rvp.location
  resource_group_name   = azurerm_resource_group.rvp.name
  network_interface_ids = [azurerm_network_interface.devapp.id]
  size                  = "Standard_B2ms"

  os_disk {
    name                 = "dev-server-disk"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2019-datacenter-gensecond"
    version   = "latest"
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.devapp.primary_blob_endpoint
  }
}
