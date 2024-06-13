from accounts import (check_if_the_account_already_exists,
                      transaction_information)
from operation_failure import operation_failure


def withdraw_money(accounts): 
  value = 0 
  account = {}
  try:
    number_account = int(input("Informe a conta para Saque: "))
    bank_agency = input("Informe a agêcia para Saque: ")
    password = input("Digite sua senha: ")

    account = check_if_the_account_already_exists(bank_agency=bank_agency,number_account=number_account,accounts=accounts)
    
    if account and account.get("password") == password:
      value = float(input("Informe o valor do saque: "))
                
      excedeu_saldo = value > account.get("balance", 0)
      excedeu_limite = value > account.get("limit", 999)
      excedeu_saques = account.get("number_withdrawals", 0) >= account.get("withdrawal_limit", 0)

      if excedeu_saldo:
        operation_failure("Você não tem saldo suficiente.")
      elif excedeu_limite:
        operation_failure("O valor do saque excede seu limite.")
      elif excedeu_saques:
        operation_failure("Número máximo de saques excedido.")

      elif value > 0:
        account["balance"] -= value
        account["extract"] += f"⛔ Saque: R$ {value:.2f}\n"
        account["number_withdrawals"] += 1
        transaction_information(value,account,"saque")
      else:
        operation_failure("O valor informado é inválido.")        
    else:
      operation_failure("Verifique o numero da conta/password e Tente Novamente!")
  except ValueError:
    operation_failure("Digite apenas números.")
        
  return account
