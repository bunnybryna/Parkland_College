def reverse(entStr):
    holder = "" 
    for i in range(0, len(entStr)):
        holder = entStr[i] + holder
    print holder