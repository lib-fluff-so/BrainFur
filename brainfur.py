import sys

def run_brainfur(code, input_data=''):
    memory = [0] * 30000
    pointer = 0
    input_index = 0
    code = code.split()
    i = 0
    while i < len(code):
        cmd = code[i]

        if cmd == 'dah':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif cmd == 'dee':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif cmd == 'tee-dah':
            pointer += 1
            if pointer >= len(memory):
                pointer = 0
        elif cmd == 'tee-dee':
            pointer -= 1
            if pointer < 0:
                pointer = len(memory) - 1
        elif cmd == 'kah-nah':
            sys.stdout.write(chr(memory[pointer]))
        elif cmd == 'tah-tah':
            if input_index < len(input_data):
                memory[pointer] = ord(input_data[input_index])
                input_index += 1
            else:
                memory[pointer] = 0
        elif cmd == 'ah-mah':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets > 0:
                    i += 1
                    if code[i] == 'ah-mah':
                        open_brackets += 1
                    elif code[i] == 'oo-bah':
                        open_brackets -= 1
        elif cmd == 'oo-bah':
            if memory[pointer] != 0:
                close_brackets = 1
                while close_brackets > 0:
                    i -= 1
                    if code[i] == 'oo-bah':
                        close_brackets += 1
                    elif code[i] == 'ah-mah':
                        close_brackets -= 1
        # 'tee-toh' and others: no-op
        i += 1