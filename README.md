# Neuro - Computation First Project
### The main purpose of this project is to get to know the Adaline algorithm and the Back Propagation algorithm.
First, we built the functions to create data sets and test sets to work with. The base of each functiom is as follows: </br>
We choose x, y <= 100 randomly. The data is all data points <x,y> where x is of the form m/100, where m is an integer between -1000 and +1000, and y is of the form n/100, where n is an integer between -1000 and +1000.

Then we worked on Parts A and B. </br>
In this part we implemented the Adaline learning algorithm and showed how it generalizes to develop a decision that works on all the set. </br>
<b> Part A </b> </br>
In this part we chose every point such that when it's 'y' value is grater than 1 the 'value' of this point is '1' else its '-1'. </br>
For example: </br>
![image](https://user-images.githubusercontent.com/78349342/168127025-0e279552-d353-4ff8-8617-fa55db465ffa.png) </br>
Then we trained the training set we built on the Adaline algorithm we implemented.</br>
Here are some of the results we got: </br>
![image](https://user-images.githubusercontent.com/78349342/168130371-4e4caad5-f40c-4d12-a9c1-61bce47e1f90.png)</br>
As we can see the accuracy score we got is 99.1% </br>

<b> Part B </b> </br>
In this part we chose every point such that <x,y> has value '1' only if 4 <= x^2 + y^2 <= 9. </br>
For example: </br>
![image](https://user-images.githubusercontent.com/78349342/168128623-17fe0841-3f71-4095-8bf9-97bce9c37749.png) </br>

Obviously most of the points got the value of '-1', because the range we gave for the radius was small, so most of the points were not in it. For that reason, in the result we will see that the algorithm classified the points pretty good although the Adaline algorithm works for linearly separable data sets: </br>

![image](https://user-images.githubusercontent.com/78349342/168130296-c3817d53-a8f8-4481-b846-94d149cf849b.png) </br>
We tried a bigger range, then we got "better" results: </br>
![image](https://user-images.githubusercontent.com/78349342/168130163-f22a5d63-2fd0-474f-be61-35c7b97bf1f8.png) </br>





