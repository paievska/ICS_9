"""модуль призначено для роботи з файлами вхідних данних"""



def get_dovidnik():
    """повертає список клієтів з файла 'dovidnik.txt'
    
    Returns:
        dovidnik_list : список ринків
    """

    from_file = [
        "100;Бессарабський",
        "200;Житній",
        "300;Володимирський"
    ]
    
    #накопичувач ринків
    dovidnik_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidnik_list.append((line_list))
    
    
    return dovidnik_list


dovidnik = get_dovidnik()

for c in dovidnik:
    print(c)


"""модуль призначено для роботи з файлами вихідних данних"""

def get_analiz():
    """повертає список аналізу цін ринків з файла 'analiz.txt' 
    
    Returns:
        analiz_list : список аналізу цін ринків
    """

    from_file = [
        "100;Бесарабський;02.11.2016;45,00;50,00;70,00;55,00",
        "100;Бесарабський;14.11.2016;45,00;45,00;60,00;50,00",
        "100;Бесарабський;22.11.2016;40,00;40,00;60,00;46,67",
        "300;Володимирський;02.11.2016;35,00;30,00;45,00;36,67",
        "300;Володимирський;14.11.2016;35,00;35,00;45,00;38,33",
        "300;Володимирський;22.11.2016;40,00;35,00;60,00;45,00"

    ]

    #накопичувач аналізу цін ринків

    analiz_list = []

    for line in from_file:
        line_list = line.split(';')
        analiz_list.append((line_list))

    return analiz_list

analiz = get_analiz()

for c in analiz:
    print(c)
    


