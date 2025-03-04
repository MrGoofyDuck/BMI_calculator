# BMI Calculator

## Objective
The objective of this project is to create a BMI Calculator application using PyQt that allows users to calculate their Body Mass Index (BMI) and provides information on their BMI status according to the Department of Health and Human Services/National Institutes of Health guidelines.

## User Interface
The PyQt user interface for the BMI calculator includes the following components:
- QLabel and QLineEdit for weight and height input.
- A "Calculate BMI" button.
- A QLabel to display the BMI result.
- BMI status display (Underweight, Normal, Overweight, Obese) based on the calculated BMI.

## BMI Calculation
The BMI calculation is based on user input. The formula for calculating BMI is:


\[ \text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2} \]



## BMI Status
The user's BMI status is determined based on the calculated BMI using the provided guidelines:
- **Underweight:** Less than 18.5
- **Normal:** Between 18.5 and 25
- **Overweight:** Between 25 and 30
- **Obese:** 30 or greater

## Menu
A menu bar is implemented at the top of the application with the following options:
- **File:**
  - **Exit:** Closes the application.
  - **Clear:** Clears the input fields.
- **Help:**
  - Displays information about how to use the BMI calculator.




