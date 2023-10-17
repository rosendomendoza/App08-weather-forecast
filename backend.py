import requests

API_KEY = "3a6c42d20430158762fed84f1b12dc18"


def get_data(place, days, type_view):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data = filtered_data[:days * 8]
    time_view = [item['dt_txt'] for item in filtered_data]
    if type_view == "Temperature":
        filtered_data = [item['main']['temp'] for item in filtered_data]
    else:
        filtered_data = [item['weather'][0]['main'] for item in filtered_data]

    return time_view, filtered_data


if __name__ == "__main__":
    dates, temperatures = get_data("VILLAMARTIN", 1, "Sky")
    print(dates)
    print(temperatures)
