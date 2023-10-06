# Decorators
## Project Description

The primary goal of this project is to capture and save the results of functions, along with their execution times, to a database. This functionality is achieved through decorators that can be applied to any Python function, allowing users to easily track and store the output and performance of their code.

### Modules

#### 1. main.py
   
This module serves as the entry point for running the project and demonstrating its functionality.

#### 2. functionsExamples.py
   
This module contains example functions that can be used to test the functionality of the decorators (you could use any function that you wnat to). Here's what example functions do:

  - lottery(amount, totalAmount): This function simulates drawing numbers from a pool of numbers. It takes two arguments: the number of numbers to draw (amount) and the total number of available numbers (totalAmount). The function randomly selects and returns amount unique numbers from the range 1 to totalAmount.
  
  - func1(a): This is a simple example function. It takes one argument a and returns a raised to the power of a.
  
  - func2(a, b): This is another simple function that takes two arguments a and b and returns the sum of a + b and the value of a.

#### 3. savingReturnsOfDifferentFunc.py

This module contains decorators and helper functions for measuring the execution time of functions and saving their results to a database. Here are the main objectives and operations in this module:

  - decoratorTime(func3): This decorator measures the execution time of the function it decorates (func3). The func3 function is wrapped inside the decorator, and the time it takes to execute is measured using the time module.
  
  - decoratorSavingResults(func, dict, con, nameTab, curs): This decorator saves the results of function calls to a dictionary (dict) and an SQLite database (con, nameTab, curs). The decorator checks whether the results and execution times of the function are already stored in the dictionary and updates them if they exist.

These modules collectively enable easy measurement of function execution times and storing results in a database, allowing for performance analysis and monitoring of Python functions in projects.


### Usage
To test your own Python functions using the functionality provided by this project, follow these steps:

#### 1. Prepare Your Functions
Before testing the project with your own functions, make sure you have defined the functions you want to test in a separate Python file.

Subsequent modifications must be made in the main module.
#### 2. Import Modules

In your own Python script, import the necessary modules from the project:

from savingReturnsOfDifferentFunc import decoratorTime, decoratorSavingResults, openingDb, creatingTable
from your_own_functions_module import your_function1, your_function2, ...

Replace your_own_functions_module with the name of the Python file where your own functions are defined. Also, replace your_function1, your_function2, etc., with the names of your own functions.

#### 3. Initialize Database and Table

Initialize a database connection and create a table to store the results of your functions:

cur, con = openingDb('yourDatabase')
creatingTable('functionsResults', cur, con)

Replace 'yourDatabase' with the desired name for your SQLite database. The table 'functionsResults' will store the results.

#### 4. Decorate Your Functions

Decorate your own functions with the decoratorTime and decoratorSavingResults decorators. For example:

decorated_function1 = decoratorSavingResults(decoratorTime(your_function1), allData, con, 'functionsResults', cur)
decorated_function2 = decoratorSavingResults(decoratorTime(your_function2), allData, con, 'functionsResults', cur)

Replace your_function1, your_function2, etc., with your own function names, and assign the decorated versions to new variables. allData is the dictionary where the results will be stored.

#### 5. Call Decorated Functions

Call your decorated functions as needed within your script:

result1 = decorated_function1(arg1, arg2, ...)
result2 = decorated_function2(arg1, arg2, ...)

Replace arg1, arg2, etc., with the appropriate arguments for your functions.
