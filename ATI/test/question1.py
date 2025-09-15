import re

def ticketValidator(code):
    not_allowed_code = ["VNA", "BAM", "JET", "VJA", "AGR"]
    # Check length
    if len(code) != 8:
        return False
    # Check forbidden airline codes
    airline_code = code[:3]
    if airline_code in not_allowed_code:
        return False
    # Check format: first 3 uppercase letters, next 4 digits, last char uppercase letter or digit
    if not re.match(r"^[A-Z]{3}[0-9]{4}[A-Z0-9]$", code):
        return False
    # Check for three consecutive identical characters
    for i in range(len(code) - 2):
        if code[i] == code[i+1] == code[i+2]:
            return False
    return True

    # if not (code[:3].isalpha() and code[:3].isupper()):
    #     return False
    # if not code[3:7].isdigit():
    #     return False
    # if not (code[7].isupper() or code[7].isdigit()):
    #     return False

print(ticketValidator("GHG1234A"))
print(ticketValidator("HOT5678Z"))
print(ticketValidator("XYZ134AA"))
print(ticketValidator("VNA12AA3"))
print(ticketValidator("VNA1111B"))
print(ticketValidator("AAA1234B"))