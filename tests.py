import unittest
from io import StringIO
import sys
import brainfur


def run_prog(code, inp=''):
    old_stdout, old_stdin = sys.stdout, sys.stdin
    sys.stdout, sys.stdin = StringIO(), StringIO(inp)
    brainfur.run_brainfur(code, inp)
    output = sys.stdout.getvalue()
    sys.stdout, sys.stdin = old_stdout, old_stdin
    return output


class TestFurbishBF(unittest.TestCase):
    def test_increment(self):
        code = "tee-toh dah kah-nah"
        self.assertEqual(run_prog(code), chr(1))

    def test_decrement(self):
        code = "tee-toh dah dah dee kah-nah"
        self.assertEqual(run_prog(code), chr(1))

    def test_pointer_move(self):
        code = "tee-toh dah tee-dah dah tee-dee kah-nah"
        self.assertEqual(run_prog(code), chr(1))

    def test_input(self):
        code = "tee-toh tah-tah kah-nah"
        self.assertEqual(run_prog(code, "Z"), "Z")

    def test_loop_echo(self):
        # Echo until zero terminator
        code = "tee-toh tah-tah ah-mah kah-nah dee tah-tah oo-bah"
        self.assertEqual(run_prog(code, "A\x00"), "A")

    def test_repeated_loop(self):
        # Print 2 then 1
        code = "tee-toh dah dah ah-mah kah-nah dee oo-bah"
        self.assertEqual(run_prog(code), chr(2) + chr(1))

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
        self.assertEqual(run_prog(code), chr(4))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)