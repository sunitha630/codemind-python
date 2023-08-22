def count_unique_elements(arr):
    count = 0
    odd_seen = set()
    for element in arr:
            odd_seen.add(element)
    count = sum(odd_seen)
    return count
n=int(input())
l=list(map(int,input().split()))
count=count_unique_elements(l)
print(count)
