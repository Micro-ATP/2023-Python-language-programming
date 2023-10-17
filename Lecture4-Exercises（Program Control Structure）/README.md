# 题目（Exercises）

## 1. Judgment conditions and combinations

Question: Get the month input by the user and output the number of days in the month (leaving no consideration for leap years)

Example: Input: 2, Output: 28

Tip: Take advantage of multi-branch structures

## 2. Multiple inputs and outputs

Topic: Solving the Problem of Chicken and Rabbit in the Same Cage

Enter the total number of chickens and rabbits and the number of legs to find out how many chickens and how many rabbits there are.

Tip: Num = ji + tu；LegNum = 2* ji + 4*tu  tu = (LegNum – Num *2) / 2

If tu is not an integer, it means the data is incorrect

## 3. Determine what day of the year today is

Tip: Reference the localtime() function in the time library to obtain the current time; distinguish whether this year is a leap year;
Accumulate the number of days in the previous n-1 months, and add it to the current month

## 4. The user inputs n and finds the factorial of n.

Example: input: 10, output: 3628800; input: 15, output: 130767436800

Tip: Use a for loop to calculate n! =1*2*3*…*n

## 5. Question: Give the user three opportunities to enter the username and password. The requirements are as follows:

For example, enter the username ‘Kate’ in the first line, enter the password ‘666666’ in the second line, and output ‘Login successful! ’, exit the program; when a total of 3 incorrect usernames or passwords are entered, it will output “Incorrect usernames or passwords 3 times! Exit the program.”.
