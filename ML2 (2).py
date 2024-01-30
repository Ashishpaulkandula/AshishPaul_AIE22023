print("enter the noof elements")
l=[]
n=int(input())
if (n<3):
    print("give more numbers")
else:
    for i in range(n):
      m=int(input())
      l.append(m)
    L=len(l)
    for i in range(L-1):
      for j in range(L-1-i):
         if (l[j]< l[j+1]):
          temp=l[j]
          l[j]=l[j+1]
          l[j+1]=temp
      print("the sorted list is")
      print(l)
      B=l[0]
      S=l[L-1]
 
      diff=(B-S)
      print(diff)
