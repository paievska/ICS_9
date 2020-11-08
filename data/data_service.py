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




def get_statistics():
    """повертає список статистики данних ринків з файла 'statistics.txt' 
    
    Returns:
        statistics_list : список статистики данних ринків
    """

    from_file = [
        "02.11.2016;100;45;50;70",
        "02.11.2016;200;35;30;50",
        "02.11.2016;300;35;30;45",
        "14.11.2016;100;45;45;60",
        "14.11.2016;200;40;40;50",
        "14.11.2016;300;35;35;45",
        "22.11.2016;100;40;40;60",
        "22.11.2016;200;40;40;50",
        "22.11.2016;300;40;40;60"

    ]

    #накопичувач статистик данних ринків

    statistics_list = []

    for line in from_file:
        line_list = line.split(';')
        statistics_list.append((line_list))

    return statistics_list

statistic = get_statistics()

for c in statistic:
    print(c)
    



