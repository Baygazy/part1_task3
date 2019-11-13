#Make sure to un-comment the function line below when you are
#done.
#Remember to name your function is_even
# WRITE YOUR CODE HERE...
def is_odd(bgz): return bgz % 2 == 1   #если при делении остаток равен 1 то вернуть True
#DO NOT remove lines below here,
#this is designed to test your code.
def test_is_odd():
 assert is_odd(2) == False
 assert is_odd(3) == True
 assert is_odd(8) == False
 assert is_odd(100) == False
 assert is_odd(101) == True
 print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_is_odd()