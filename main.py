import streamlit as st

# from var04 import do_var04
# from var06 import do_var06
# from var11 import do_var11
from var13 import do_var13
# from var14 import do_var14
# from var17 import do_var17

st.image('titanik-50.jpg')
choice = st.selectbox ('Номер варианта:', ['Вариант №04', 'Вариант №06', 'Вариант №11', 'Вариант №13', 'Вариант №14', 'Вариант №17'])

if choice == 'Вариант №04':
    #do_var04()
    st.write ('К сожалению данная страница находится в разработке. Но скоро вы сможете узнать процент выживших молодых (до 30) и старых (после 60) пассажиров, указав класс билета. Приносим свои извинения.')
elif choice == 'Вариант №06':
    # do_var06()
    st.write ('К сожалению данная страница находится в разработке. Но скоро вы сможете узнать среднюю стоимость билета у спасенных и погибших, выбрав из списка порт посадки. Приносим свои извинения.')
elif choice == 'Вариант №11':
    # do_var11()
    st.write ('К сожалению данная страница находится в разработке. Но скоро вы сможете узнать долю погибших и спасенных пассажиров, указав возрастную категорию из списка - «молодой» (до 30 лет), «среднего возраста» (от 30 до 60) и «старый» (более 60 лет). Приносим свои извинения.')
elif choice == 'Вариант №13':
    do_var13()
    # st.write ('К сожалению данная страница находится в разработке. Но скоро вы сможете узнать количество погибших детей по каждому пункту посадки, указав максимальный возраст (число от 1 до 18). Приносим свои извинения.')
elif choice == 'Вариант №14':
    # do_var14()
    st.write ('К сожалению данная страница находится в разработке. Но скоро вы сможете узнать число родственников отдельно для выживших и погибших пассажиров указанного пола. Приносим свои извинения.')
elif choice == 'Вариант №17':
    # do_var17()
    st.write ('К сожалению данная страница находится в разработке. Но скоро вы сможете узнать среднюю, минимальную или максимальную стоимость билета у пассажиров по каждому пункту посадки. Приносим свои извинения.')