def alternatingCharacters(s):
    total = 0
    prev = None
    for char in s:
        if char == prev:
            total += 1
        prev = char
    
    return total