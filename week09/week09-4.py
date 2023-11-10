a = list(map(int, input().split())) #斷開,整數,變數
ans = a[0]  #取前面的數字 a[0]
for x in a:  #for迴圈,把a的每個數字x都選一次
  if x>ans:   #如果現在的比ans還大
    ans = x   #更新答案
print('最大值是:', ans) #離開迴圈時,便找到ans

for x in a:
  print(x)