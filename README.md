### Test Score Predictor

A Python program that uses linear regression to predict test scores based on study hours. It allows users to input their past test scores and corresponding study hours, then predicts future test scores and calculates the required study hours to achieve a desired grade.

## Features

- Interactive user interface for data input
- Linear regression-based score prediction
- Calculation of required study hours for target scores
- Input validation for numeric values
- Support for multiple subjects

## Requirements

- Python 3.x
- Install dependencies: `pip install -r requirements.txt`

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Download or clone the repository containing `test score predictor.py`.
3. Open a terminal and navigate to the directory containing the file.
4. Run the program using:
   ```
   python "test score predictor.py"
   ```

## Usage

1. Start the program by running the script.
2. Choose to continue or exit.
3. Enter the subject name.
4. Input your past test scores and corresponding study hours (at least 2 data points required).
5. Specify your desired score goal and planned study hours for the next test.
6. View the predictions and required study hours.

## Example

```
============TEST SCORE PREDICTOR=============

Do you wish to continue(y/n): y
Enter subject: Math
Proceed to enter test scores(y/n): y
Enter test score 1: 85
how many hours did you spend studying?: 10
Enter test score 2: 90
how many hours did you spend studying?: 12
Do you wish to continue(y/n): n
what score do you want to achieve: 95

how many hours are you going to spend studying for the next test: 15
=====RESULTS=====

Your score is roughly going to be '93' after carefully reviewing the amount of time you are going to spend studying for this subject

To achieve your desired grade you would need to study for about '16' hours
Good luck in your exam.
```

## How It Works

The program implements simple linear regression where:

- X-axis: Hours studied
- Y-axis: Test scores

It calculates the best-fit line and uses it to make predictions.

## Limitations

- Assumes a linear relationship between study hours and test scores
- Requires at least 2 data points for regression
- Does not account for other factors affecting test performance

## Sample Data

See `sample_data.txt` for example input data that can be used to test the Test Score Predictor.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork and improve the program. Suggestions for enhancements are welcome.

