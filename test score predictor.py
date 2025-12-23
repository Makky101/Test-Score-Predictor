"""
Test Score Predictor

This program uses linear regression to predict test scores based on study hours.
It allows users to input past test scores and hours studied, then predicts future scores.

Author: Makky101
"""

def myLinearRegressionModel(testScores, hoursStudied, scoreGoal, hours):
    """
    Performs linear regression to predict test scores and calculate required study hours.

    Args:
        testScores (list): List of past test scores
        hoursStudied (list): List of hours studied for each test
        scoreGoal (float): Desired score to achieve
        hours (float): Hours planning to study for next test

    Returns:
        list: [predicted_score, required_hours]
    """
    meanY = sum(testScores) / len(testScores)
    meanX = sum(hoursStudied) / len(hoursStudied)
    results = findMAndC(meanY,meanX,testScores,hoursStudied)
    gradient = results[0]
    yIntercept = results[1]
    errorRateSum = 0
    for num in range(len(hoursStudied)):
        predictedY = (gradient * hoursStudied[num]) + yIntercept
        yDiff = testScores[num] - predictedY
        squared = yDiff ** 2
        errorRateSum += squared
    
    expectedRes = (gradient * hours) + yIntercept
    hoursNeeded = (scoreGoal - yIntercept) / gradient

    return[expectedRes, hoursNeeded]

def findMAndC(meanY, meanX, y, x):
    """
    Calculates the slope (m) and y-intercept (c) for linear regression.

    Args:
        meanY (float): Mean of y values (test scores)
        meanX (float): Mean of x values (hours studied)
        y (list): List of y values
        x (list): List of x values

    Returns:
        list: [slope, y_intercept]
    """
    nominator = denominator = 0
    # Calculate numerator for slope
    for num in range(len(x)):
        xDiff = x[num] - meanX
        yDiff = y[num] - meanY
        product = xDiff * yDiff
        nominator += product

    # Calculate denominator for slope
    for num in range(len(x)):  # Fixed: should be len(x), not len(hoursStudied)
        xDiff = x[num] - meanX
        squared = (xDiff) ** 2
        denominator += squared

    m = nominator / denominator
    c = meanY - (m * meanX)

    return [m, c]

def is_number(s):
    """
    Checks if a string can be converted to a float.

    Args:
        s (str): String to check

    Returns:
        bool: True if convertible to float, False otherwise
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def has_number(inputString1, inputString2):
    """
    Checks if two strings are numbers.

    Args:
        inputString1 (str): First string
        inputString2 (str): Second string

    Returns:
        tuple: (bool, bool) for each string
    """
    return is_number(inputString1), is_number(inputString2)


def processResult(scoreGoal, hours):
    """
    Processes and displays the prediction results.

    Args:
        scoreGoal (int): Desired score
        hours (int): Planned study hours
    """
    results = myLinearRegressionModel(testScores,hoursStudied,scoreGoal,hours)
    print()
    print('=====RESULTS=====')
    print()
    print(f"Your score is roughly going to be '{round(results[0])}' after carefully reviewing the amount of time you are going to spend studying for this subject")
    print()
    print(f"To achieve your desired grade you would need to study for about '{round(results[1])} hours'")
    print('Good luck in your exam.')

print('============TEST SCORE PREDICTOR=============')
print()

# Global lists to store user input data
testScores = []
hoursStudied = []

# Main program loop for user interaction
while True:
    proceed = input('Do you wish to continue(y/n): ')
    if proceed.lower() == 'y' or proceed.lower() == 'yes':
        subject = input('Enter subject: ')
        if not subject:
            continue
        while True:
            comply = input('Proceed to enter test scores(y/n): ')
            if comply.lower() == 'y' or comply.lower() == 'yes':
                count = index = 0
                while True:
                    testScore = input(f'Enter test score {index + 1}: ')
                    hoursSpent = input("how many hours did you spend studying?: ")
                    isValid1, isValid2 = has_number(testScore,hoursSpent)
                    if isValid1 and isValid2:
                        testScores.append(float(testScore))
                        hoursStudied.append(float(hoursSpent))
                        count += 1
                        index += 1

                        if count >= 2:
                            advance = input('Do you wish to continue(y/n): ')
                            if advance.lower() == 'y' or advance.lower() == 'yes':
                                pass
                            else:
                                break
                    else:
                        print('Enter a valid number')
                        continue
                while True:
                    scoreGoal = input('what score do you want to achieve: ')
                    print()
                    hours = input('how many hours are you going to spend studying for the next test: ')

                    if scoreGoal.isdigit() and hours.isdigit():
                        processResult(float(scoreGoal),float(hours))
                        break
                    print('Please Enter valid numbers')
            elif comply.lower() == 'n' or comply.lower() == 'no':
                print('Have a good day!')
                break
            else: 
                print('Please enter a valid choice!')
    elif proceed.lower() == 'n' or proceed.lower() == 'no':
        print('have a good day!')
        break
    else:
        print('Please enter a valid choice!')
