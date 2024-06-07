import textwrap

def menu():
  menu = """\n
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [q]\tSair
  => """
  return input(textwrap.dedent(menu))

def operation_failure(message:str):
  return print(f"Operação falhou! {message.title()}")

def deposit(saldo,valor,extrato):
  if(valor > 0):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
  else:
    operation_failure("O valor informado é inválido.")

  return saldo, extrato

def withdraw_money(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    operation_failure("Você não tem saldo suficiente.")
  elif excedeu_limite:
    operation_failure("O valor do saque excede seu limite.")
  elif excedeu_saques:
    operation_failure("Número máximo de saques excedido.")

  elif valor > 0:
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
  else:
    operation_failure("O valor informado é inválido.")

  return saldo, extrato, numero_saques

def main():
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  LIMITE_SAQUES = 3

  while True:
    opcao = menu()

    if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))
      saldo, extrato =  deposit(saldo,valor,extrato)
         
    elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      saldo, extrato, numero_saques = withdraw_money(extrato=extrato,saldo=saldo,valor=valor,limite=
                    limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
      
    elif opcao == "e":
      print("\n============= EXTRATO =============")
      print("Não foi Realizada Movimentação." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("===================================")

    elif opcao == "q":
      break

main()