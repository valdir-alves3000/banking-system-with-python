from operation_failure import operation_failure


def create_user(users):
  try:
    cpf = int(input("Informe o CPF (somente número): "))
  
    name = input("Informe seu Nome: ")
    user = find_user_by_cpf(cpf,users)
    if(user):
      operation_failure("Usuário já cadastrato no sistema.")
    else:
      users.append({"cpf": cpf,"name": name})
      print("✅ Usuário criado com sucesso!")
  except ValueError:
    operation_failure("Digite somente números")  
  return users

def find_user_by_cpf(cpf,users):
  user_exists = [user for user in users if user["cpf"] == cpf]    
  return user_exists[0] if user_exists else None