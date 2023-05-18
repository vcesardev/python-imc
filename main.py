def calculate_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def imc_category(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc < 24.9:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = calculate_imc(peso, altura)
category = imc_category(imc)

print("Seu IMC é:", round(imc,2))
print("Categoria:", category)