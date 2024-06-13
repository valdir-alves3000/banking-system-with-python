import textwrap


def menu():
  menu = """\n
  [d]\tDepositar
  [s]\tSacar
  [user]\tCriar Usuário
  [conta]\tAbrir Conta
  [e]\tExtrato
  [q]\tSair
  => """
  return input(textwrap.dedent(menu))