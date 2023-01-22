max_quotient = 0

for i in range(100, 1000):
    digits = [int(d) for d in str(i)]
    if len(set(digits)) == 3:
        quotient = i / sum(digits)
        max_quotient = max(max_quotient, quotient)

print(max_quotient)
