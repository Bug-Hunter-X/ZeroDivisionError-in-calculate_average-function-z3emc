# Python Bug: ZeroDivisionError in Average Calculation

This repository demonstrates a common bug in Python: a `ZeroDivisionError` that occurs when calculating the average of an empty list.  The `calculate_average` function lacks proper error handling for this edge case.  The solution shows how to gracefully handle empty lists to prevent the error.

## Bug Description:

The `calculate_average` function fails when it receives an empty list as input, resulting in a `ZeroDivisionError` due to division by zero. 

## Solution:

The solution adds a check to see if the input list is empty. If it's empty, the function returns 0, avoiding the error.