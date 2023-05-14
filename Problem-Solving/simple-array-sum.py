def simpleArraySum(ar):
    s = 0
    for i in ar:
        s = s + i 
    return s
    """other logic direct call sum function 
    
    
    return sum(ar)
    """

ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))

