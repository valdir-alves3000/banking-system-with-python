import re


def format_date(date):
  date = remove_non_numeric(date)
  return re.sub(r"(\d{2})(\d{2})(\d{4})", r"\1/\2/\3", date)

def format_cpf(cpf):
  cpf = remove_non_numeric(cpf)  
  return re.sub(r"(\d{3})(\d{3})(\d{3})(\d{2})", r"\1.\2.\3-\4", cpf)

def remove_non_numeric(value):
  return re.sub(r"\D", "", value)

def get_input(data):
    message =""
    if data == "cpf":
      message = "Informe o CPF (somente número): "

    if data == "name":
      message = "Informe seu Nome: "

    if data == "date_birth":
      message = "Informe a data de nascimento (somente números): "

    if data == "address":
      message = "Informe o endereço: "

    if data == "number_account":
      message = "Informe o numero da conta: "

    if data == "value":
      message = "Informe o Valor: "   

    if data == "password":
      message = "Digite sua Senha: "   
    
    return input(message)
  
 