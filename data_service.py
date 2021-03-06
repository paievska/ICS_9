"""модуль призначено для роботи з файлами вхідних данних"""



def get_dovidniks():
    """повертає список клієтів з файла 'dovidniks.txt'
    
    Returns:
        dovidniks_list : список ринків
    """
    
    with open('\\ICS_9\\data\\dovidniks.txt') as dovidniks_file:
        from_file = dovidniks_file.read().splitlines()
    
    #накопичування елеменів довідника
   
    dovidniks_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidniks_list.append((line_list))
    
    return dovidniks_list
   






def get_statistics():
    """повертає список статистики данних ринків з файла 'statistics.txt' 
    
    Returns:
        statistics_list : список статистики данних ринків
    """

    with open('\\ICS_9\\data\\statistics.txt') as statistics_file:
        from_file = statistics_file.readlines()

    #накопичувач статистичних даних ринків

    statistics_list = []

    for line in from_file:
        line_list = line.split(';')
        line_list[2] = int(line_list[2])
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        statistics_list.append((line_list))

    return statistics_list





def show_dovidniks(dovidniks):
    """виводить елементи довідника на екран

    Args:
        dovidnik (list): список елементів
    """

    
    for dovidnik in dovidniks:
        print("код ринку: {:5} назва ринку: {:5}" .format(dovidnik[0], dovidnik[1]))
        
        


def show_statistics(statistics):
    """виводить статистичі дані про ринкові ціни на екран

    Args:
        statistic (list): список даних про ринкові ціни
    """
    for c in statistics:
        print("дата:{:5} код ринку:{:5} ціна за картоплю:{:5} ціна за капусту:{:5} ціна за цибулю:{:5}"
            .format(c[0], c[1], c[2], c[3], c[4]))
        


#dovidniks = get_dovidniks()
#show_dovidniks(dovidniks)

#statistics = get_statistics()
#show_statistics(statistics)

