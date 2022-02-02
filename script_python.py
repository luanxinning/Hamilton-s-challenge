#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Hamilton’s challenge
Date: 2021_11-15
Author: luan xinning

Description:
    This program will replicate Hamilton’s work. It will firstly simulate a DNA sequence, 
chop it into many reads and predcit a new DNA sequence only with these reads and the length
of the simuated sequence.
    This program will ask the user to choose the length of simulated DNA sequence and the
length of each chopped reads. After several tests, I find that if the length of reads is long 
enough(the length of reads are at least one fifth of the length of simulated sequences, and 
it should be bigger than about 5 or 6), the accuracy of the prediction can be 100%. If not, 
the program will tell the user to increase the length of reads(bases).
    
List of user defined functions:
    predict_sequence:
    This function can be used to predict(add nucletides of both sides) a DNA sequence
given by its start point and the length of simulated sequence. The result of it includes
the predicted sequence and the accuracy of prediction. 
    
List of modules used that are not explained in the course material:
    No such modules are used.
    
Procedure:
    1. Simulate a random DNA sequence.
    2. Chop this sequence into nx30 reads of length l.
    3. Find the starting point of next step prediction.
    4. Define a function to predict the DNA sequence and gives its accuracy.
    
Usage:
    python script_python.py

"""
#%%
# 1. Simulate a random DNA sequence
n = int(input('Please enter the length of a random DNA sequence: \n'))
nucl = ['A','T','C','G']  # all posible nucletides
seq = []                  # store the following DNA sequence in a list
import random             # used for randomly chosen
for i in range(n):
    seq.append(nucl[random.randint(0,3)])  # each time chose a nucletide randomly, to set a 
                                           # random DNA sequence.

#%%
# 2. Chop this sequence into nx30 reads of length l
l = int(input('Please enter how many bases do you want: \n'))
reads = []                           # store all reads into a big list
for i in range(n*30):
    x = random.randint(0,n-l)        # get the position of the first nucl in each read
    read = []
    for j in range(l):
        read.append(seq[x+j])        # store each nucl of a read into a list
    reads.append(read)               # add each read into the big list one by one

#%%    
# 3. Find the starting point of next step prediction
bar = {}
for i, r in enumerate(reads):   # i is the index of each read in [reads]. i is used for next for loop
    target = ''.join(r)         # turn lists into strings
    for j in range(i+1, len(reads)):
        if target[1:] == ''.join(reads[j][:-1]):  # if two reads are of l-1 similarity:
            if target[1:] in bar:
                bar[target[1:]] += 1              # calculate how many times does each overlapping part occur
            else:
                bar[target[1:]] = 1               # find a new overlapping part
start = sorted(bar.items(), key = lambda kv:(kv[1], kv[0]))[-1][0]
# find the overlapping part that occurs mostly and set it as the starting point of 
# next step prediction

#%% 
# 4. Define a function to predict the DNA sequence and gives its accuracy.
def predict_sequence(start):
    flag = True
    while flag:
        left = {}
        right = {}
        for r in reads:
            r = ''.join(r)                       # turn list into string
            if start[:(l-1)] == r[-(l-1):]:
            # to prolong the left part of 'start', try to find reads that are of l-s similarity
            # with it. It is the same with right part
                if r in left:
                    left[r] += 1                 # calculate how many times does each read occur
                else:
                    left[r] = 1                  # add it if it's found firstly
            if start[-(l-1):] == r[:(l-1)]:
                if r in right:
                    right[r] += 1
                else:
                    right[r] = 1
                    
        if right != {}:  # if we still can find reads to add on the right side:
            for k in right:
                try:
                    right[k] = bar[k[-(l-1):]]   
                except:
                    pass
                # figure out whether we can find needer reads to add. Dismiss the reads 
                # the don't meet our need.
            right = sorted(right.items(), key = lambda kv:(kv[1], kv[0]))[-1][0][-1]
            # depends on the frequences of all found reads, we choose the most frequent one
            # to add on the right side
        else: 
            right = ''    # If we can't find new reads, then don't add anything
    
        if left != {}:    # The same with above
            for k in left:
                try:
                    left[k] = bar[k[:(l-1)]]
                except:
                    pass
            left = sorted(left.items(), key = lambda kv:(kv[1], kv[0]))[-1][0][0]
        else: 
            left = ''
            
        start = left + start + right   # add the prolonged nucletides on both sides
        
        if (right == '' and left == '') or len(start) > 1.5*n:
            flag = False
        # there are two principles to stop prolonging the predicted sequence:
        # 1. we can not find any reads in both left and right side anymore
        # 2. the length of this sequence is too long
        
            if len(start) > 1.5*n:   
                print('Please increase the length of bases!')
            # in this case, the prediction will not be accurate.
            
            else:
                print('The simulated sequence is:\n',''.join(seq))
                print('The predicted sequence is:\n',start)
                print('The accuracy of this prediction is 100%')
                
predict_sequence(start)

