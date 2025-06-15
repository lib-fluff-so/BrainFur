import unittest
from io import StringIO
import sys

def run_furbish_bf(code, input_data=''):
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

class TestFurbishBF(unittest.TestCase):
    def run_prog(self, code, inp=''):
        old_stdout, old_stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(inp)
        run_furbish_bf(code, inp)
        output = sys.stdout.getvalue()
        sys.stdout, sys.stdin = old_stdout, old_stdin
        return output

    def test_increment(self):
        code = "tee-toh dah kah-nah"
        self.assertEqual(self.run_prog(code), chr(1))

    def test_decrement(self):
        code = "tee-toh dah dah dee kah-nah"
        self.assertEqual(self.run_prog(code), chr(1))

    def test_pointer_move(self):
        code = "tee-toh dah tee-dah dah tee-dee kah-nah"
        self.assertEqual(self.run_prog(code), chr(1))

    def test_input(self):
        code = "tee-toh tah-tah kah-nah"
        self.assertEqual(self.run_prog(code, "Z"), "Z")

    def test_loop_echo(self):
        # Echo until zero terminator
        code = "tee-toh tah-tah ah-mah kah-nah dee tah-tah oo-bah"
        self.assertEqual(self.run_prog(code, "A\x00"), "A")

    def test_repeated_loop(self):
        # Print 2 then 1
        code = "tee-toh dah dah ah-mah kah-nah dee oo-bah"
        self.assertEqual(self.run_prog(code), chr(2) + chr(1))

    def test_nested_loop(self):
        code = (
            "tee-toh "  # start
            "dah dah "  # cell[0] = 2
            "ah-mah "  # while cell[0] != 0
            "tee-dah "  # move → cell[1]
            "dah dah "  # cell[1] += 2
            "ah-mah "  # while cell[1] != 0
            "tee-dah "  # move → cell[2]
            "dah "  # cell[2] += 1
            "tee-dee "  # move ← cell[1]
            "dee "  # cell[1] -= 1
            "oo-bah "  # end inner loop
            "tee-dee "  # move ← cell[0]
            "dee "  # cell[0] -= 1
            "oo-bah "  # end outer loop
            "tee-dah tee-dah "  # ←← move two cells right to cell[2]
            "kah-nah"  # output cell[2], should be chr(4)
        )
        self.assertEqual(self.run_prog(code), chr(4))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)