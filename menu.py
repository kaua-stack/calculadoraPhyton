from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao  = -1
        self.opera  = Operacao()
        self.num1   = 0
        self.num2   = 0
    def mostraMenu(self):
        print("\n--- MENU ---\n\n"
              "Escolha uma das opções abaixo: "
              "\n0. sair"          +
              "\n1. Somar"         +
              "\n2. Subtrair"      +
              "\n3. Dividir"       +
              "\n4. Multiplicar"   +
              "\n5. Potência"      +
              "\n6. Raiz"          +
              "\n7. Tabuada"       +
              "\n8. exercicio1"    +
              "\n9. exercicio2"    +
              "\n10. exercicio3"   +
              "\n11. exercicio4"   +
              "\n12. exercicio5"   +
              "\n13. exercicio6"   +
              "\n14. exercicio7"   +
              "\n15. exercicio8"   +
              "\n16. exercicio9"   +
              "\n17. exercicio10"  +
              "\n18. exercicio11"  +
              "\n19. exercicio12"  +
              "\n20. exercicio13"  +
              "\n21. exercicio14"  +
              "\n22. exercicio15"  +
              "\n23. exercicio16"  +
              "\n24. exercicio17"  +
              "\n25. exercicio18"  +
              "\n26. exercicio19"  +
              "\n27. exercicio20"  +
              "\n\n--- SEGUNDA LISTA ---\n\n"
              "\n28. exercicio21"  +
              "\n29. exercicio22"  +
              "\n30. exercicio23"  +
              "\n31. exercicio24"  +
              "\n32. exercicio25"  +
              "\n33. exercicio26"  )

    def coletar(self):
        self.num1 = int(input("Informe o primeiro numero: "))
        self.num2 = int(input("Informe o segundo numero: "))

    def execucao(self):
        while self.opcao != 0:
            self.mostraMenu()   # chamando as opçoes
            self.opcao = int(input("Escolha uma das opções acima: "))
            if self.opcao == 0:
                print("obrigado!!")
            if self.opcao == 1:
                self.coletar() # chamando o input
                print(f'a Soma dos números digitados é: {self.opera.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A Subtrair dos números digitados é: {self.opera.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A Divisão dos números digitados é: {self.opera.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A Multiplicação dos números digitados é: {self.opera.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A Potencia dos números digitados é: {self.opera.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'A Raiz de {self.num1} digitado é: {self.opera.raiz(self.num1)}')
                print(f'A Raiz de {self.num2} digitado é: {self.opera.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada do {self.num1} digitado é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada do {self.num2} digitado é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:
                print( f'numero de 1 ao 10 é : {self.opera.exercicio1()}')

            elif self.opcao == 9:
                print(f'Numero pares do 1 ao 20 é :  {self.opera.exercicio2()}')

            elif self.opcao == 10:
                print(f'calculo da soma dos numeros de 1 ao 100 é :{self.opera.exercicio3()}')

            elif self.opcao == 11:
                print(f'multiplos de 5 do 1 ao 50 é: {self.opera.exercicio4()}')

            elif self.opcao == 12:
                num = int(input('informe um numero: '))
                print(f'se o numero e impar ou par : {self.opera.exercicio5(num)}')

            elif self.opcao == 13:
                num = int(input('informe um numero: '))
                print(f'positivo, negativo ou zero :  {self.opera.exercicio6(num)}')

            elif self.opcao == 14:
                num = int(input('informe um numero: '))
                print(f'A tabuada do {num} é : {self.opera.exercicio7(num)}')

            elif self.opcao == 15:
                num = int(input('informe um numero: '))
                print(f'do 0 ate {num} é : {self.opera.exercicio8(num)}')

            elif self.opcao == 16:
                num = int(input('informe um numero: '))
                print(f'A soma do 0 ate  {num} é : {self.opera.exercicio9(num)}')

            elif self.opcao == 17:
                print(f'Numeros primos do 1 ao 20 :  {self.opera.exercicio10()}')

            elif self.opcao == 18:
                num = int(input('informe um numero: '))
                print(f'verificando se o  {num} é primo :  {self.opera.exercicio11(num)}')

            elif self.opcao == 19:
                num = int(input('informe um numero: '))
                print(f'calculando o fatorial do {num} é : {self.opera.exercicio12(num)}')

            elif self.opcao == 20:
                print(f'calcular o fibinocci ate o decimo termo:  {self.opera.exercicio13()}')

            elif self.opcao == 21:
                num = int(input('informe um numero: '))
                print(f'verificando se o numero faz parte do fibinocci {self.opera.exercicio14(num)}')

            elif self.opcao == 22:
                num = int(input('informe um numero: '))
                print(f'Calcular a soma dos digitos do numero{self.opera.exercicio15(num)}')

            elif self.opcao == 23:
                num = int(input('informe um numero: '))
                print(f'numero impar e par : {self.opera.exercicio16(num)}')

            elif self.opcao == 24:
                num = int(input('informe um numero: '))
                print(f'numeros primos {self.opera.exercicio17(num)}')

            elif self.opcao == 25:
                num = int(input('informe um numero: '))
                print(f'sequencia collatz {self.opera.exercicio18(num)}')

            elif self.opcao == 26:
                num = int(input('informe um numero: '))
                print(f' {self.opera.exercicio19(num)}')

            elif self.opcao == 27:
                num = int(input('informe um numero: '))
                print(f'numero perfeito {self.opera.exercicio20(num)}')

            elif self.opcao == 28:
                print(f'armazenada {self.opera.exercicio21(num)}')

            elif self.opcao == 29:
                num = int(input('informe um numero: '))
                print(f'anterior é : {self.opera.exercicio22(num)}')

            elif self.opcao == 30:
                num = int(input('informe a base: '))
                num = int(input('informe a altura: '))
                print(f'Resultado {self.opera.exercicio23()}')

            elif self.opcao == 31:
                num = int(input('informe sua idade: '))
                print(f'{self.opera.exercicio24()}')

            elif self.opcao == 32:
                num = int(input('informe o total de votos : '))
                num = int(input('informe o total de votos brancos: '))
                num = int(input('informe o total de votos nulos: '))
                num = int(input('informe o total de votos validos '))
                print(f' {self.opera.exercicio25()}')

            elif self.opcao == 33:
                num = int(input('qual o salario atual: '))
                num = int(input('qual o valor de reajuste: '))
                print(f'{self.opera.exercicio26()}')














