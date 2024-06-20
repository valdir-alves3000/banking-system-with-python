import textwrap


def menu():
  menu = """\n
  ============= MENU =============
  [d]\tDepositar
  [s]\tSacar
  [nu]\tNovo Usuário
  [nc]\tAbrir Conta
  [lc]\tListar Contas
  [e]\tExtrato
  [q]\tSair
  => """
  return input(textwrap.dedent(menu))