import csv
import streamlit as st
import matplotlib.pyplot as plt


def load_data(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Age']:
                try:
                    row['Age'] = float(row['Age'])
                    data.append(row)
                except ValueError:
                    pass
    return data


def count_deceased_children(data, max_age):
    embarked_counts = {'C': 0, 'Q': 0, 'S': 0}
    for row in data:
        if row['Age'] <= max_age and row['Survived'] == '0':
            embarked_counts[row['Embarked']] += 1
    return embarked_counts


def do_var13():
    st.image('titanik-50.jpg')
    st.title('Количество погибших детей на Титанике по каждому пункту посадки')

    file_path = 'data.csv'
    data = load_data(file_path)

    max_age = st.number_input('Введите максимальный возраст для подсчета детей'
                              ' (1-18):',
                              min_value=1, max_value=18, value=18)

    if st.button('Показать результаты'):
        embarked_counts = count_deceased_children(data, max_age)

        table_data = [
            ['Шербур', embarked_counts['C']],
            ['Квинстаун', embarked_counts['Q']],
            ['Саутгемптон', embarked_counts['S']]
        ]

        st.write(f"Количество погибших детей (возраст до"
                 f" {max_age} включительно) по пунктам посадки:")
        st.table(table_data)

        ports = ['Шербур', 'Квинстаун', 'Саутгемптон']
        counts = [embarked_counts['C'], embarked_counts['Q'],
                  embarked_counts['S']]

        fig, ax = plt.subplots()
        ax.bar(ports, counts, color=['blue', 'green', 'red'])
        ax.set_xlabel('Порты посадки')
        ax.set_ylabel('Количество погибших детей')
        ax.set_title(f'Количество погибших детей (возраст до'
                     f' {max_age} включительно) по пунктам посадки')

        st.pyplot(fig)


if __name__ == "__do_var13__":
    do_var13()
