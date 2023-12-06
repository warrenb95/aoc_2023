from math import prod

class Day6:
    def __init__(self) -> None:
        pass

    def countWaysToWin(self, time: int, targetDistance: int) -> int:
        winningCount = 0
        for i in range(time):
            travelTime = time - i                                    
            if distance(i, travelTime) > targetDistance:
                winningCount += 1
            
        return winningCount

def distance(speed:int, time: int) -> int:
    return speed * time

if __name__ == "__main__":
    d6 = Day6()

    with open("day-6/input.txt") as f:
        input = f.readlines()
        
    # part 1
    times = [int(i.strip()) for i in input[0].split(":")[1].strip().split(" ") if i != ""]
    print(times)
    distances = [int(i.strip()) for i in input[1].split(":")[1].strip().split(" ") if i != ""]
    print(distances)

    print(prod([d6.countWaysToWin(times[i], distances[i]) for i in range(len(times))]))

    # part 2
    bigTime = int("".join([i for i in input[0].split(":")[1].strip() if i != " "]))
    print(bigTime)
    bigDistance = int("".join([i for i in input[1].split(":")[1].strip() if i != " "]))
    print(bigDistance)

    print(d6.countWaysToWin(bigTime, bigDistance))

