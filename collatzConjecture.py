#Famous problem: any whole interger entered will always become 1

count = 0
num = int(input('Enter a number: '))

while num != 1:
    
    if num % 2 == 0:
        num = (num // 2)

        count += 1
        print(count, ':', num)

    elif num % 2 != 0:
        num = ((3 * num) + 1)

        count += 1
        print(count, ':', num)
