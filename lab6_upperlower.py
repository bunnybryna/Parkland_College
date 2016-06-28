def upperLower(entStr):
    holderUp = ""
    holderLow = ""
    for i in range(len(entStr)):
        current_value = int(ord(entStr[i]))
        if current_value >= 65 and current_value <= 90:
            holderUp = holderUp + entStr[i]
        if current_value >= 97 and current_value <= 122:
            holderLow = holderLow + entStr[i]
    print holderUp
    print holderLow