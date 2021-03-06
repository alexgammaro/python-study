from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(type(data_atual))
    print(data_atual)
    data_atual_str = data_atual.strftime("%d/%m/%Y | %H:%M:%S")
    print(type(data_atual_str))
    print(data_atual_str)
    print(data_atual.strftime("%c"))
    print(data_atual.weekday())# Dia da semana em numeral
    tupla_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
    print(tupla_semana[data_atual.weekday()])
    print(data_atual.month)  # Mês em numeral
    tupla_mes = ("", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro"
                 "Outubro", "Novembro", "Dezembro")
    print(tupla_mes[data_atual.month])
    data_criada = datetime(2018, 5, 13, 18, 20, 00)
    print(data_criada)
    print(data_criada.strftime("%c"))
    data_string = "23/04/2021 15:22:00"
    data_convertida = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
    print(type(data_convertida))
    print(data_convertida)
    nova_data_atras = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data_atras)
    nova_data_frente = data_convertida + timedelta(days=365, hours=4, minutes=50, seconds=40)
    print(nova_data_frente)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime("%A %B %Y")
    print(type(data_atual))
    print(data_atual.strftime("%d/%m/%Y"))
    print(type(data_atual_str))
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(type(horario))
    print(horario)
    horario_str = horario.strftime("%H:%M:%S")
    print(type(horario_str))
    print(horario_str)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()