l=list(map(int,input().split()))
n=int(input("Number to be searched :"))
for i in range(len(l)):
  if l[i]==n:
    print(i)
