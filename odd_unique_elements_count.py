def count_odd_unique_elements(arr):
    odd_count = 0
    odd_seen = set()
    for element in arr:
        if element % 2 != 0:
            odd_seen.add(element)
    odd_count = len(odd_seen)
    return odd_count
n=int(input())
l=list(map(int,input().split()))
count=count_odd_unique_elements(l)
print(count)