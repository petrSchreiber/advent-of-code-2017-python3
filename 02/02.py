def checksum(line):
    values = [int(num) for num in line.split('\t')]

    return max(values) - min(values)


with open('data.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    total += checksum(line)

print(total)
