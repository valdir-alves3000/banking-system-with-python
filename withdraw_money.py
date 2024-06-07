from operation_failure import operation_failure

def withdraw_money(*,balance, value, extract, limit, number_withdrawals, withdrawal_limit):
  excedeu_saldo = value > balance
  excedeu_limite = value > limit
  excedeu_saques = number_withdrawals >= withdrawal_limit

  if excedeu_saldo:
    operation_failure("Você não tem saldo suficiente.")
  elif excedeu_limite:
    operation_failure("O valor do saque excede seu limite.")
  elif excedeu_saques:
    operation_failure("Número máximo de saques excedido.")

  elif value > 0:
    balance -= value
    extract += f"⛔ Saque: R$ {value:.2f}\n"
    number_withdrawals += 1
  else:
    operation_failure("O valor informado é inválido.")

  return balance, extract, number_withdrawals
