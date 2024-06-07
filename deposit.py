from operation_failure import operation_failure

def deposit(saldo,valor,extrato):
  if(valor > 0):
    saldo += valor
    extrato += f"✅ Depósito: R$ {valor:.2f}\n"
  else:
    operation_failure("O valor informado é inválido.")

  return saldo, extrato