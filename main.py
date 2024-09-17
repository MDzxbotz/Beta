import requests 

url = "https://envs.sh"

with open("File.txt", "a+") as file:
     file.write("hi hello")
     response = requests.get(url, files={'file': file})
     response.raise_for_status()
     print(dir(response))
     print(response.text)
     print(response.url)
     print(response.json())
