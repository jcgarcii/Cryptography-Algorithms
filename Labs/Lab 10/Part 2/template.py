# ISU Lottory generates two lottery numbers every other day.
# The formula for generating these random numbers has been kept secret until
# a curious cpre231 student hacked into their database and leaked the
# code they used to generate their lottery numbers
import random


#Generates a winning lottery number for today and tomorrow
def generateLottery(dateOfGeneration, timeInSeconds):
    # timeInSeconds = [0, 1, ..., 86400]
    # dateOfGeneration = MM/DD/YYYY
    lotteryNumbers = []

    # Add the date and the seconds to get the seed
    random.seed(int(dateOfGeneration.replace("/","")) + timeInSeconds)

    # Generate lottery number for the current day
    randomNumbers = []
    for i in range(10):
        randomNumbers.append(str(random.randrange(0, 10)))
    lotteryNumbers.append('-'.join(randomNumbers))

    # Generate lottery number for the next day
    randomNumbers = []
    for i in range(10):
        randomNumbers.append(str(random.randrange(0, 10)))
    lotteryNumbers.append('-'.join(randomNumbers))

    #Return an array of two values
    # lotteryNumbers[0] = Today's lottery number
    # lotteryNumbers[1] = Tomorrow's lottery number
    return lotteryNumbers


def main():
    res = []
    date = str(input('Enter a Date [MM/DD/YYYY] Format\n>> '))
    toMatch = str(input('Enter the string of numbers you would like to match\n>> '))
    seconds = 0

    res = generateLottery(date, seconds)

    for i in range(0, 86400):
        if(str(res[0]) == toMatch):
            print('---- Matched! ----')
            break
        
        else: 
            seconds +=1
            res = generateLottery(date, seconds)

    print('Here are the numbers for '+ date +': ', res[0]) 
    print('Here are the day after the input date numbers: ', res[1])

if __name__ == '__main__':
    main()
