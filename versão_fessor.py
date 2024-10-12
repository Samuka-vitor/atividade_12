def exibir_menu():
    print("0 - sair")
    print("1 - Quadrado")
    print("2 - Triângulo")
    print("3 - Círculo")
    print("4 - Trapézio")

# lambdas
circulo = lambda r: 3.14*(r**2)
quadrado = lambda l: l**2
triangulo = lambda b, h: (b*h)/2
trapezio = lambda B, b, a: ((B+b)*a)/2

# programa principal 

while True:
    exibir_menu()
    opcao = input("Escolha a opção desejada: ")

    match opcao:
        case "0":
            break
        case "1":
            r = float(input("Informe o raio do círculo: ").replace(",","."))
            print(f"Área do círculo: {circulo(r)}")
            continue

        case "3":
            b = float(input("Informe a base do triângulo: ").replace(",","."))
            h = float(input("Informe a altura do triângulo: ").replace(",","."))
            print(f"Área do triângulo: {triangulo(b,h)}.")
            continue

        case "4":
            B = float(input("Informe a base maoir do trapézio: ").replace(",",".")) 
            b = float(input("Informe a base menor do trapézio: ").replace(",",".")) 
            a = float(input("Informe a altura do trapézio: ").replace(",",".")) 
            print(f"Área do trapézio: {triangulo(B,b,a)}")
            continue

        case _:
            print("Opção Inválida")
            continue

        