import main

def test_getCalibration():
    input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

    assert main.getNumberCalibration(input[0]) == "12", "Calibration should be 12"
    assert main.getNumberCalibration(input[1]) == "38", "Calibration should be 38"
    assert main.getNumberCalibration(input[2]) == "15", "Calibration should be 15"
    assert main.getNumberCalibration(input[3]) == "77", "Calibration should be 77"
