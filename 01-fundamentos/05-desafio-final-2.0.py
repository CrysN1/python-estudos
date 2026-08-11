print("==============================")
print("       CADASTRO DE USUÁRIO")
print("==============================")

name = input("Qual é o seu nome? ").strip()
age = int(input("Qual é a sua idade? "))
city = input("Qual é a sua cidade? ").strip()
profession = input("Qual é a sua profissão? ").strip()
email = input("Qual é o seu email? ").strip()
while not "@" in email or not "." in email:
    email = input("Qual é o seu email? ").strip()
if "@" in email and "." in email:
    print("Email Valido.")
else:
    print("Email invalido")

# Classificação da idade
if age < 0:
    classification = "Idade inválida."
elif age <= 12:
    classification = "Criança."
elif age <= 17:
    classification = "Adolescente."
elif age <= 59:
    classification = "Adulto."
else:
    classification = "Idoso."

print("\n==============================")
print("       DADOS DO USUÁRIO")
print("==============================")

print(f"Nome: {name.title()}")
print(f"Idade: {age} anos")
print(f"Classificação: {classification}")
print(f"Cidade: {city.title()}")
print(f"Profissão: {profession.title()}")
print(f"Email: {email}")

print("\n==============================")
print("       INFORMAÇÕES EXTRAS")
print("==============================")

print(f"Nome em maiúsculas: {name.upper()}")
print(f"Quantidade de caracteres do nome: {len(name)}")
print(f"Daqui a 12 anos você terá {age + 12} anos.")

print("\n==============================")
print("Obrigado por utilizar este programa!")
print("==============================")

print("Criador: CrystyanDev")