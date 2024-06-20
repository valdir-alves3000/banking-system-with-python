from account import Account
from withdraw_money import WithdrawMoney


class CurrentAccount(Account):
  def __init__(self, number_account,client,limit=500,withdrawal_limit=3):
    super().__init__(number_account,client)
    self.limit = limit
    self.withdrawal_limit = withdrawal_limit
    
  def withdraw_money(self,value):
    number_withdrawals = len([transaction for transaction in self.bank_account_statement.transactions if transaction["type"] == WithdrawMoney.__name__])

    exceed_limit = value > self.limit
    exceeded_withdrawal_limit = number_withdrawals >= self.withdrawal_limit

    if exceed_limit:
      print("O valor do saque excede o limite.")

    elif exceeded_withdrawal_limit:
      print("Número máximo de saques excedido.")

    else:
      return super().withdraw_money(value)
    
    return False
  
  def __str__(self):
    return f"""\
        Agência:\t{self.bank_agency}
        C/C:\t{self.number_account}
        Titular:\t{self.client.name}
    """
