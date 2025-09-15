import re

def ticketValidator2(code):
    not_allowed_code = ["VNA", "BAM", "JET", "VJA", "AGR"]
    errors = []
    if len(code) != 8:
        errors.append("Ticket code must be exactly 8 characters")
    airline_code = code[:3]
    if airline_code in not_allowed_code:
        errors.append("Invalid. Airline code is not allowed")
    if not (code[:3].isalpha() and code[:3].isupper()):
        errors.append("First 3 characters must be uppercase letters")
    if not code[3:7].isdigit():
        errors.append("Next 4 characters must be digits")
    if not (code[7].isupper() or code[7].isdigit()):
        errors.append("Last character must be uppercase letter or digit")
    for i in range(len(code) - 2):
        if code[i] == code[i+1] == code[i+2]:
            errors.append("Ticket code contains three consecutive identical characters")
            break
    if not errors:
        return "Valid"
    return ". ".join(errors)

print(ticketValidator2("GTR1234A"))      # Valid
print(ticketValidator2("VNA1234A"))      # Invalid. Airline code is not allowed
print(ticketValidator2("htr12AA3"))      # First 3 characters must be uppercase letters. Next 4 characters must be digits
print(ticketValidator2("VNA1111#"))      # Invalid. Airline code is not allowed. Ticket code contains three consecutive identical characters. Last character must be uppercase letter or digit