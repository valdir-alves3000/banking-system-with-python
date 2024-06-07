import textwrap

def menu():
  menu = """\n
  [d]\tDepositar
  [s]\tSacar
  [user]\tCriar Usuário
  [conta]\tAcessar a Conta
  [e]\tExtrato
  [q]\tSair
  => """
  return input(textwrap.dedent(menu))