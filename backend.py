import requests
API_KEY="62543491d40e0754b157120063e6f73c"
def get_data(place,forecast_days):
    try:
        url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response = requests.get(url)
        data=response.json()
        filtered_data = data["list"] 
        nr_values = 8 * forecast_days
        filtered_data   = filtered_data[:nr_values]
        return filtered_data
    except KeyError:
        return "No data available for this location"

if __name__ == "__main__":
    print(get_data("London",5))


