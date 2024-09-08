import random

def seened(n):
    seente_list = ["puravik", "kukeseen", "pilvik"]
    seen = random.choice(seente_list)
    print(f"Pilvi võttis seene {seen}")
    if seen == "puravik":
        if n == 1:
            return 1
        else:
            n -= 1        
    return 1 + seened(n)
print(seened(3))
#16.04 - 16.05
#16.26 - 16-39

#14min