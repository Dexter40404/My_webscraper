def count():
    with open("output.txt", "r", encoding='utf-8') as file:
        output = []
        for line in file:
            words = line.find("total words")
            if words == 0:
                num = line.split(": ")[1]
                x = num.strip()
                output.append(x)


    total = "Total is: " + str(sum(int(num)for num in output)) + '.'
    print(total)

