twenty = 20
number = 0
while twenty > number:
    number += 1
    if number == 4:
        print(f'{number} is unlucky')
    elif number == 13:
        print(f'{number} is unlucky')
    elif number % 2:
        print(f"{number} is even")
    elif:
        print(f"{number} is odd")
        
   #alternative
for num in range(1,21):
    if num == 4 or num ==13:
        state ="unlucky"
    elif num % 2 ==:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")
