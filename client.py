class Client:
  def __init__(self, address):
    self.address = address
    self.accounts = []
  
  def add_transaction(self,account,transaction):
    transaction.register(account)

  def add_account(self,account):
    self.accounts.append(account)
    
  def __repr__(self):
    return f"Client(address={self.address}, accounts={self.accounts})"

