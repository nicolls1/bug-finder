# Bug Finder

## Overview

### Algorithm Thoughts

Let's we define our landscape as X by Y gird and the bug as a N by M grid. All lines in our grid are an equal width X but a bug does not need to have the same length lines so N will be the max length.

We are first constrained by reading the file which is an O(X\*Y) operation. To check for a valid bug we will need to compare every bug value for an O(N\*M) operation. The referenced brute force approach in the problem definition would be checking every possible position for a bug and it would be O(X\*Y\*N\*M). 

A first small improvement would be removing the bottom and right edges that are outside of the range of the bug to get O((X-N)\*(Y-M)\*N\*Y). Given that this is only a small improvement and that its not really one when the bug is much smaller than the landscape, it seems there must be something more.

### Inputs as Matrices 

If we interpret the bug and the landscape as matrices, we can do matrix operations to try and find where the bugs are. From a runtime perspective, we will still be doing operations at every location in the landscape but since we won't be branching with the matrix operations. Also, GPUs exist for matrix operations and could speed up large inputs. 

### Correlation between matrices

I first looked around how people would solve finding a sub-image in a larger image since it seems like a similar problem. I realized that the better, more general, problem I was trying to solve is finding a sub-matrix in a larger matrix. Matlab has a function called normxcorr2 but this does not exist in python. At some point, I found this implementation as a possible solution: https://github.com/Sabrewarrior/normxcorr2-python/blob/master/normxcorr2.py. I was able to simplify the implementation and make it more specific to this problem. There was quite a bit more research and tinkering that went on as my signal processing knowledge is a bit rusty but that was the general process to finding the solution.

### Pip Libraries

* Numpy: Numpy is a standard library for doing matrix operations so it seemed very appropriate for this problem
* Scipy: Scipy provides the fftconvolve method. This function convolve the matrices by doing multiplication in the frequency domain. I used it because I didn't feel the need to reinvent the wheel.

## Usage

### Install

Assuming you have a fresh python 2.7 environment with pip installed, install pip requrements with:
```
pip install -r requirements.txt 
```

### Run

```
python main.py <path_to_bug> <path_to_landscape>
```

Example:
```
python main.py test_files/default/bug.txt test_files/default/landscape.txt
```

### Test

```
python tests.py
```

## Edit Update:

It seems the landscape file is ended with 2 newlines and I removed one of them during my testing. I added a check to see if the last line is empty and remove it if it is. Also, I added a test to check if the landscape file is valid and a unit test for it.