import json
import os

def add_client(client_data):
    data_file = "data/clients.json"

    if not os.path.exists(data_file):
        # Create an empty list if the file doesn't exist
        with open(data_file, "w") as json_file:
            json.dump([], json_file)

    with open(data_file, "r") as json_file:
        clients = json.load(json_file)
        clients.append(client_data)

    with open(data_file, "w") as json_file:
        json.dump(clients, json_file)

def get_all_clients():
    with open("data/clients.json", "r") as json_file:
        clients = json.load(json_file)
    return clients