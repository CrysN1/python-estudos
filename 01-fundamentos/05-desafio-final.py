name = input("Qual é o seu nome? ")
age = int(input("Qual é a sua idade? "))
if age <= 12:
    print("Você é criança.")
elif age <=17:
    print("Você é adolescente.")
else:
    print("Você é adulto.")
city = input("Qual é a sua cidade? ")
profission = input("Qual é a sua profissão? ")

print("=========================")
print("Cadastro do usuario")
print("=========================")

print(f"Nome: {name.title()}")
print(f"Idade: {age} Anos")
print(f"Cidade: {city.title()}")
print(f"Profissão: {profission.title()}")
print("\n")

print(name.upper())
print(f"Quantidade de caracteres do nome: {len(name)}")
print(f"\nDaqui a 12 anos você terá {age + 12}")

print("\n=========================")
print("\nObrigado por utilizar este programa")
print("\n=========================")
print("Criador: CrystaynDev")