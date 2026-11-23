try:
    with open("abc.txt","r") as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("File not Found!")