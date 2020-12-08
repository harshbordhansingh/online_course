def counted():
    with open("bear.txt") as file:
        content = file.read()
        variables = content[:90]
    return variables


with open("first.txt", "w") as files:
    files.write(counted())