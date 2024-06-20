import re

from operation_failure import operation_failure
from physical_person import PhysicalPerson
from utils import format_cpf, format_date, get_input, remove_non_numeric


def create_clients(clients):
  cpf = get_input("cpf") 
  cpf = format_cpf(cpf)
      
  client = filter_client(cpf,clients)
  if(client):
    return operation_failure("Usuário já cadastrato no sistema.")
      
  name = get_input("name") 
  date_birth = get_input("date_birth")
  date_birth = format_date(date_birth)
  
  address = get_input("address")

  client = PhysicalPerson(name=name,date_birth=date_birth,cpf=cpf,address=address)

  clients.append(client)

  print("✅ Usuário criado com sucesso!")

def filter_client(cpf,clients):
  for client in clients:
    if client.cpf == cpf:
      return client
  return None

def get_client_account(client, number_account=None):
  if not client.accounts:
    operation_failure("Cliente não possui conta!")
    return False
  
  if number_account:  
    for account in client.accounts:

      if account.number_account == number_account:
        return account
      
    operation_failure("Número da conta não encontrado!")
    return False

  return client.accounts[0]