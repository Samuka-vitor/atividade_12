
def exibir_menu():
    print("Escolha uma opção.\n")
    print("1 - Quadrado")
    print("2 - Triângulo")
    print("3 - Círculo")
    print("4 - Trapézio")

# Apresentação do menu
    #print("Escolha uma opção.\n")
    #print("1 - Quadrado")
    #print("2 - Triângulo")
    #print("3 - Círculo")
    #print("4 - Trapézio")

try:
    opcao = int(input("Insira o número da opção desejada: "))

    if opcao == 1:
        lado = float(input("Qual o comprimento dos lado, meu nobre?").replace(",","."))
        area_quadrado = lambda l: l**2 # essa lambda deveria está fora do 'if'
        area = area_quadrado(lado)
        print(f"A área do quadrado é a seguinte: {area}")
    
    elif opcao == 2:
        base = float(input("Qual é o tamanho da base, meu nobre? ").replace(",","."))
        altura = float(input("Qual é o tamanho da altura, meu nobre? ").replace(",","."))
        area_triangulo = lambda b,a: (b*a/2) # essa lambda deveria está fora do 'if'
        triangulo = area_triangulo(base, 
        altura)
        print(f"A área do triângulo é {triangulo}")
    
    elif opcao == 3:
        raio = float(input("Qual o valor do raio, meu nobre? ").replace(",","."))
        area_circulo = lambda r: 3.14 * (r ** 2) # essa lambda deveria está fora do 'if'
        area = area_circulo(raio)
        print(f"A área do seu circulo é: {area}")

    elif opcao == 4:
        b_maior = float(input("Qual o tamanho da sua base maior, meu nobre? ").replace(",","."))
        b_menor = float(input("Qual o tamanho da sua base menor, meu nobre? ").replace(",","."))
        altura = float(input("Qual o valor da altura, meu nobre? ").replace(",","."))
        area_trapezio = lambda B,b,a: ((B + b)*a)/2 # essa lambda deveria está fora do 'if'
        area = area_trapezio(b_maior, b_menor, altura)
        print(f"A área do trápezio é: {area}")

except ValueError:
    print("Entrada não é válida. Tente novamente com outro valor, obrigado.")    

except Exception as e:
    print(f"Ocorreu o seguinte erro: {e}")

    