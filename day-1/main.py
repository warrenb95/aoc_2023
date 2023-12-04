def getNumberCalibration(calibration):
    print(calibration)

    vString = ""
    i = 0
    while i < len(calibration):
        if calibration[i].isdigit():
            vString = calibration[i]
            break
        i += 1

    j = len(calibration)-1
    while j >= 0:
        if calibration[j].isdigit():
            vString += calibration[j]
            break
        j-= 1


    print(vString)
    return vString

if __name__ == "__main__":
    result =0
    f = open("input.txt", "r")
    for line in f.readlines():
        calibration = getNumberCalibration(line)
        result += int(calibration)

    print(result)
