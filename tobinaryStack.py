from Stack import Stack
'''Here we will find the binary of any integer value
    So in order to do that what we need is
    Ex:21
    if we divide 21 by 2(21//2=10)
    we get:10
    so      remainder is 1 
    to get that we will use % operator
    so that :21%2=1
    Now we the next value which is 10 
    and again 10//2=5
    10%2=   rem is 0
    so 5//2=2
    5%2     rem=1
    2//2=1
    2%2=0
    1//2=1
    1%2     rem=1
    so finally we have from to bottom(10101)
    and now invert it so it would be 10101
    Here what we will do is that when we get any rem we will add it to stack(Last in first out) so that in the end will pop it to get the binary in correct order
    
    So if we want to convert from int oct
    Decimal to octal(base 8):
    decnum%8=rem then divide answer by the same
    decnum/8=quot same for result till 0

Note:Add other converter
    
    '''
def dectooctal(integer):
    s=Stack()
    nextvalue=integer
    while nextvalue>0:
      rem=nextvalue%8
      s.push(rem)
      print(s.peek())
      nextvalue=nextvalue/8
    answer=""  
    while not s.isEmpty():
        answer+=str(s.pop())
    return answer    

def dectobin(integer):
    s=Stack()
    nextint=integer
    while nextint>0:
        rem=nextint%2
        s.push(rem)
        nextint=nextint//2
    binary=""
    for i in range(s.size()):#we can do this with better option as while not s.isEmpty
        binary+=str(s.pop())
    return binary    
print(dectobin(233))
print(dectooctal(1792),"Nothing!")
