import streamlit as st
import matplotlib.pyplot as plt


#изменения от 06.06.
def  get_bilet(lines):
    with (open('data.csv') as file):
        #вводим переменные с пассажирами и билетами
        S_bilet = 0
        S_passenger = 0
        S_min = -1
        S_max = 0

        C_bilet = 0
        C_passenger = 0
        C_min = -1
        C_max = 0

        Q_bilet = 0
        Q_passenger = 0
        Q_min = -1
        Q_max = 0

        min_valueS = 0

    #разделяем строку на значения и категоию
        for line in file:
            data = line.split(',')

            #исключаем ID пассажира
            if data[0] == 'PassengerId':
                continue

            #высчитываем количество пассажиров с портом пасадки S и общую сумму стоимости билетов
            if data[12].strip() == 'S':
                S_passenger = S_passenger + 1
                S_bilet = S_bilet + float(data[10])

                if (S_min > float(data[10]) or S_min == -1) and float(data[10]) != 0:
                    S_min = float(data[10])
                if S_max < float(data[10]):
                    S_max = float(data[10])

            #высчитываем количество пассажиров с портом пасадки С и общую сумму стоимости билетов
            if data[12].strip() == 'C':
                C_passenger = C_passenger + 1
                C_bilet = C_bilet + float(data[10])

                if (C_min > float(data[10]) or C_min == -1) and float(data[10]) != 0:
                    C_min = float(data[10])
                if C_max < float(data[10]):
                    C_max = float(data[10])

            # высчитываем количество пассажиров с портом пасадки Q и общую сумму стоимости билетов
            if data[12].strip() == 'Q':
                Q_passenger = Q_passenger + 1
                Q_bilet = Q_bilet + float(data[10])

                if (Q_min > float(data[10]) or Q_min == -1) and float(data[10]) != 0:
                    Q_min = float(data[10])
                if Q_max < float(data[10]):
                    Q_max = float(data[10])



    #вводим переменные средней, минимальной и максимальной стоимости по портам посадки и присваиваем им значение из вычеслений выше
    averageS = S_bilet / S_passenger
    averageC = C_bilet / C_passenger
    averageQ = Q_bilet / Q_passenger
    minimumS = round(S_min,2)
    minimumC = round(C_min,2)
    minimumQ = round(Q_min,2)
    maximumS = round(S_max,2)
    maximumC = round(C_max,2)
    maximumQ = round(Q_max,2)

def do_var17():
    st.image('Titanic.jpg')
    st.header('Практическая работа Яковлева А.А.')
    st.write('Вычисление средней, минимальной и максимальной стоимости билета у пассажиров по каждому пункту посадки.')
    option = st.selectbox('Выбирите категорию стоимости билета', ['Средняя', 'Минимальная', 'Максимальная'])
    pport = ['Порт S', 'Порт C', 'Порт Q']

    # если выбрана категория средней стоимости то переменная avg_port равна соответствующим переменным по портам посадки
    if option == "Средняя":
        avg_port = [averageS, averageC, averageQ]

    if option == "Минимальная":
        avg_port = [minimumS, minimumC, minimumQ]

    if option == "Максимальная":
        avg_port = [maximumS, maximumC, maximumQ]

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