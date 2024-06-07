from menu import menu
from user import create_user
from deposit import deposit
from withdraw_money import withdraw_money

def main():
  WITHDRAWAL_LIMIT = 3
  BANK_AGENCY = '0001'

  balance = 0
  limit = 500
  extract = ""
  number_withdrawals = 0
  users = []
  accounts = []

  while True:
    option = menu()

    if option == "user":
      create_user(users)      

    if option == "d":
      value = float(input("Informe o valor do depósito: "))
      balance, extract =  deposit(balance,value,extract)
         
    elif option == "s":
      value = float(input("Informe o valor do saque: "))
      balance, extract, number_withdrawals = withdraw_money(extract=extract,balance=balance,value=value,limit=
                    limit,number_withdrawals=number_withdrawals,withdrawal_limit=WITHDRAWAL_LIMIT)
      
    elif option == "e":
      print("\n============= EXTRATO =============")
      print("Não foi Realizada Movimentação.\n" if not extract else extract)
      print(f"✅ Saldo: R$ {balance:.2f}")
      print("===================================")

    elif option == "q":
      break

main()