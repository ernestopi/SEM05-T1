def segundos_para_horas(quant_segundos):
    horas = quant_segundos//3600
    resto = quant_segundos%3600
    minutos = resto//60
    segundos = resto%60
    return f'{horas}:{minutos}:{segundos}'
segundos = int(input())
horas = segundos_para_horas(segundos)
print(f'{horas}')

