tens = [ 1, 10, 100, 1000 ]
nombres = [
    ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"],
    [False, "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"],
    [False, "ciento", "doscientos", "trecientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    ]
elevaciones = [False, False, False, "mil"]

def numberName(n):
    nameString = ""
    i = 0
    y = 0
    lastDigit = False
    numberString = str(n[::-1]) #Reverse String
    for digit in numberString:
        if i == 3:
            y += i
            i = 0
            nameString = elevaciones[y]+" "+nameString
        digitInt = int(digit)
        if nombres[i][digitInt]:
            if i == 1:
                if nombres[i][digitInt] + " y " + nombres[i][lastDigit] == "diez y uno": nameString == "once "+ nameString
                elif nombres[i][digitInt] + " y " + nombres[i][lastDigit] == "diez y dos": nameString == "doce "+ nameString
                elif nombres[i][digitInt] + " y " + nombres[i][lastDigit] == "diez y tres": nameString == "trece "+ nameString
                elif nombres[i][digitInt] + " y " + nombres[i][lastDigit] == "diez y cuatro": nameString == "catorce "+ nameString
                elif nombres[i][digitInt] + " y " + nombres[i][lastDigit] == "diez y cinco": nameString == "quince "+ nameString
                else: nameString = nombres[i][digitInt] + " y " + nameString
            else:
                nameString = nombres[i][digitInt] + nameString
        i += 1
        lastDigit = digitInt
    return nameString
            