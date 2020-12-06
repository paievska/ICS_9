"""головний модуль додатку
виводить розрахункову таблицю, зберігає розрахунок у файл
показує на екрані первинні дані
"""



from process_data import create_analiz
from data_service import show_dovidniks, show_statistics, get_dovidniks, get_statistics
import os

MAIN_MENU = \
'''
~~~~~~~~~ ОБРОБКА АНАЛІЗІВ СЕРЕДНІХ РИНКОВИХ ЦІН НА ОСНОВІ ПРОДУКТІВ СПОЖИВЧОГО КОШИКА ~~~~~~~~~~

1 - вивід аналізів ринків на екран
2 - запис аналізів ринків в файл
3 - вивід статистичних даних ринків
4 - вивід довідника ринків
0 - завершити роботу
-----------------------------
'''
TITLE = "АНАЛІЗ СЕРЕДНІХ РИНКОВИХ ЦІН НА ОСНОВІ ПРОДУКТІВ СПОЖИВЧОГО КОШИКА"
HEADER = \
'''
=======================================================================================================================================
| Код ринку     |   Найменування ринку       |     Дата     | Ціна за картоплю |   Ціна за капуста  |  Ціна за цибулю  | Середня ціна |
=======================================================================================================================================
'''
FOOTER = \
'''
=======================================================================================================================================
'''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"

def show_analiz(analiz_list):
    """виводить сформовані аналізи на екран у вигляді таблиці

    Args:
        analiz_list ([type]): список аналізів середніх ринкових цін
    """
    
    print(f'\n\n{TITLE:^90}')
    print(HEADER)
    
    for analiz in analiz_list:
        print(f"{analiz['code']:>16.5}",
              f"{analiz['market_name']:18}",
              f"{analiz['data_name']:>24}",
              f"{analiz['price_potato']:>18.2f}"
              f"{analiz['price_cabidge']:>19.2f}"
              f"{analiz['price_onion']:>19.2f}"
              f"{analiz['avaradge_amount']:>17.2f}"
              )
    

    print(FOOTER)


def write_analiz(analiz_list):
    """пише список аналізів середніх ринковх цін у файл

    Args:
        analiz_list ([type]): список аналізів
    """
    
    with open('analiz.txt', "w") as analiz_file:
        for analiz in analiz_list:
            line = \
                str(analiz['code']) + ';' +      \
                analiz['market_name'] + ';' +      \
                analiz['data_name']  + ';' +      \
                str(analiz['price_potato'])  + ';' +   \
                str(analiz['price_cabidge'])  + ';' + \
                str(analiz['price_onion'])  + ';' + \
                str(analiz['avaradge_amount']) + '\n' 
                
            analiz_file.write(line)
        
        
        print("Файл заявок сформовано ...")
    

while True:
    
    # вивід головного меню
    os.system('cls')
    print (MAIN_MENU)
    command_number = input('Введіть номер команди: ')

    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        analiz_list = create_analiz()
        show_analiz(create_analiz())
        input(STOP_MESSAGE)
    
    elif command_number == '2':
        analiz_list = create_analiz()
        write_analiz(analiz_list)
        input(STOP_MESSAGE)
    
    elif command_number == '3':
        show_statistics(get_statistics())
        input(STOP_MESSAGE)
    
    elif command_number == '4':
        show_dovidniks(get_dovidniks())
        input(STOP_MESSAGE)
        
    else:
        print("невірний номер команди...")
        input(STOP_MESSAGE)
