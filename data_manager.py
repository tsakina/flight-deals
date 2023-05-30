import requests

sheet_headers = {
            "Authorization": "Bearer wearestudyingpython",
        }

URL = "https://api.sheety.co/07e851852fb93b82ef145ccda6b4d68e/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=URL, headers=sheet_headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{URL}/{city['id']}", json=new_data, headers=sheet_headers)
            print(response.text)

    def get_customer_emails(self):
        url = "https://api.sheety.co/07e851852fb93b82ef145ccda6b4d68e/flightDeals/users"
        response = requests.get(url=url, headers=sheet_headers)
        data = response.json()["users"]
        return data

