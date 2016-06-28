def half(entStr):
    evens = ""
    odds = ""    
    if len(entStr) % 2 ==0:
        for i in range(len(entStr)/2-1, -1,-1):
            evens = entStr[i] + evens
        print evens
    if not (len(entStr) % 2 ==0):
        for i in range((len(entStr)-1)/2,-1, -1):
            odds = entStr[i] + odds
        print odds 