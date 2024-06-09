from accounts import create_account
from bank_account_statement import bank_account_statement
from deposit import deposit
from menu import menu
from operation_failure import operation_failure
from user import create_user
from withdraw_money import withdraw_money


def main():
  BANK_AGENCY = '0001'
  users = []
  accounts = []

  while True:
    option = menu()

    if option == "user":
      users = create_user(users)   
    if option == "conta":
      create_account(bank_agency=BANK_AGENCY, users=users,accounts=accounts)

    if option == "d":
      try:
        value = float(input("Informe o valor do depósito: "))   
        number_account = float(input("Informe a conta de depósito: "))
      except ValueError:
        operation_failure("Digite apenas números.")
        
      if len(accounts) > 0:     
        accounts =  deposit(value,BANK_AGENCY,number_account,accounts)
      else:
        operation_failure("Não há conta no Sistema.")        
         
    elif option == "s":
      withdraw_money(accounts)
      
    elif option == "e":      
      bank_account_statement(accounts)     

    elif option == "q":
      break

main()