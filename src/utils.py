from datetime import datetime


def get_first_week_day(dt):
    return datetime.strptime(dt + '-1', "%Y-%W-%w")


def get_statictic(articles, limit):
    year = datetime.now().year
    cur_week = datetime.now().isocalendar()[1]

    ## init
    statistic = {}
    for i in range(limit):
        if cur_week - i < 0:
            year -= 1
            cur_week += 48

        w_key = f'{year}-{cur_week - i}'
            
        statistic[w_key] = {
            'start_at': get_first_week_day(w_key),
            'value_avg':0,
            'count': 0,
        }
    
    ## update article info
    for article in articles:
        week = article.time.isocalendar()[1]
        w_key = F'{article.time.year}-{week}'

        if statistic.get(w_key, 0):
            statistic[w_key]['value_avg'] += article.emotional_value
            statistic[w_key]['count'] += 1

    ## turn to list
    data = []
    for _, val in statistic.items():
        val['value_avg'] /= val['count'] if val['count'] != 0 else 1
        data.append(val)

    return data
