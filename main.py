import streamlit as st

# from var11 import do_var11
# from var12 import do_var12
# from var13 import do_var13
# from var14 import do_var14
# from var15 import do_var15
# from var16 import do_var16

st.image('titanik-50.jpg')
choice = st.selectbox ('Номер варианта:', ['Вариант №11', 'Вариант №12', 'Вариант №13', 'Вариант №14', 'Вариант №15', 'Вариант №16'])

if choice == 'Вариант №11':
    #do_var11()
    st.write ('Вариант 11 не сделан')
elif choice == 'Вариант №12':
    # do_var12()
    st.write ('Вариант 12 не сделан')
elif choice == 'Вариант №13':
    # do_var13()
    st.write ('Вариант 13 не сделан')
elif choice == 'Вариант №14':
    # do_var14()
    st.write ('Вариант 14 не сделан')
elif choice == 'Вариант №15':
    # do_var15()
    st.write ('Вариант 15 не сделан')
elif choice == 'Вариант №16':
    # do_var16()
    st.write ('Вариант 16 не сделан')