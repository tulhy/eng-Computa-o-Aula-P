# media_final = float(input("Média final: "))
#
# if media_final >= 6:
#     print ("Aprovado!")
# else:
#     print ("Reprovado!")




# velocidade = float(input("Qual foi sua velocidade? "))
#
# if velocidade > 80:
#     multa = (velocidade - 80) * 5
#     print (f"Multa no valor de R$ {multa:.2f}.")
# else:
#     print ("sua velocidade era permitida")



num1 = float(input("digite o valor um "))
num2 = float(input("digite o valor dois "))
num3 = float(input("digite o valor tres "))

if num1 >= num2 and num1 >= num3:
    print(f"o numero maior é {num1}")
elif num1 >= num2 and num1 >= num3:
    print(f"o numero maior é {num2}")
elif num1 >= num2 and num1 >= num3:
    print(f"o numero maior é {num3}")


if num1 <= num2 and num1 <= num3:
        print(f"o numero menor é {num1}")
elif num1 <= num2 and num1 <= num3:
        print(f"o numero menor é {num2}")
elif num1 <= num2 and num1 <= num3:
        print(f"o numero menor é {num3}")

# maior = max(num1, num2, num3)
# menor = min(num1, num2, num3)
#
# print(f"o maior numero é {maior}")
# print(f"o menor numero é {menor}")




salario = float(input("digite o seu salario: "))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print(f"o aumento será de R${aumento:.2f} seu novo salario será de R${novo_salario:.2f}")