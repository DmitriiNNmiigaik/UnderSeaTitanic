import streamlit as st
import matplotlib.pyplot as plt
def  get_bilet(lines):
    S_bilet=0
    S_passajir=0
    S_min = -1
    S_max = 0

    C_bilet = 0
    C_passajir = 0
    C_min = -1
    C_max = 0

    Q_bilet = 0
    Q_passajir = 0
    Q_min = -1
    Q_max = 0

    for line in lines:
        data = line.split(',')

        if data[0] == 'PassengerId':
            continue    #переход на следую строку
        if data[10] == '' or data[10] == ' ':
            continue  # Пропускаем пассажира без стоимости билета

        if data[12].strip() == 'S':     #strip убирает переход - enter
            S_passajir = S_passajir + 1
            S_bilet = S_bilet + float(data[10])

            if (S_min > float(data[10]) or S_min == -1) and float(data[10]) != 0:
                S_min = float(data[10])
            if S_max < float(data[10]):
                S_max = float(data[10])

        if data[12].strip() == 'C':     #strip убирает переход - enter
            C_passajir = C_passajir + 1
            C_bilet = C_bilet + float(data[10])

            if (C_min > float(data[10]) or C_min == -1) and float(data[10]) != 0:
                C_min = float(data[10])
            if C_max < float(data[10]):
                C_max = float(data[10])

        if data[12].strip() == 'Q':     #strip убирает переход - enter
            Q_passajir = Q_passajir + 1
            Q_bilet = Q_bilet + float(data[10])

            if (Q_min > float(data[10]) or Q_min == -1) and float(data[10]) != 0:
                Q_min = float(data[10])
            if Q_max < float(data[10]):
                Q_max = float(data[10])


    return round(S_bilet / S_passajir,2), S_min, S_max, round(C_bilet / C_passajir,2), C_min, C_max, round(Q_bilet / Q_passajir,2), Q_min, Q_max


with open("data.csv") as file:
   lines = file.readlines()
   S_srednee, S_min, S_max, C_srednee, C_min, C_max, Q_srednee, Q_min, Q_max = get_bilet(lines)


#print("Средняя стоимость билета в порту посадки S:",  S_srednee)
#print("Минимальная стоимость билета в порту посадки S:",  round(S_min,2))
#print("Максимальная стоимость билета в порту посадки S:",  round(S_max,2))

#print()

#print("Средняя стоимость билета в порту посадки C:",  C_srednee)
#print("Минимальная стоимость билета в порту посадки C:",  round(C_min,2))
#print("Максимальная стоимость билета в порту посадки C:",  round(C_max,2))

#print()

#print("Средняя стоимость билета в порту посадки Q:",  Q_srednee)
#print("Минимальная стоимость билета в порту посадки Q:",  round(Q_min,2))
#print("Максимальная стоимость билета в порту посадки Q:",  round(Q_max,2))



def do_var17():
    st.title ('Вычисление стоимости билета у пассажиров по каждому пункту посадки.')
    option = st.selectbox('Выбирите категорию стоимости билета', ['Средняя', 'Минимальная', 'Максимальная'])
    pport = ['Порт S', 'Порт C', 'Порт Q']

    #если выбрана категория средней стоимости то переменная avg_port равна соответствующим переменным по портам посадки
    if option == "Средняя":
        avg_port = [S_srednee, C_srednee, Q_srednee]

    if option == "Минимальная":
        avg_port = [S_min, C_min, Q_min]

    if option == "Максимальная":
        avg_port = [S_max, C_max, Q_max]

    data = {'Порт посадки': pport, 'Cтоимость билета': avg_port}
    st.table(data)

    fig = plt.figure(figsize=(8, 3))
    plt.bar(pport, avg_port)
    plt.xlabel("Порт посадки")
    plt.ylabel("Стоимость билета")
    plt.title("Средняя стоимость по портам посадки")

    st.pyplot(fig)

if __name__ == "__do_var17__":
    do_var17()