#a = [1,1,2,3,5,8,13,21]
a = [1,1]
for i in range(2,40):  #課本的第三章list的第3-6頁  .append()
  a.append( a[i-1] + a[i-2] ) #利用 .append()  在最後面加一項
  # a[i] = a[i-1] + a[i-2]
print(a)