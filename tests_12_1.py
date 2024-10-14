from runner import Runner as rn
import unittest


def repeat(numb_repeat, *funcs):
    for func in funcs:
        for i in range(numb_repeat):
            func()


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        unit_1 = rn('Mr.Fox')
        repeat(10, unit_1.walk)
        self.assertEqual(unit_1.distance, 50)

    def test_run(self):
        unit_2 = rn('Mr.Fox')
        repeat(10, unit_2.run)
        self.assertEqual(unit_2.distance, 100)

    def test_challenge(self):
        unit_1 = rn('Mr.Fox')
        unit_2 = rn('lupus')
        repeat(10, unit_1.walk, unit_2.run)
        self.assertNotEqual(unit_1.distance, unit_2.distance)


if __name__ == '__main__':
    unittest.main
