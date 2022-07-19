# Check if s1 and s2 are anagrams of each other
def validAnagram(s1, s2):

    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    d1 = {}
    d2 = {}

    for letter in s1:
        if letter in d1:
            d1[letter] += 1
        else:
            d1[letter] = 1

    for letter in s2:
        if letter in d2:
            d2[letter] += 1
        else:
            d2[letter] = 1

    if d1 == d2:
        return True
    else:
        return False

    
    

print(validAnagram("gdsay", "dayg"))