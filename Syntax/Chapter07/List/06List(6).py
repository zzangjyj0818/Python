scores = [88, 100, 96, 43, 65, 78]

max_val = max(scores)
min_val = min(scores)
sum_val = sum(scores)
avg_val = sum_val / len(scores)
print(max_val, min_val, sum_val, int(avg_val))

sum_value = 0

for score in scores:
    sum_value += score

print(sum_value)