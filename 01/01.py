def get_captcha(content, offset):
    total = 0
    for i in range(0, len(content)):
        index_b = (i + offset) % len(content)
        if content[i] == content[index_b]:
            total += int(content[i])

    return total


with open('data.txt', 'r') as f:
    content = f.read()

print(get_captcha(content, 1))
print(get_captcha(content, len(content)//2))
