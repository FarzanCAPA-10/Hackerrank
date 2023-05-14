def compare(a, b):
    x = 0
    y = 0
    for i in range(0 , len(a)):
        if a[i] > b [i]:
            x = x + 1
        elif a[i] < b[i]:
            y = y + 1
        else:
            continue
        
    return [x,y]



a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

print(compare(a,b))