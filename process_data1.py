"""розрахунок заявок на товари по магазину
"""

from data_service import get_dovidniks, get_statistics

# структура рядка розрахункової таблиці
analiz = {
    
    'code'  : 0,      # назва устаткування
    'market_name'  : '',      # назва клієнта
    'data_number' : '',      # номер заказа
    'price_potato'          : 0.0,       # кількість
    'price_cabidge '        : 0.0,     # ціна
    'price_onion'        : 0.0,      # сума
    'avaradge_amount'    : 0.0 
}

def create_analiz_list():
    """формування списку заявок по магазину на основі вхідних файлів
    """
    
    def get_dovidnik_name(dovidnik_code):
        """повертає назву клієнта по його коду

        Args:
            dovidnik_code ([type]): код клієнта
        """
        
        for dovidnik in dovidniks:
            if dovidnik_code == dovidnik[0]:
                return dovidnik[1]
        
        return 'назва не знайдена'
    
    analiz_list = []
    
    statistics = get_statistics()
    dovidniks = get_dovidniks()
    
    # послідовна обробка рядків масиву 'orders`
    for statistic in statistics:
        
        # зробити робочий словник з шаблону
        analiz_work = analiz.copy()
        
        # заповнити робочий словник значеннями 
        analiz_work['code']   = statistic[1]
        analiz_work['market_name']  = get_dovidnik_name(statistic[1])
        analiz_work['data_number']           = statistic[0]
        analiz_work['price_potato']         = statistic[2]
        analiz_work['price_cabidge']         = statistic[3]
        analiz_work['price_onion']  = statistic[4]
        analiz_work['avaradge_amount'] = (analiz_work['price_potato'] + analiz_work['price_cabidge'] + analiz_work['price_onion'])/3
        
        # накопичити сформований рядок
        analiz_list.append(analiz_work)
    for item in analiz_list:
        print(item)
create_analiz_list
        
        
        
        

