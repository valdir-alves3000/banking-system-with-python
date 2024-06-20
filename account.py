from bank_account_statement import BankAccountStatement
from operation_failure import operation_failure


class Account:
  def __init__(self, number_account,client):
    self._balance = 0
    self._number_account = number_account
    self._bank_agency = '0001'
    self._client = client
    self._bank_account_statement = BankAccountStatement()

  @classmethod
  def add_account(cls,client,number_account):
    return cls(number_account,client)
  
  @property
  def balance(self):
    return self._balance
  
  @property
  def number_account(self):
    return self._number_account
  
  @property
  def bank_agency(self):
    return self._bank_agency
  
  @property
  def client(self):
    return self._client
      
  @property
  def bank_account_statement(self):
    return self._bank_account_statement
    
  def withdraw_money(self,value):
    balance = self.balance
    exceeded_balance = value > balance

    if exceeded_balance:
      operation_failure("Você não tem saldo suficiente.")

    elif value > 0:
      self._balance -= value
      print("\n✅ Saque realizado com sucesso!")
      return True
    
    else:
      operation_failure("\n O valor informado é inválido.")

    return False
  
  def deposit(self,value):
    if value > 0:
      self._balance += value
      print("\n✅ Depósito realizado com sucesso!")
    else:
      operation_failure("O valor informado é inválido.")
      return False
    
    return True
