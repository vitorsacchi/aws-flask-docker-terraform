resource "aws_instance" "api_ec2" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"
  key_name      = "minha-chave"  # nome EXATO da key na AWS

  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  tags = {
    Name = "flask-api-ec2"
  }
}
