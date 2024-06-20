
from client_service import filter_client, get_client_account
from deposit import Deposit
from operation_failure import operation_failure
from utils import format_cpf, get_input, remove_non_numeric
from withdraw_money import WithdrawMoney


def deposit(clients):
  cpf = get_input("cpf")
  cpf = format_cpf(cpf)

  client = filter_client(cpf,clients)

  if not client:
    operation_failure("Cliente não Localizado!")
    return
  
  number_account = get_input("number_account")
  if not number_account.isdigit():
    return operation_failure("Digite somente números")
    
  account = get_client_account(client,number_account)
  if not account:
    return

  value = get_input("value")
  if not cpf.isdigit():
   return operation_failure("Digite somente números")
  value = int(value)

  transaction = Deposit(value)

  client.add_transaction(account,transaction)

def withdraw_money(clients):
  cpf = get_input("cpf")
  if not cpf.isdigit():
    return operation_failure("Digite somente números")
  
  client = filter_client(cpf,clients)

  if not client:
    operation_failure("Cliente não Localizado!")
    return

  number_account = get_input("number_account")
  if not number_account.isdigit():
    return operation_failure("Digite somente números")
  
  password = get_input("password")
  account = get_client_account(client,number_account)

  if not account or account.password != password:
    return operation_failure("Verifique sua Conta/Senha!")    

  value = get_input("value")
  if not value.isdigit():
   return operation_failure("Digite somente números")
  value = int(value)
  
  transaction = WithdrawMoney(value)

  
  client.add_transaction(account,transaction)
  
def show_extract(clients):
  cpf = get_input("cpf")
  cpf = format_cpf(cpf)
  
  client = filter_client(cpf,clients)

  if not client:
    operation_failure("Cliente não Localizado!")
    return
  
  number_account = get_input("number_account")
  if not number_account.isdigit():
    return operation_failure("Digite somente números")
  
  password = get_input("password")
  account = get_client_account(client,number_account)

  if not account or account.password != password:
    return operation_failure("Verifique sua Conta/Senha!")    
  
  print("\n============= EXTRATO =============")
  transactions = account.bank_account_statement.transactions

  extract = ""
  if not transactions:
    print("Não foi Realizada Movimentação.")
  else:
    for transaction in transactions:
      icon = "✅" if transaction['type'] == "Deposit" else "⛔"
      operation = "Depósito" if transaction['type'] == "Deposit" else "Saque"

      extract += f"\n{operation}:\n\t{icon} R$ {transaction['value']:.2f}\n\tData: {transaction['date']}"
      
  print(extract)
  print(f"\n✅ Saldo: R$ {account.balance:.2f}")
  print("===================================")
  