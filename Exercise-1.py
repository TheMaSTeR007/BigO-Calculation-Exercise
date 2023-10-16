# In this program we calcaulte the Big O Notation of function --> which is written on the right side of every line of function as a comment.

# Here is a Function which prints a string Entered by user as many times directed by the user.
def StringMultiplier(string,multiplier):
    
    text = "The string is multiplied :" # O(1)
    times = "times" # O(1)
    till = "till now" # O(1)

    for i in range(multiplier): # O(n)
        message = f"{string} --> {text} {i+1} {times} {till}." # O(n)
        print (message) # O(n)
        print("-"*len(message)) # O(n)

StringMultiplier("Hello",5)

# So here we get to know that the Big O notation for above funciton is :

# O(1) + O(1) + O(1) + O(n) + O(n) + O(n) + O(n) = 1 + 1 + 1 + n + n + n + n = 3 + 4n

# BigO notation is --> 3 + 4n for above function
