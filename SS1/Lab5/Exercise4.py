def possibleWords(wordList, charList):
    # Build dictionary for available characters
    available = {}
    for ch in charList:
        available[ch] = available.get(ch, 0) + 1

    result = []

    for word in wordList:
        # Build dictionary for the current word
        needed = {}
        for ch in word:
            needed[ch] = needed.get(ch, 0) + 1

        # Check if word can be formed
        is_valid = True
        for ch in needed:
            if needed[ch] > available.get(ch, 0):
                is_valid = False
                break

        if is_valid:
            result.append(word)

    return result



print(possibleWords(['fat','tap','day','fun','man','ant','bag','aim'],['m','t','e','d','f','a','p','y','i']))