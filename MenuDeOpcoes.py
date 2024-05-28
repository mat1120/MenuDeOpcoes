n1 = int(input("Digite um valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))
n5 = int(input("Digite o quinto valor: "))
numeros = [n1, n2, n3, n4, n5]
opcao = 0
soma = 0
menos = 0
multiplcar = 0
dividir = 0
while opcao != 7:
    opcao = int(input("""Escolha uma das opções:
[ 1 ] somar
[ 2 ] subtrair
[ 3 ] multiplcar
[ 4 ] dividir
[ 5 ] maior e menor
[ 6 ] Novos numeros 
[ 7 ] Encerrar programa: """))
    if opcao not in (1, 2, 3, 4, 5,6,7):
        print("OPÇAO INVALIDA,TENTE NOVAMENTE")
    else:
        if opcao == 1:
            soma = sum(numeros)
            print("a soma dos numeros equivale á {}".format(soma))
        elif opcao == 2:
            menos = numeros[0]
            for num in numeros[1:]:
                menos -= num
            print("a subtração dos numeros inseridos euquivale á {}".format(menos))
        elif opcao == 3:
            multiplcar = numeros[0]
            for num in numeros[1:]:
                multiplcar *= num
            print("a multiplicação dos numeros inseridos equivale á {}".format(multiplcar))
        elif opcao == 4:
            dividir = numeros[0]
            for num in numeros[1:]:
                dividir /= num
            print("a divisão dos numeros inseridos equivale á {}".format(dividir))
        elif opcao == 5:
            maior = max(n1, n2, n3, n4, n5)
            menor = min(n1, n2, n3, n4, n5)
            print("O maior numero é {} e o menor numero {}".format(maior, menor))
        elif opcao == 6:
            opcao = int(input("Quais valores? "))
        elif opcao == 7:
            print("Encerrando programa,obrigado e volte sempre")

