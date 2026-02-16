def largestele(arr):
    if not arr:
        return "no element in arr";
    largest = arr[0];
    for i in arr[1:]:
        if (i > largest):
            largest = i;
    return largest;
    
arr = [5];
res1 = largestele(arr);
print(res1)


def secondlarge(arr):
    if len(arr)<2:
        return "no second large ele";
    # if arr[0] > arr[1]:
    #     large = arr[0];
    #     second = arr[1];
    # else:
    #     large = arr[1];
    #     second = arr[0];
    large = second = float('-inf')
    
    for i in arr:
        if i > large:
            second = large;
            large = i;
        elif i > second and i != large:
            second = i;
            
    if second == float('-inf'):
        return "no second large ele";
        
    return second;
    
arr = [10,11,16,9,8000];
res2 = secondlarge(arr);
print(res2);


def sortedarr(arr):
    if len(arr)<=1:
        return "array already sorted";
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i+1]):
            return " false";
    return "true";
    
arr = [7,8,0];  
res3 = sortedarr(arr);
print(res3)