texto = "programação"
letra_para_contar = "a"
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador +=1

print(f"a letra '{letra_para_contar}'aparece {contador} vezes na palavra '{texto}'.")