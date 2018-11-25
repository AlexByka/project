def get_value(key: str) -> str:
    with open("example.db", "r") as file:
        for line in file:
            if key + ":" in line:
                #return line[len(key) +1:-1] # 1 способ получения ключа по значению
                #return line.split(":")[1] # 2 способ получения ключа по значению
                return line.split(":")[1].replace("\n","") # 3 способ получения ключа по значению

print(get_value("user2"))