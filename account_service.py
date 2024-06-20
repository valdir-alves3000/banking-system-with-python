
import random
import textwrap

from client_service import filter_client
from current_account import CurrentAccount
from operation_failure import operation_failure
from utils import format_cpf, get_input


def create_account(clients,accounts):
  cpf = get_input("cpf") 
  cpf = format_cpf(cpf)
    
  client = filter_client(cpf,clients)

  if not client:
    operation_failure("Cliente não Localizado no Sistema.")
    return
  
  number_account = str(generete_number_account())
  password = get_input("password")
  account = CurrentAccount.add_account(client,number_account,password)

  accounts.append(account)
  client.accounts.append(account)

  print("\n✅ Conta criada com sucesso!")
  print(account)
               
def generete_number_account():
  number_account = random.randint(100000, 999999)
  return number_account

def list_accounts(accounts):
  for account in accounts:
    print("*" * 100)
    print(textwrap.dedent(str(account)))