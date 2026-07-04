# Mini Project 3: Unit Converter

## Objective

The objective of this project is to practice Python functions by creating a Unit Converter. The program allows users to convert values between different units of length, temperature, and weight using separate functions.

## Concepts Practiced

This project helped in understanding and practicing:

* Functions
* Function Parameters
* Function Arguments
* Return Values
* Function Calls
* User Input
* Conditional Statements (if, elif, else)
* Code Reusability
* Formatted Output using f-strings

## Conversions Included

The program supports the following conversions:

1. Kilometers to Miles
2. Celsius to Fahrenheit
3. Kilograms to Pounds
4. Miles to Kilometers
5. Fahrenheit to Celsius
6. Pounds to Kilograms

## Functions Used

### 1. menu()

Displays all available conversion options to the user.

### 2. get_choice()

Takes the user's menu choice and returns it to the main program.

### 3. km_to_miles(km)

Converts kilometers into miles.

Formula:

Miles = Kilometers × 0.621371

### 4. celsius_to_fahrenheit(c)

Converts Celsius into Fahrenheit.

Formula:

Fahrenheit = (Celsius × 9/5) + 32

### 5. kg_to_pounds(kg)

Converts kilograms into pounds.

Formula:

Pounds = Kilograms × 2.20462

### 6. miles_to_km(miles)

Converts miles into kilometers.

Formula:

Kilometers = Miles ÷ 0.621371

### 7. fah_to_cel(f)

Converts Fahrenheit into Celsius.

Formula:

Celsius = (Fahrenheit − 32) × 5/9

### 8. pounds_to_kg(pounds)

Converts pounds into kilograms.

Formula:

Kilograms = Pounds ÷ 2.20462

### 9. display_result(result, unit)

Displays the converted value along with its unit.

## Program Flow

Display Menu

↓

Get User Choice

↓

Take Input Value

↓

Call Appropriate Conversion Function

↓

Return Converted Value

↓

Display Result

## Sample Output

----- Unit Converter -----

1. Kilometers to Miles
2. Celsius to Fahrenheit
3. Kilograms to Pounds
4. Miles to Kilometers
5. Fahrenheit to Celsius
6. Pounds to Kilograms

Enter your choice: 1

Enter Kilometers: 10

Result: 6.21 Miles

## Learning Outcome

Through this project, I learned how to divide a problem into multiple functions, pass values through parameters, return calculated results, and build a menu-based application using Python. I also learned how functions work together to solve a complete problem while keeping the code organized and reusable.
