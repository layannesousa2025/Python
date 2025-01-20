def calculaIMC(peso, altura):
    return peso / (altura ** 2)

peso = eval(input('digite o peso em quilos'))
altura = eval(input('digite a altura em centimento'))
calculaIMC(peso,altura)
imc = calculaIMC(peso,altura)
print('imc=',imc)
