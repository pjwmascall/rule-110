def rule(current_pattern):
    if current_pattern == [1,1,1]:
        return 0
    if current_pattern == [1,1,0]:
        return 1
    if current_pattern == [1,0,1]:
        return 1
    if current_pattern == [1,0,0]:
        return 0
    if current_pattern == [0,1,1]:
        return 1
    if current_pattern == [0,1,0]:
        return 1
    if current_pattern == [0,0,1]:
        return 1
    if current_pattern == [0,0,0]:
        return 0

def print_pattern(generation, sequence):
    pattern = ''
    for number in sequence:
        if number == 1:
            pattern += '*'
        if number == 0:
            pattern += ' '
    print(f'Generation {generation}: {pattern}')

def cellular_automaton(sequence, number_of_generations):
    for generation in range(number_of_generations):
        sequence_with_wraparound = [sequence[-1]] + sequence + [sequence[0]]
        sequence = []
        for i in range(1, len(sequence_with_wraparound) - 1):
            current_triplet_in_sequence = [sequence_with_wraparound[i - 1]] + [sequence_with_wraparound[i]] + [sequence_with_wraparound[i + 1]]
            new_state_for_center_cell = rule(current_triplet_in_sequence)
            sequence.append(new_state_for_center_cell)
        print_pattern(generation, sequence)

def sequence_generator(length_of_sequence):
    from random import uniform
    return [round(uniform(0,1)) for _ in range(length_of_sequence)]

input_sequence = sequence_generator(10)

cellular_automaton(input_sequence, 100)