from accounts import (check_if_the_account_already_exists,
                      transaction_information)
from operation_failure import operation_failure


def deposit(bank_agency,accounts):
  if len(accounts) > 0:     
    try:
      value = float(input("Informe o valor do depósito: "))   
      number_account = float(input("Informe a conta de depósito: "))
    except ValueError:
      operation_failure("Digite apenas números.")               

    account = check_if_the_account_already_exists(bank_agency=bank_agency,number_account=number_account,accounts=accounts)
    
    if(value > 0):
      account["balance"] += value
      account["extract"] += f"✅ Depósito: R$ {value:.2f}\n"
     
      transaction_information(value,account,"depósito")
     
    else:
      operation_failure("O valor informado é inválido.")
  else:
    operation_failure("Não há conta no Sistema.") 

  return accounts