def addition():
    total = 0
    count = 0
    num = float(input("Enter a number/Enter to exit: "))
    while len(str(num)) > 0:
        total = total + float(num)
        count = count + 1
        num = input("Enter another number/Enter to calculate: ")
    return f'Sum is ==> {total} \nTotal numbers entered are ==> {count}'


def subtraction():
    total = 0
    count = 0
    num = float(input("Enter a number/Enter to exit: "))
    while len(str(num)) > 0:

        num = float(num)
        if total == 0 and count == 0:
            total = num
        else:
            total = total - num
        count += 1
        num = input("Enter another number/Enter to calculate: ")
    return f'Subtracted value is ==> {total}\n Total number entered is ==> {count}'


def multiplication():
    count = 0
    total = 0
    num = float(input("Enter a number/Enter to exit: "))
    while len(str(num)) > 0:
        num = float(num)
        if count == 0:
            total = 1 * num
        else:
            total = total * num
        count += 1
        num = input("Enter another number/Enter to calculate: ")
    return f'Multiplied value is ==> {total}\nTotal numbers entered is ==> {count}'


def division():
    total = 0
    count = 0
    num = float(input("Enter a number/ Enter to exit: "))
    while len(str(num)) > 0:
        num = float(num)
        if num == 0:
            total = 0
        else:
            total = total / num
        count += 1
        num = input("Enter another number/Enter to calculate: ")
    return f'Division value is ==> {round(total, 2)}\nTotal number entered is ==> {count}'


def average():
    count = 0
    total = 0
    num = float(input("Enter a number/Enter to exit: "))
    while len(str(num)) > 0:
        num = float(num)
        total = total + num

        count += 1
        num = input("Enter another number/Enter to calculate:")
    return f'Average value is ==> {round(total / count, 2)}\nTotal numbers entered is ==> {count}'


while True:
    print("** Lets build a calculator **\n")
    print("Choose a math operation:-> ")
    print(">   ADD --> Addition")
    print(">   SUB --> Subtraction")
    print(">   MUL --> Multiplication")
    print(">   DIV --> Division")
    print(">   AVG --> Average")
    print(">   Q --> Exit")

    choice = input("Input math operation --> ")
    if choice == 'Q':
        break

    elif choice == 'ADD':
        print(addition())
        flag = input("Do you want to continue(Y/N): ")
        if flag == "N":
            break

    elif choice == "SUB":
        print(subtraction())
        flag = input("Do want to continue(Y/N): ")
        if flag == "N":
            break

    elif choice == 'MUL':
        print(multiplication())
        flag = input("Do want to continue(Y/N): ")
        if flag == "N":
            break

    elif choice == 'DIV':
        print(division())
        flag = input("Do want to continue(Y/N): ")
        if flag == "N":
            break

    elif choice == 'AVG':
        print(average())
        flag = input("Do want to continue(Y/N): ")
        if flag == "N":
            break













