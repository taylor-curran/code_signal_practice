def csFindAddedLetter(str_1, str_2):
    
    # Make a Dictionary of Counts
    counts_1 = {}
    for char in str_1:
        if char in counts_1:
            counts_1[char] +=1
        else:
            counts_1[char] = 1

    counts_2 = {}
    for char in str_2:
        if char in counts_2:
            counts_2[char] +=1
        else:
            counts_2[char] = 1

    for char in str_2:
        if char not in counts_1:
            return char
        else:
            if counts_2[char] == counts_1[char]:
                pass
            else:
                return char