import json
import requests as rq

def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load url")

def load_json(data):
    if not data is None:
        j=json.load(data)
        fname=j["results"][0]["name"]["first"]
        lname=j["results"][0]["name"]["last"]
        email=j["results"][0]["email"]
        return fname,lname,email

def main():
    url = "https://randomuser.me/api"
    values = load_json(get_data(url))
    if not values is None:
        print("First value", values[0])
        print("Last value", values[1])
        print("Email", values[2])


if __name__ == '__main__':
    main()


#api.openweathermap.org/data/2.5/weather?q=London