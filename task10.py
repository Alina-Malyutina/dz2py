n = int(input('Enter quantity of coins: '))
countHeads = 0
CountTails = 0
for i in range(n):
    coin = int(input('Enter side of coin - 1 - head, 0 - tail: '))
    if coin == 1:
        countHeads += 1
    elif coin == 0:
        CountTails += 1
    else:
        print('Something is uncorrect!')
if countHeads > CountTails:
    print(f"Need to flip tails - there is {CountTails}")
elif countHeads < CountTails:
    print(f"Need to flip heads - there is {countHeads}")
else:
    print(f"There is no difference what to flip -there is {countHeads} heads and {CountTails} tails ")
