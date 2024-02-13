import json
import os


def read_configuration():
    config_file = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "config/config.json")
    with open(config_file, "r") as json_file:
        return json.load(json_file)
