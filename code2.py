def series (series_name,n):
   if series_name =="fibonacci":
   a = 1
   b = 1
 elif series_name == " lucas" :
a = 2 
b = 1

result = []
while len(result) != n:
result.append(a)
next_fib = a + b
a = b 
b = next_fib

