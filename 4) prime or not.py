n=int(input())
is_flag=False
for i in range(2,n):
    if(n%i==0):
        is_flag=True
        break
if is_flag:
    print("0")
else:
    print("1")
