def repeatedString(s, n):
    repeat = n // len(s)
    occOnInitialString = s.count('a', 0, n)
    occSubTotal = repeat * occOnInitialString
    
    lastAmountOfLetters = n % len(s)
    amountInLastString = 0
    i = 1
    for letter in s:
        if i > lastAmountOfLetters:
            break
        i = i + 1
        if letter == 'a':
            amountInLastString = amountInLastString + 1
    
    return occSubTotal + amountInLastString