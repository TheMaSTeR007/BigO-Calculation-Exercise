# // What is the Big O of the below function? //

# In this program we calcaulte the Big O Notation of function --> which is written on the right side of every line of function as a comment.

# Here is a Function which prints some calculation defined in function
def adderMultiplier(input):
  a = 5  # O(1)
  b = 10 # O(1)
  c = 15 # O(1)

  for i in range(input):   # O(n)
    x = i + 1  # O(n)
    y = i + 2  # O(n)
    z = i + 3  # O(n)
    print(x,y,z) # O(n)

  for j in range(input):  # O(n)
    p = j * 2  # O(n)
    q = j * 3  # O(n)
    print(p,q) # O(n)

  print("Function has ended") # O(1)

adderMultiplier(5)

# So here we get to know that the Big O notation for above funciton is :

# O(1) + O(1) + O(1) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(1) = 1 + 1 + 1 + n + n + n + n + n + n + n + n + n + 1 = 4 + 9n

# BigO notation is --> 4 + 9n for above function
