def get_steps(instruction, element_modification=lambda x: 1):
    instruction_copy = instruction[:]
    jump_count = 0
    index = 0
    while -1 < index < len(instruction_copy):
        value = instruction_copy[index]
        instruction_copy[index] += element_modification(value)
        index += value
        jump_count += 1

    return jump_count


with open('data.txt', 'r') as f:
    instruction = [int(v) for v in f.read().splitlines()]

print(get_steps(instruction))
print(get_steps(instruction, lambda x: 1 if x < 3 else -1))
