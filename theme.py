theme_file = open("theme.txt", "a")

while True:
    try:
        line = input()
    except EOFError:
        print("終わり")
        break
    else:
        if line:
            theme_file.write(line)
        else:
            theme_file.write("\n")

theme_file.close()