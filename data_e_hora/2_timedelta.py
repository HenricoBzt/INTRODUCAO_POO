from datetime import timedelta,date,datetime

tipo_carro = ["P","M","G"]
tempo_pequeno = 30
tempo_medio = 40
tempo_grande = 60
data_atual = datetime.now()
def tempo_estimado(tipocarro):
    print("=======SELECIONE O TAMANHO DO CARRO=======")
    tipocarro = str(input(','.join(tipo_carro)))
    if tipocarro == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
        print(f"O Carro chegou:{data_atual} e ficará pronto no tempo previsto de:{data_estimada}")
    elif tipocarro == "M":
        data_estimada = data_atual + timedelta(minutes=tempo_medio)
        print(f"O Carro chegou:{data_atual} e ficará pronto no tempo previsto de:{data_estimada}")
    else:
        data_estimada = data_atual + timedelta(minutes=tempo_grande)
        print(f"O Carro chegou:{data_atual} e ficará pronto no tempo previsto de:{data_estimada}")
        
data = date(2024,8,19)

tempo_estimado(tipo_carro)




