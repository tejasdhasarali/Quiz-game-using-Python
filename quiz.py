from random import *;
from sports import*;
from capital import *;
from political import*;
class WrongEntry(Exception):
    def __init__(self,x):
        Exception.__init__(self)
        self.x1=x
print "WELCOME TO QUIZ!!!\n"
print"Do you wish to see the Instruction...!??"
print"If yes type '1' otherwise type any other number"
z=input()
if z==1:
    print"INSTRUCTION:\n1.Enter the full answer as half answer is considered as wrong\n2.Make sure that you will enter the correct spelling as answer with wrong spelling is considered as wrong\n3.Don't use any punctuations in the answer\n4.Please Don't enter the answer in numbers\n"
print"---------------------------------------------------------------------------------------------------------------------------------------------------------------"
while(1):
    print"Enter the number of questions you want to face"
    n=input()
    try:
        print"Enter the type of questions you want to face\nFOR QUESTION RELATED TO:\n\t\tCAPITALS OF DIFFERENT COUNTRIES : TYPE 1\n\t\tFIRST INDIAN : TYPE 2\n\t\tSPORTS : TYPE 3"
        t=input()
        print"---------------------------------------------------------------------------------------------------------------------------------------------------------------"
        if t!=1 and t!=2 and t!=3:
            raise WrongEntry("Wrong entry\nERROR!!!")
    except WrongEntry as ex:
        print ex.x1
        break
    print"Choose the difficult level\n1:EASY\n2:INTERMEDIATE\n3:HARD"
    print"IN EASY LEVEL :\n\tYou will get a second chance for answering the same question"
    print"IN INTERMEDIATE LEVEL :\n\tNo negative marking or no second chance is given"
    try:
        print"IN HARD LEVEL :\n\tYou will loose 1 from your final score for every wrong answer"
        d=input()
        print"---------------------------------------------------------------------------------------------------------------------------------------------------------------"
        if d!=1 and d!=2 and d!=3:
            raise WrongEntry("Wrong choice\nERROR!!!")
    except WrongEntry as ex1:
        print ex1.x1
        break   
    try:
        if t==1:
            list1=sample(capital,n)
            dict1=capital
            print"Country name is displayed and you should guess its capital"
        elif t==2:
            list1=sample(political,n)
            dict1=political
        elif t==3:
            list1=sample(sports,n)
            dict1=sports
    except ValueError:
        print"ERROR !!!\nEntered number of questions exceeds predefined number of questions"
        break
    score=0
    for i in range (1,n+1):
        print"Question No %i is :"%(i)
        print list1[i-1]
        ans=raw_input().lower()
        if ans==dict1[list1[i-1]].lower():
            print"Excellent!!! your answer is correct"
            score+=1
        else:
            print"Sorry your answer is wrong"
            if d==1:
                print"You will get a second chance for answering the same question since it is easy level"
                ans=raw_input().lower()
                if ans==dict1[list1[i-1]].lower():
                    print"Excellent!!! your answer is correct"
                    score+=1
                else:
                    print"Sorry your answer is wrong again"
            elif d==3:
                score-=1
            print"The right answer for the question {} is :".format(list1[i-1])
            print dict1[list1[i-1]]
        print"\nYour present score after answering %i questions is :"%(i)
        print score
        print"---------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print"\n\nTHANK YOU FOR PLAYING THE QUIZ!!!\n\n"
    print"Your final score of the quiz is : {}/{}".format(score,n)
    print "\nIf you wish to continue the quiz press 1 otherwise press any other number to quit"
    a=input()
    if a!=1:
        break
print"\n\nTHANK YOU\n\n"
print"\nCome back and improve your general knowledge\n"
