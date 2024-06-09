from accounts import check_if_the_account_already_exists
from operation_failure import operation_failure


def bank_account_statement(accounts):  
  try:
    number_account = float(input("Informe a conta para Extrato: "))        
    bank_agency = float(input("Informe a agêcia para Extrato: "))        
  except ValueError:
    operation_failure("Digite apenas números.")
  
  password = input("Digite sua senha: ")
  account = check_if_the_account_already_exists(bank_agency=bank_agency,number_account=number_account,accounts=accounts)
  
  if account and account["password"] == password:        
    print("\n============= EXTRATO =============")
    print("Não foi Realizada Movimentação.\n" if not account["extract"] else account["extract"])
    print(f"✅ Saldo: R$ {account.get('balance', 0):.2f}")
    print("===================================")
  
