n = int(input())
zero_c = one_c = 0

for _ in range(n):
    if int(input()):
        one_c += 1
    else:
        zero_c += 1

print("Junhee is cute!" if one_c > zero_c else "Junhee is not cute!")