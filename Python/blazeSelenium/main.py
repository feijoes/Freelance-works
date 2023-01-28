import seleniumBot
import requests
  
def login():
    with open(".env") as f:
        lines: list[str] = [line.strip("\n") for line in f.readlines()]
        user , password = lines[0] ,lines[1]
    seleniumBot.login(user,password)

#getDouble()

# api-endpoint
URL = "http://127.0.0.1:8000"
  
# sending get request and saving the response as response object
r = requests.get(url = URL)
print(r.json())

