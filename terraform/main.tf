terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.0"
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

resource "random_password" "password" {
  length      = 16
  min_lower   = 1
  min_upper   = 1
  min_numeric = 1
  min_special = 1
  special     = true
}

resource "random_id" "random_id" {
  keepers = {
    # Generate a new ID only when a new resource group is defined
    resource_group = azurerm_resource_group.rvp.name
  }

  byte_length = 8
}

resource "azurerm_resource_group" "rvp" {
  name     = "rvp-demo-rg"
  location = "southeastasia"
}

# Create virtual network
resource "azurerm_virtual_network" "rvp" {
  name                = "rvp-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name
}

# Create subnet
resource "azurerm_subnet" "rvp" {
  name                 = "internal"
  resource_group_name  = azurerm_resource_group.rvp.name
  virtual_network_name = azurerm_virtual_network.rvp.name
  address_prefixes     = ["10.0.2.0/24"]
}

# Create public IPs
resource "azurerm_public_ip" "rvp" {
  name                = "rvp-public-ip"
  location            = azurerm_resource_group.rvp.location
  resource_group_name = azurerm_resource_group.rvp.name
  allocation_method   = "Dynamic"
}
