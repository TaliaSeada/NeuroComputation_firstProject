# Neuro - Computation First Project
### The main purpose of this project is to get to know the Adaline algorithm and the Back Propagation algorithm.
<b> Adaline - https://en.wikipedia.org/wiki/ADALINE </br>
Back Propagation - https://en.wikipedia.org/wiki/Backpropagation </b> </br>
__In this project we built the algorithms, tested them and improved them in the process.__ </br>

_Content_:
* Building the data
* Parts A and B:
  1. Part A
  2. Part B
* Parts C and D:
  1. Part C
  2. Part D

## _Building the data_:
First, we built the functions to create data sets and test sets to work with. The base of each functiom is as follows: </br>
We choose x, y <= 100 randomly. The data is all data points <x,y> where x is of the form m/100, where m is an integer between -1000 and +1000, and y is of the form n/100, where n is an integer between -1000 and +1000.

## _Parts A and B_:
In this part of the project we implemented the Adaline learning algorithm and showed how it generalizes to develop a decision that works on all the set. </br>
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

## _Parts C and D_:
In this part of the project we implemented the Back-propagation learning algorithm and showed how it generalizes to develop a decision that works on all the set. </br>
<b> Part C </b> </br>
In this part we used the same data sets we created in part A and B. Then we trained the training set on the  Back-propagation algorithm we implemented.</br>
Here are some of the results we got: </br>
__linearly separable data set:__ </br>
![image](https://user-images.githubusercontent.com/78349342/168133924-b737e38a-11bd-491b-be9d-ff1f41a51527.png) </br>
__nonlinearly separable data sets:__ </br>
![image](https://user-images.githubusercontent.com/78349342/168133959-f8904080-4c05-443f-b547-433c48df1a56.png) </br>
![image](https://user-images.githubusercontent.com/78349342/168133699-28d6cae6-4597-4b62-8401-ade2471c37a5.png) </br>

For the linearly separable data set we got nearly the same result as the Adaline algorithm gave us. Also for the set with the small range of radii, but for the bigger range we got way better results than with the Adaline algorithm.</br>
In this part we looked in to each neuron and saw how it "sees the data, for example of the first data set: </br>
![image](https://user-images.githubusercontent.com/78349342/168134422-6d2c816e-855a-4b47-844a-7e19f6133cfa.png) </br>
And from the second: </br>
![image](https://user-images.githubusercontent.com/78349342/168134692-2ed358cd-0608-4085-ba5b-a092422135dc.png) </br>
 We can see the nonlinear shapes the neurons "see". </br>
 
 <b> Part D </b> </br>
In this part we used the traind neurons from the next to last level of Part C as input and only an Adaline for the output. We gave the Adaline the output of the neurons from Part C in the level below the output, and trained only the Adaline. </br>
Here are some of the results we got: </br>
__linearly separable data set:__ </br>
![image](https://user-images.githubusercontent.com/78349342/168136539-0d3fcfef-121c-4d35-bc6c-1c7f5c122fc4.png) </br>
__nonlinearly separable data sets:__ </br>
![image](https://user-images.githubusercontent.com/78349342/168136617-ec9eabb8-65c2-4959-a850-d50fa79c9e8a.png) </br>
![image](https://user-images.githubusercontent.com/78349342/168136753-cfe9474c-d9fa-4325-a083-d975748d4c37.png) </br>

For the linearly separable data set we got nearly the same result as the Back-propagation algorithm gave us. For the set with the small range of radii we didnt got any better result, also for the bigger range we didnt got some better results. </br>

In this part we looked in to each neuron of the how it "sees" the data, for example of the second set - which we were more interested in: </br>
![image](https://user-images.githubusercontent.com/78349342/168137975-bbcdb07c-444a-411f-86ca-906a66997121.png) </br>

We can see how they actuall "see" a circle!






