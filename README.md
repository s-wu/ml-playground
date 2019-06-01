# ml-playground

This is an exercise in practical machine learning. A pseudorandom number generator outputs one million bits (0s and 1s). However, 2000 of those bits are randomly selected and their values are hidden. We are given the result (one million digits, of which the majority are 0s and 1s and 2000 are replaced with 2s) and would like to recover the original values of the 2000 hidden bits with as much accuracy as possible. We can try to learn the patterns in the data ourselves, but perhaps a machine can do better.


The repository includes three datasets (input-easy, input-medium, input-hard) as well as a runner and example solver written in Python 3. You may need to install sklearn to run the program:


```
$ pip install sklearn
```


To test your code, just run runner.py with the dataset that you'd like to test on:


```
$ python runner.py easy
$ python runner.py medium
$ python runner.py hard
```


The example solver does a single-variable linear regression and its only feature is the previous bit. You may want to create new features, try new models, or even do some manual analysis of the data.


See how well you can do! It is possible to achieve more than 90% accuracy on all three datasets.


This exercise was inspired by IPSC 2017 problem K.