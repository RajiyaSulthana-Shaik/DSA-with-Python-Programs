# Search an element in an array (LINEAR SEARCH)
def linears(arr, num):
    x = 0;
    for i in range(len(arr)):
        if (arr[i] == num):
            return i;
    return -1;
    
arr = [10, 5, 3,3, 7,3,0,5,7,3]
res5 = linears(arr, 5);
print(res5);

# count occurance of given element
def Countelement(arr, num):
    x = 0;
    for i in range(len(arr)):
        if (arr[i] == num):
            x+=1; 
    return x; 
    
arr = [10, 5, 3,3,5, 7,3,0,5,7,3]
res5 = Countelement(arr, 5);
print(res5);

# Practice patterns
def P1(num):
    for i in range(num):
        for j in range(num):
            print("* ", end="")
        print()
res4 = P1(4);
print(res4)