#SOT base 107 001
a = int(input())

a50 = a//50
a10 = a%50//10
a5 = a%10 //5
a1 = a%5 // 1
#print(a50,a10,a5,a1
print( f'{a}=50*{a50}+10*{a10}+5*{a5}+1*{a1}', end='')