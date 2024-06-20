from account_service import create_account, list_accounts
from client_service import create_clients
from menu import menu
from transaction_service import deposit, show_extract, withdraw_money


def main():
  clients = []
  accounts = []
  while True:
    option = menu()
     
    if option == "d":
      deposit(clients)

    if option == "nu":
      create_clients(clients)

    if option == "nc":
      create_account(clients,accounts)
     
    elif option == "s":
      withdraw_money(clients)

    elif option == "lc":
      list_accounts(accounts)      
      
    elif option == "e":
      show_extract(clients)      
     
    elif option == "q":
      break

main()
