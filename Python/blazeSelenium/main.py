import seleniumBot

  
def login():
    with open(".env") as f:
        lines: list[str] = [line.strip("\n") for line in f.readlines()]
        user , password = lines[0] ,lines[1]
    seleniumBot.login(user,password)

seleniumBot.getDouble()

