def calculateAbsolute():
    in_num  = input("Enter a number: ")

    if int(in_num) > 21:
        diff = abs((int(in_num) - 21) * 2)
    else:
        diff = abs(int(in_num) - 21)

    print ("Result:", diff)

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
