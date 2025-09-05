Find All Duplicates
Write a function (in python) or method (in Java) that accepts a list of integers and returns a list of only those integers that appear more than once.
Lab 3 work
-The first approach to solving this problem involves creating a function that uses nested loops and which compares the element in the array with the one next to it to see 
if they are the same. The index of the inner loop must start one later than the outer to avoid duplicates.
-The second approach involves using a HashMap or dictionary. Loop through the input array, and add each element to the Hashmap/set one by one.
Since a HashMap can contain no duplicates, you will know which elements in the input are duplicates simply by seeing which ones can't be inserted into the set twice.
