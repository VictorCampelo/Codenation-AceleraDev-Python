from datetime import datetime
from operator import itemgetter

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def minutes(seconds):
    return divmod(seconds, 60) # Seconds in a minute = 60

def classify_by_phone_number(records):
    costs = []
    for record in records:
        total = 0.36
        end = datetime.fromtimestamp(record['end'])
        start = datetime.fromtimestamp(record['start'])
        duration = end - start
        if start.hour >= 6 and start.hour <= 22:
            if (end.hour >= 22 or end.hour == 0) and end.minute > 0 :
                total += ((minutes(duration.total_seconds())[0] - end.minute) * 0.09)
            else:
                total += (minutes(duration.total_seconds())[0] * 0.09)
        if costs:
            flag = 0
            for cost in costs:
                if cost['source'] == record['source']:
                    cost['total'] = round((cost['total'] + round(total,2)), 2)
                    flag = 1
                    break
            if flag == 0:
                costs.append({'source': record['source'], 'total': round(total,2)})
        else:
            costs.append({'source': record['source'], 'total': round(total,2)})
    
    costs = sorted(costs, key=itemgetter('total'), reverse=True) 
    return costs