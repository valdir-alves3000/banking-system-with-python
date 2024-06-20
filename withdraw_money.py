from transaction import Transaction


class WithdrawMoney(Transaction):
  def __init__(self,value):
    self._value = value

  @property
  def value(self):
    return self._value
  
  def register(self,account):
    success_transaction = account.withdraw_money(self.value)

    if success_transaction:
      account.bank_account_statement.add_transaction(self)

        