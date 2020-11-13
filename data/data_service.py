"""модуль призначено для роботи з файлами вхідних данних"""



def get_dovidnik():
    """повертає список клієтів з файла 'dovidnik.txt'
    
    Returns:
        dovidnik_list : список ринків
    """
    
    with open('./data/dovidnik.txt') as dovidnik_file:
        from_file = dovidnik_file.readlines()
   
    dovidnik_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidnik_list.append((line_list))
    
    
    return dovidnik_list






def get_statistics():
    """повертає список статистики данних ринків з файла 'statistics.txt' 
    
    Returns:
        statistics_list : список статистики данних ринків
    """

    with open('./data/statistics.txt') as statistics_file:
        from_file = statistics_file.readlines()

    #накопичувач статистик данних ринків

    statistics_list = []

    for line in from_file:
        line_list = line.split(';')
        statistics_list.append((line_list))

    return statistics_list




def show_dovidnik(dovidnik):
    """виводить елементи довідника на екран

    Args:
        dovidnik (list): список елементів
    """

    for c in dovidnik:
        print("код ринка:{:3} назва ринку: {:3}"
            .format(c[0], c[1] ))


def show_statistics(statistics):
    """виводить статистичі дані про ринкові ціни на екран

    Args:
        statistic (list): список даних про ринкові ціни
    """
    for c in statistics:
        print("дата:{:5} код ринку:{:5} ціна за картоплю:{:5} ціна за капусту:{:5} ціна за цибулю:{:5}"
            .format(c[0], c[1], c[2], c[3], c[4]))
        
    



