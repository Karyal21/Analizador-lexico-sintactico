x=0
y=1
z=0
def pedir():
 while True:
  s=input("Ingrese el numero de digitos:")
  n=int(s)
  return n
n=pedir()
if n>1:
   print("1")
if n==1:
   print("1")
n=n-1
for i in range (n):
   z=x+y
   print(z)
   x=y
   y=z