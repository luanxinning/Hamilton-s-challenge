# Hamilton's-challenge
Simulate a random DNA sequence and predict it by short-read sequencing

In this program, I need to predict, or, to some extent, find out the true/whole sequence only with many chops/reads. The total procedure is listed below:
1.Find the start point. The whole prediction will rely on it later.
The most important of this prediction is finding all of the l-1 similarity part, called bar, and find out how many times does each bar occur in all pairs of chopped reads. These bars are stored into a dictionary called bar, there the keys are bar sequences( l-1 length) and the values are their frequencies.
The start point is its bar with highest frequency.
2.prolong the predicted sequence start by start
On both side (left and right), I add a nucleotide each time. These two nucleodtides are also determined by frequencies:
I find the read that l-1 length of it is the same with l-1 length of start(meaning start and this read share l-1 similarity). Among all of these reads, I choose the one with highest frequency and add it on left/right side of start. After adding, the start will be updated, the new start has two more nucleotides compared with the formal one. After looping, I can get the final sequence.
3.How to end prolonging
A) I can’t find any read to add anymore
B) The predicted sequence is too long (in this case, I set it to be no more than 1.5 length of simulated sequence.)  

note:
After several tests, I find that if the length of reads is long enough(the length of reads are at least one fifth of the length of simulated sequences, and it should be bigger than about 5 or 6), the accuracy of the prediction can be 100%. If not, the program will tell the user to increase the length of reads(bases).
