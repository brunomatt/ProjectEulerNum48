# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

sum = 0

for i in range(1, 1001):
    sum += i**i

num_str = str(sum)

answer = num_str[-10:]

print(answer)