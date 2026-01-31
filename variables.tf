variable "db_user" {
  description = "Usuario do banco de dados"
}

variable "db_password" {
  description = "Senha do banco de dados"
  sensitive   = true
}