import unittest

class Day2:
    def __init__(self, inMap: dict[str, int]) -> None:
        self.cubeMap = inMap

    def impossible(self, line: str):
        sp = line.split(":")
        points = sp[0].split(" ")[1]
        turn = sp[1].split(";")

        for t in turn:
            t = t.strip()

            for c in t.split(","):
                c = c.strip()
                colSlice = c.split(" ")
                count = colSlice[0]
                colour = colSlice[1]

                if self.cubeMap[colour] < int(count):
                    return 0

        return int(points)


class TestDay2(unittest.TestCase):
    def test_impossible(self):
        d2 = Day2({
            "red": 12,
            "green": 13,
            "blue": 14
            })

        input = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]

        self.assertEqual(d2.impossible(input[0]), 1)
        self.assertEqual(d2.impossible(input[1]), 2)
        self.assertEqual(d2.impossible(input[2]), 0)
        self.assertEqual(d2.impossible(input[3]), 0)
        self.assertEqual(d2.impossible(input[4]), 5)

    def test_input(self):
        d2 = Day2({
        "red": 12,
        "green": 13,
        "blue": 14
        })
        f = open("day-2/input.txt", "r")

        total = 0
        for line in f.readlines():
            total += d2.impossible(line)

        print(total)

        f.close()

if __name__ == "__main__":
    unittest.main()

