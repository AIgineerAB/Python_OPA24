# Exercise 1 - Python fundamentals

In this exercise sheet, you will get repetition of core Python and apply into exercises which are related to data processing.

> [!NOTE]
> These exercises covers lecture 4-6.

## 1. Cleaning string data

You would like to print out a short text of your introduction as below:

-----------------My introduction------------------ </br>
I am currently studying AI. My class is called OPA24.

However, you are given a raw data as a list: 

```["   i ", "AM ", "    CURRENTLY ", "TEACHING", "ai.   ", "mY", "   CLASS", "IS", "CALLED", "opa21."]```

Transform the raw data into the desired output as above with string methods. Here are string methods that you can use:

- ```strip()``` to remove extra whitespaces
- ```join()``` to combine elements of the list into one string
- ```swapcase()``` to swap lower and upper case letters
- ```center()``` to align a string with a specified character
- ```replace()``` to replace a specified phrase with another specified phrase

## 2. Hire IT employee data

In a company `Hire IT`, there are these employees.

| employeeID | name    | department | salary |
| ---------: | :------ | :--------- | ------ |
|          0 | Alice   | HR         | 31000  |
|          1 | Bob     | IT         | 41000  |
|          2 | Charlie | HR         | 28000  |

&nbsp; a) Create a list of dictionaries to represent this data, where each dictionary represents each row.

&nbsp; b) Extract the second record in this dataset.

&nbsp; c) Extract all rows from this dataset and print it in this format

```
Alice works in department HR and earns 31000.
Bob works in department IT and earns 41000.
Charlie works in department HR and earns 28000.
```

&nbsp; d) Find out the average salary in Hire IT.

&nbsp; e) Find out the average salary among the HR department in Hire IT.

&nbsp; f) Extract all records where the department is HR.

&nbsp; g) Find all unique departments in this list.

## 3. Gotta catch 'em all

&nbsp; a) Define a Pokemon class with attributes for name, type, level and hp(health points). All pokemon object should have 100 as hp when they are instantiated.

&nbsp; b) Implement `__str__()` method to display the Pokemon's details. Also implement a `__repr__()` method.

&nbsp; c) Design an attack method in the Pokemon class. This method takes another pokemon object as input and causes damage of another pokemon object's hp. An attacking pokemon can cause damage of double of its own level. 

&nbsp; d) Instantiate two pokemons and let one pokemon attacks another. Show the remaining hp of the damaged pokemon after the attack.


## 4. Analyze a log file 

It is common to log from different softwares and systems so that you always can go back to find out what happened, e.g. for debugging purposes. Under the data directory, there is a short log from a data engineering tool called data build tool (dbt), which is used for data transformations with SQL and jinja templating language. 

There seem to have been some errors during runs. You are tasked to read this log using Python and parse it to find some useful information for debugging. Print them out in a nicely formatted way. 

&nbsp; a) Read the log file. Find all rows that correspond to error. 

&nbsp; b) Each row is composed of *Timestamp*, *Log level*, *Thread* and *Detail message*. For each row, store the information of the error message into a dictionary with Timestamp, Log level, Thread and Detail message as keys. Put the dictionaries into a list. 

&nbsp; c) Write out the list of dictionaries into a file called `error.json`. 

## 5. Theory questions

These study questions are good for understanding the fundamentals of Python.

&nbsp; a) What is the difference between dictionary and lists?

&nbsp; b) What are postional arguments in functions?

&nbsp; c) What is the difference between using postional arguments and keyword arguments in functions?

&nbsp; d) What is the difference between a list and a tuple?

&nbsp; e) Explain the concept of Python's dynamic typing.

&nbsp; f) What is the purpose behind the `__repr__()` method in a class?

&nbsp; g) How does `__str__()` method differ from `__repr__()` method?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology              | explanation |
| ------------------------ | ----------- |
| dictionary               |             |
| list                     |             |
| list comprehension       |             |
| append                   |             |
| dictionary comprehension |             |
| argument                 |             |
| boolean                  |             |
| class                    |             |
| exception                |             |
| function                 |             |
| keyword arguments        |             |
| object                   |             |
| return statement         |             |
| tuple                    |             |
| type                     |             |
| self                     |             |
| instatiate               |             |
| iterating                |             |

