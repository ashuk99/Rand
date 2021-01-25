n = int(input("Enter a number (>1): "))
no_steps = 0

while n != 1:
    if n % 2 == 0:
        n /= 2
        no_steps += 1
    else:
        n = n*3 + 1
        no_steps += 1

print(f'{no_steps} steps')
