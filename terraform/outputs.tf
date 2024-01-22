output "public_ip_address" {
  value = azurerm_windows_virtual_machine.devapp.public_ip_address
}

output "admin_password" {
  sensitive = true
  value     = azurerm_windows_virtual_machine.devapp.admin_password
}


output "utilities_public_ip_address" {
    value = azurerm_linux_virtual_machine.utilities.public_ip_address
}

output "utilities_admin_username" {
  value = azurerm_linux_virtual_machine.utilities.admin_username
}