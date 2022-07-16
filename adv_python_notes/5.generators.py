def firstn_generator(n):
   num = 0
   while num < n:
      yield num
      num +=1

first_n = firstn_generator(10)

def fibonacci_generator():
    n1=0
    n2=1
    c = 0
    while c < 100000 :
        yield n1
        n1, n2 = n2, n1 + n2
        c+=1
        

print(sum(fibonacci_generator()))