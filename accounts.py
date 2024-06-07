import textwrap
from user import find_user_by_cpf
from operation_failure import operation_failure

def list_accounts(accounts):
    for account in accounts:
        linha = f"""\
            Agência:\t{account['agencia']}
            C/C:\t\t{account['numero_conta']}
            Titular:\t{account['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def create_account(*,users, number_account, bank_agency):
  cpf = input("Informe o CPF do usuário: ")
  user = find_user_by_cpf(cpf, users)

  if user:
      print("\n✅ Conta criada com sucesso!")
      return {"agencia": bank_agency, "numero_conta": number_account, "usuario": user}

  operation_failure("Usuário não encontrado.")
