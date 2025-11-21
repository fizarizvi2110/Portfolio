# Homework 10 Programming
---------------------------------

Please remember that to submit the assignment you will need to the Education drop down menu and select  assignment complete. Once you have marked the assignment as complete you will not be able to edit it again. 

Make sure to format and comment your code carefully and correctly based on the style we've been using in class.

## Problem 1 - 47 Points

For this problem you will write a java program called *Fail2Ban*.  This program will take two command line arguments: the name of a single log file (such as the one attached to this assignment) and the name of an output file.

You will read each line of the program in, extract the IP address from the line and determine whether the line is a failed login attempt or valid login attempt.

Look through the *logs_processed.txt* file.  It follows a fairly clear format and indicates "Invalid" whenever a bad attempt is made.  Once you identify the invalid line, the IP address should always be in the same position.  Make use of String's split method to parse the lines.

Keep track of the number of times a particular IP address fails to login.  

Your program should then open the output file and print a  list of IP addresses to that fail 3 or more times.

A sample command line execution of this file might look like this:

```$ java Fail2Ban logs_processed.txt output.txt```

The list of IP addresses that have failed 3 or more times should appear in the output.txt file.

You are provided with an empty *Fail2Ban.java* file to fill in your solution to the assignment.

## Problem 2 - 3 points

In addition to the source files for your programs include a single text file in your codio workspace named readMe.txt with an explanation of what you did for each programming problem. That is, write in plain English, instructions for using your software, explanations for how and why you chose to design your code the way you did. The readMe.txt file is also an opportunity for you to get partial credit when certain requirements of the assignment are not met.
