"""розрахунок аналізів середніх ринкових цін на основні продуктів споживчого кошика
"""
from data_service import get_dovidniks, get_statistics
#накопичувач аналізів ринкових цін
analiz = {
    'code' : 0 ,              # код ринку
    'market_name' : '',       # найменування ринку
    'data_name' : '' ,        # дата
    'price_potato' : 0.0 ,     # ціна катоплі
    'price_cabidge' : 0.0 ,    # ціна капусти
    'price_onion' : 0.0 ,      # ціна цибулі
    'avaradge_amount' : 0.0   # середня ціна

}
def create_analiz():
    """формування списку аналізу даних по ринках на основі вхідних файлів
    """
    def get_dovidnik_name(dovidnik_code):
        """повертає назву ринку по його коду

        Args:
            dovidnik_code ([type]): код ринку
        """
        
        for dovidnik in dovidniks:
            if dovidnik_code == dovidnik[0]:
                return dovidnik[1]
        
        return 'назва не знайдена'

    analiz_list = []
    dovidniks = get_dovidniks()
    statistics = get_statistics()

    #послідовна обробка рядків масиву 'statistics'
    for statistic in statistics:
        analiz_work = analiz.copy()

        analiz_work['code'] = statistic[1]
        analiz_work['market_name'] = get_dovidnik_name(statistic[1])
        analiz_work['data_name'] = statistic[0]
        analiz_work['price potato'] = statistic[2]
        analiz_work['price cabidge'] = statistic[3]
        analiz_work['price onion'] = statistic[4]
        analiz_work['avarage amount'] = (analiz_work['price potato'] + analiz_work['price cabidge'] + analiz_work['price onion'])/3

        analiz_list.append(analiz_work)
    for item in analiz_list:
        print(item)
create_analiz()
