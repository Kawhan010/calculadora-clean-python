def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def exibir_menu():
    print("\n" + "="*30)
    print("       CALCULADORA CLEAN")
    print("="*30)
    print("1️⃣  Somar")
    print("2️⃣  Subtrair")
    print("3️⃣  Multiplicar")
    print("4️⃣  Dividir")
    print("5️⃣  Sair")
    print("="*30)

def solicitar_numeros():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        return a, b
    except ValueError:
        print("⚠️  Entrada inválida. Digite apenas números.")
        return None, None

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "5":
            print("\n👋 Encerrando... Até a próxima!")
            break

        if opcao in ["1", "2", "3", "4"]:
            a, b = solicitar_numeros()
            if a is None or b is None:
                continue

            if opcao == "1":
                resultado = somar(a, b)
                operacao = "Soma"
            elif opcao == "2":
                resultado = subtrair(a, b)
                operacao = "Subtração"
            elif opcao == "3":
                resultado = multiplicar(a, b)
                operacao = "Multiplicação"
            elif opcao == "4":
                resultado = dividir(a, b)
                operacao = "Divisão"

            print(f"\n✅ Resultado da {operacao}: {resultado}")
        else:
            print("⚠️  Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
