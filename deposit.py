import textwrap

from accounts import check_if_the_account_already_exists
from operation_failure import operation_failure


def deposit(valor,bank_agency,number_account,accounts):
  account = check_if_the_account_already_exists(bank_agency=bank_agency,number_account=number_account,accounts=accounts)
  
  if(valor > 0):
    account["balance"] += valor
    account["extract"] += f"✅ Depósito: R$ {valor:.2f}\n"
    print(f"✅ Depósito realizado com sucesso\n")
    linha = f"""\
        Agência:\t{account['bank_agency']}
        C/C:\t\t{account['number_account']}
        Titular:\t{account['user']['name']}
        Valor:\t{f"R$ {valor}"}
    """
    print(textwrap.dedent(linha))
  else:
    operation_failure("O valor informado é inválido.")

  return accounts