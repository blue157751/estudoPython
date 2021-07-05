# Fazendo uma simples calculadora

# Essa função soma dois números
def soma(x, y):
    return x + y

# Essa função subtrai dois números
def subtrair(x, y):
    return x - y

# Essa função multiplica dois números
def multiplicar(x, y):
    return x * y

# Essa função divide dois números
def dividir(x, y):
    return x / y


print("Selecione a operação.")
print("1.Somar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # Pega o input do usuário
    choice = input("Digite a sua escolha(1/2/3/4): ")

    # Checa se a escolha está entre as 4 opções
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print(num1, "+", num2, "=", soma(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtrair(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))
        break
    else:
        print("Dado inválido")