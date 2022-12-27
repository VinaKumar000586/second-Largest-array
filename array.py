def secondlargest(arr,n):
    if n==0:
        return -1
    largest =0
    second_largest = -1
    for i in arr:
        largest=max(i,largest)
    for i in arr:
        if i < largest and i>second_largest:
         second_largest = max(i,second_largest)
    return second_largest

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ans = secondlargest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends