

def convertOnes(num):
    if num == 1: return "one"
    elif num == 2: return "two"
    elif num == 3: return "three"
    elif num == 4: return "four"
    elif num == 5: return "five"
    elif num == 6: return "six"
    elif num == 7: return "seven"
    elif num == 8: return "eight"
    elif num == 9: return "nine"
    else: return ""

def readOneDigit(num):
    result = ""
    return convertOnes(num % 10)

print(readOneDigit(5))

def convertTeens(num):
    if num == 10: return "ten"
    elif num == 11: return "eleven"
    elif num == 12: return "twelve"
    elif num == 13: return "thirteen"
    elif num == 14: return "fourteen"
    elif num == 15: return "fifteen"
    elif num == 16: return "sixteen"
    elif num == 17: return "seventeen"
    elif num == 18: return "eighteen"
    elif num == 19: return "nineteen"
    else: return ""

def convertTens(num):
    if num == 2: return "twenty"
    elif num == 3: return "thirty"
    elif num == 4: return "forty"
    elif num == 5: return "fifty"
    elif num == 6: return "sixty"
    elif num == 7: return "seventy"
    elif num == 8: return "eighty"
    elif num == 9: return "ninety"
    else: return ""

def readFourDigits(num):
    result = ""

    # Thousands
    if num >= 1000:
        result += convertOnes(num // 1000) + " thousand"
        num = num % 1000
        if num > 0:
            result += " and "

    # Hundreds
    if num >= 100:
        result += convertOnes(num // 100) + " hundred"
        num = num % 100
        if num > 0:
            result += " and "

    # Tens and Ones
    if num >= 20:
        result += convertTens(num // 10)
        if num % 10 != 0:
            result += " " + convertOnes(num % 10)
    elif num >= 10:
        result += convertTeens(num)
    elif num > 0:
        result += convertOnes(num)

    return result.strip()


def readFourDigits(num: int) -> str:
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    words = []

    # Thousands
    if num >= 1000:
        words.append(ones[num // 1000] + " thousand")
        num %= 1000

    # Hundreds
    if num >= 100:
        words.append(ones[num // 100] + " hundred")
        num %= 100

    # Tens and Ones
    if num > 0:
        if len(words) > 0:
            words.append("and")   # add "and" between groups

        if num < 10:
            words.append(ones[num])
        elif num < 20:
            words.append(teens[num - 10])
        else:
            words.append(tens[num // 10])
            if num % 10 != 0:
                words.append(ones[num % 10])

    return " ".join(words).strip()


