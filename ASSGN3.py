#Q.1 - Consider the below given probabilities: 
'''P(A) = 11 / 36
P(B) = 6 / 36
P(A|B) = 2 / 36
Write a function in Python which takes 3 probabilities as argument and outputs
the Conditional probability P(B|A).
'''

from fractions import Fraction
def probab(A, B, C):
    print("P(A): %f" %(A))
    print("P(B): %f" %(B))
    print("P(A|B): %s" %(C))
    cond_probab=(C*B)/A
    return cond_probab
    
probab(11.0/36,6.0/36,2.0/36)

#Q.2 - Bag I contains 4 white and 6 black balls while another Bag II contains 4
white and 3 black balls. 
#One ball is drawn at random from one of the bags and it is found to be black. 
#Find the probability that it was drawn from Bag I.


bag1=1.0/2 #probability of selecting bag1
bag2=1.0/2 #probability of selecting bag2
black1=6.0/10 #probability of selecting black ball from bag1
black2=3.0/7 #probability of selecting black ball from bag2
prob=(bag1*black1)/((bag1*black1)+(bag2*black2))
print(prob)

#Q.3 - A man is known to speak truth 2 out of 3 times.
#He throws a die and reports that number obtained is a four.
#Find the probability that the number obtained is actually a four.


truth=2.0/3
lie=1.0/3
four=1.0/6
nofour=5.0/6
prob=(truth*four) / ((truth*four) + (lie*nofour))
print(prob)
