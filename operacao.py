import math

class Operacao:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def somar(self, num1, num2):
        self.coletar(num1, num2)       # ultilizando o método
        return self.num1 + self.num2


    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2


    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2


    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível dividir!"
        else:
            return self.num1 / self.num2


    def tabuada(self, num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i} '
        return resultado


    def potencia(self, base, expoente):
        return pow(base, expoente)


    def raiz(self, num):
        return math.sqrt(num)


    def exercicio1(self):
        res = ""
        for i in range(1,11,1):
            res += f'\n{i}'
        return res


    def exercicio2(self):
        res = ""
        for i in range(0, 21, 2):
            res += f'\n{i}'
        return res


    def exercicio3(self):
        soma = 0
        for i in range(0,101):
            soma += i
        return soma


    def exercicio4(self):
        res = ""
        for i in range(1, 51, 1):
            if i % 5 == 0:
             res += f'\n{i}'
        return res


    def exercicio5(self,num):
        if num % 2 == 0:
            return 'Número par!'
        else:
            return "Número ímpar"


    def exercicio6(self,num):
        if num < 0:
            return "Número negativo!"
        if num == 0:
            return "Número zero!"
        else:
            return "Número positivo!"


    def exercicio7(self,num):
        tab = ""
        for i in range(0, 11, 1):
            tab += f'\n{num} * {i} = {num * i}'
        return tab


    def exercicio8(self,num):
        res = ""
        for i in range(0,num):
            res += f'\n{i}'
        return res


    def exercicio9(self,num):
        soma = ""
        for i in range(1, num, 1):
            soma += f'\n{num} + {i} = {num + i}'
        return soma


    def exercicio10(self):
        primo = '1\n\n2\n3\n5'
        for i in range(5,21,1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo


    def exercicio11(self,num):
        if num == 2 or num == 3 or num == 5:
            return f'0 {num} e primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'o {num}  e primo!'
        return f'o {num}nao e primo'


    def exercicio12(self,num):
        soma = 1
        for i in range(1, num, 1):
            soma += soma * i
        return soma


    def exercicio13(self,num):
        ter = ""
        ultimo = 1
        penultimo = 1

        if (num == 1) or (num == 2):
            print("1")
        else:
            for cont in range(1, 11):
                ter = ultimo + penultimo
                penultimo = ultimo
                ultimo = ter
                cont += 1
            return ter

    def exercicio14(self):
        n = int(input(" Digite Quantos termos você deseja :"))
        num1 = 0
        num2 = 1
        num3 = 0

        while num3 <= n:
            print("{}.".format(num3), end="")
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return print

    def exercicio15(self, num):
        soma = 0
        a = num
        b = str(a)
        for i in range(len(b)):
            soma += int(b[i])
        return soma


    def exercicio16(self,num):
        resultado = ""
        for i in range(1, num):
            if i % 2 == 0:
                resultado += f'\n{i} Par'
            else:
                resultado += f'\n{i} Impar'
        return resultado

    def exercicio17(self,num):
         primo = ""
         for i in range(1, num, 1):
             if i == 2 or i == 3 or i == 5:
                 primo += f'\n{i}'
             elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                 primo += f'\n{i}'
         return primo

    def exercicio18(self, num1):
        resultado = ""
        for i in range(1, num1):
            if i % 2 == 0:
                resultado += f'\n{i / 2}'
            else:
                resultado += f'\n{i * 3 + 1}'
        return resultado

    def exercicio19(self, num1):
        par = 0
        impar = 0
        for i in range(1, num1 + 1):
            if i % 2 == 0:
                par += i
            else:
                impar += i
        return f'A soma dos pares é de:{par}, e dos ímpares é:{impar}'


    def exercicio20(self,num):
        soma = 0
        for i in range(0,num):
            if num % i == 0:
                soma += i
            if soma == num:
                return "e numero perfeito"
            else :
                return "nao e numero perfeito"

    #Exercicio da segunda lista

    def exercicio21(self):
        num1 = 10
        num2 = 20
        return {num1 + 10}, {num2 - 10}

    def exercicio22(self, num):
        return num - 1

    def exercicio23(self,base,altura):
        return base * altura

    def exercicio24(self, ano, meses, dias):
        idadeAtual = ano * 365 + meses * 30 + dias
        return f'{idadeAtual}'

    def exercicio25(self,valototal, votosbranco, votosnulos, votosvalidos):
        return f'votos total é {valototal}\n votos brancos :{ votosbranco / 100}% \n votos nulos :{votosnulos / 100}% \n  votos validos de : {votosvalidos / 100}%'

    def exercicio26(self):
        salarioantigo = 0
        reajuste = 0
        salarioAtual = salarioantigo + reajuste
        return f'{salarioAtual}'



































