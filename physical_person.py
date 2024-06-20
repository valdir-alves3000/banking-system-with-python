from client import Client


class PhysicalPerson(Client):
  def __init__(self, name,date_birth, cpf,address):
    super().__init__(address)
    self.name = name
    self.date_birth = date_birth
    self.cpf = cpf

