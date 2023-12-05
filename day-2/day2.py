class Day2:
    def impossible(self, line: str):
        sp = line.split(":")
        print(sp)

if __name__ == "__main__":
    d2 = Day2()

    f = open("input.txt", "r")
    for line in f:
        d2.impossible(line)
        break
