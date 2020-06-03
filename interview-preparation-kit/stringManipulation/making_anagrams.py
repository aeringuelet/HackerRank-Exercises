def makeAnagram(a, b):
    chars = {}

    for c in a:
        chars[c] = chars.get(c, 0) + 1
    
    for c in b:
        chars[c] = chars.get(c, 0) - 1

    amoutToDelete = 0
    for c in chars:
        amoutToDelete += abs(chars[c])

    return amoutToDelete