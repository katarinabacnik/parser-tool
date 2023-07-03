import os

import requests

from file_helpers import validate_folder_path


def download(url: str, folder_path: str) -> None:
    validate_folder_path(folder_path)
    file_path = os.path.join(folder_path, url.split("/")[-1])
    with open(file_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
        print(f"Downloaded {url} to {file_path}")


def main():
    url = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/blood_pressure.csv"
    folder = "data"
    download(url, folder)


main()
