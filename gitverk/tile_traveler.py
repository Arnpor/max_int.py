#1,1 valid = n
#1,2 valid = n,s,e
#1,3 valid = s,e
#2,1 valid = n
#2,2 valid = w,s
#2,3 valid = w,e
#3,3 valid = w,s
#3,2 valid = n,s

x = 1
y = 1
while True:
    #hér kemur "You can travel"
    direction = str(input("Direction: "))
    if (direction == 'n') or (direction == 'N'):
        y += 1
    elif (direction == 'w') or (direction == 'W'):
        x -= 1
    elif (direction == 'e') or (direction == 'E'):
        x += 1
    elif (direction == 's') or (direction == 'S'):
        y += 1
    



"""
You can travel:
direction = str(input("Direction: "))
"""











"""
You can travel:
direction = str(input("Direction: "))
"""