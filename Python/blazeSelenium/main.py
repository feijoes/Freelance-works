import os

def main():
    with open(".env") as f:
        lines: list[str] = [line.strip("\n") for line in f.readlines()]
        user , password = lines[0] ,lines[1]
        
    os.system(f"seleniumBot.py {user} {password}")

main()