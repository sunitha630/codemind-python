from collections import Counter
n=int(input())
numbers = list(map(int,input().split()))
number_counts = Counter(numbers)
pair_count = 0
for count in number_counts.values():
    pair_count += count // 2
print(pair_count)