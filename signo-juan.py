def obtener_signo_zodiacal(dia, mes):
    if (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 19):
        return "Aries"
    if (mes == 4 and 20 <= dia <= 30) or (mes == 5 and 1 <= dia <= 20):
        return "Tauro"
    if (mes == 5 and 21 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
        return "Géminis"
    if (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 1 <= dia <= 22):
        return "Cáncer"
    if (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1 <= dia <= 22):
        return "Leo"
    if (mes == 8 and 23 <= dia <= 31) or (mes == 9 and 1 <= dia <= 22):
        return "Virgo"
    if (mes == 9 and 23 <= dia <= 30) or (mes == 10 and 1 <= dia <= 22):
        return "Libra"
    if (mes == 10 and 23 <= dia <= 31) or (mes == 11 and 1 <= dia <= 21):
        return "Escorpio"
    if (mes == 11 and 22 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
        return "Sagitario"
    if (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 19):
        return "Capricornio"
    if (mes == 1 and 20 <= dia <= 31) or (mes == 2 and 1 <= dia <= 18):
        return "Acuario"
    if (mes == 2 and 19 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
        return "Piscis"
    else:
        return "Fecha no válida"

# Solicitar fecha de nacimiento al usuario
dia = int(input("Ingresa el día de nacimiento: "))
mes = int(input("Ingresa el mes de nacimiento: "))

# Determinar y mostrar el signo zodiacal
signo = obtener_signo_zodiacal(dia, mes)
print(f"Tu signo zodiacal es: {signo}")
