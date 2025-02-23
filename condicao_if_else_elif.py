salario = float(input("Informe o seu salário -> "))

if salario <= 3000:
    print("Programador junior")
elif salario > 3000 and salario <= 6000:
    print ("Programador Pleno")
else:
    print("Programador Senior")