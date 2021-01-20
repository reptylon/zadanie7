def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print('Jan',  'Kowal', 'pesel: 90122413426', age=33)

# Wniosek: Funkcje z zadania można wywołać bez błędu bez wprowadzania w niej zmian.
