import random
import textwrap

from operation_failure import operation_failure
from user import find_user_by_cpf


def generete_number_account():
  number_account = random.randint(100000, 999999)
  return number_account

def check_if_the_account_already_exists(bank_agency,number_account,accounts):
  account_exists = [account for account in accounts if account["number_account"] == number_account and account["bank_agency"] == bank_agency]
  return account_exists[0] if account_exists else None
   
  
def list_accounts(accounts):
    for account in accounts:
        linha = f"""\
            Agência:\t{account['agencia']}
            C/C:\t\t{account['numero_conta']}
            Titular:\t{account['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def check_user_has_account(user,accounts):
   user_has_account = [account for account in accounts if account["user"] == user]
   return user_has_account[0] if user_has_account else None

def create_account(*,users, bank_agency,accounts):
  cpf = input("Informe o CPF do usuário: ")
  user = find_user_by_cpf(cpf, users)
  password = input("Digite sua senha: ")

  user_has_account = check_user_has_account(user,accounts)

  if user_has_account :
     operation_failure("Usuário Já Possui um Conta.")
  else:
    number_account = generete_number_account()
    account_already_exists = check_if_the_account_already_exists(bank_agency,number_account,accounts)

    while account_already_exists:
      number_account = generete_number_account()
      account_already_exists = check_if_the_account_already_exists(bank_agency,number_account,accounts)
    
    if user:
        account = {
          "bank_agency": bank_agency, 
          "number_account": number_account, 
          "withdrawal_limit": 3,
          "limit": 500,
          "number_withdrawals": 0,
          "extract": "", 
          "balance": 0,          
          "user": user,
          "password": password, 
        }
        accounts.append(account)
        print("\n✅ Conta criada com sucesso!")
        print(account)
    else:
      operation_failure("Usuário não encontrado.")
