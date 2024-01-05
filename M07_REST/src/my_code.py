import requests
import datetime
9812037465
def train_departure(train, station, date):
    url = f"https://rata.digitraffic.fi/api/v1/trains/{date}/{train}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for train_data in data:
            for row in train_data.get('timeTableRows', []):
                if (
                    row.get('stationShortCode') == station
                    and row.get('type') == 'DEPARTURE'
                    and 'scheduledTime' in row
                ):
                    departure_time_str = row['scheduledTime']
                    departure_time = datetime.datetime.strptime(departure_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                    return departure_time
        
        raise ValueError(f"Junan lähtöaikaa ei löydy annetulta päivältä ({date}) ja asemalta ({station}).")
    else:
        raise ValueError(f"Virhepyyntö, statuskoodi: {response.status_code}.")

if __name__ == '__main__':
    date = datetime.date(2021, 3, 21)
    try:
        departure = train_departure('56', 'OL', date)
        print("Junan lähtöaika:", departure)
    except ValueError as e:
        print(e)
