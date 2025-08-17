import requests

API_KEY = "efe804c7746c9c9640bb11d97df7419f"

def get_data(place, forecast_days=None, type_of_forecast=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if type_of_forecast == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if type_of_forecast == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tesla", forecast_days=3, type_of_forecast="Sky"))