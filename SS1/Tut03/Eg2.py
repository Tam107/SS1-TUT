def getNonDuplicate(n):
    result = list()
    while len(result) < n:
        try:
            num = int(input("Please enter a number: "))
            if num not in result:
                result.append(num)
            else:
                print("This number already exists in the list. Please enter a new number")
        except ValueError:
            print("Please enter an integer")
    return result


print(getNonDuplicate(5))
