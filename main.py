import requests 

url = "https://envs.sh"

with open("File.txt", "a+") as file:
     file.write("hi hello")
     response = requests.post(url, files={'file': file})
     print(response.json())
