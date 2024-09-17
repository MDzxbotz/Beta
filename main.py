import requests 

url = "https://envs.sh"

with open("test.jpg", "rb") as file:
     file.seek(1)
     response = requests.post(url, files={'file': file})
     response.raise_for_status()
     print(dir(response))
     print(response.text)
     print(response.url)
     print(response.json())
