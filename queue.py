class Queue:
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return self.size() == 0  

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        self.container.pop(0)

    def size(self):
        return len(self.container)

    def peek(self) :
        return self.container[0]  

import random

#create new queue to store preliminary participants in preliminary round
preliminary = Queue()

#create new queue to store the final participants that qualify for final round
finalQ = Queue()

#create new queue to store the number of participants in final round
lastRound = Queue()

#enqueue all participatns to preliminary queue
preliminary.enqueue("Ada")
preliminary.enqueue("Bala")
preliminary.enqueue("Chloe")
preliminary.enqueue("Dylan")
preliminary.enqueue("Elvin")
preliminary.enqueue("Fadhilah")
preliminary.enqueue("Gwendolyn")
preliminary.enqueue("Hakim")
preliminary.enqueue("Ian")
preliminary.enqueue("Jeremy")

#create variable to store the total score of participants in the preliminary round
preliminaryTotalScore = 0

#create variable to store the total number of medals that the participants obtain in the final round
totalNumOfMedal = 0

#print the Preliminary round
print("Preliminary round starts...\n")

#loop the same number of times as the size of preliminary queue
for i in range(0,preliminary.size()): 

    #generate random number from 0 to 100
    score1 = random.randint(0,100)   

    #add up the total score of everyone in prelimninary round
    preliminaryTotalScore += score1

    #print in ascending order of each participant with the name and score
    print("Participant #"+str(i+1)+":"+preliminary.peek()+ " - " + str(score1))

    #check if each participant score is more than 50, and if its more than 50, store into finalQ queue
    if (score1 >= 50):
        finalQ.enqueue(preliminary.peek())
        preliminary.dequeue()
    
    else :
        preliminary.dequeue()

print("\nFinal round starts...\n")

#loop the same number of times as the size of finalQ queue
for i in range(0,finalQ.size()):  

    #generate random number from 0 to 100
    score2 = random.randint(0,100)   
    
    #check if each participant score is more than 80, and if its more than 80, print the participant name, score and gold medal
    if (score2 >= 80):
        print("Participant #"+str(i+1)+":"+finalQ.peek()+ " - " + str(score2) + " -" + " Gold")

        #add up total number of medals obtained
        totalNumOfMedal += 1 

        #store participants to new queue
        lastRound.enqueue(finalQ.dequeue()) 
    
    #check if each participant score is more than 60, and if its more than 60, print the participant name, score and silver medal
    elif(score2 >=60 ):
        print("Participant #"+str(i+1)+":"+finalQ.peek()+ " - " + str(score2) + " -" + " Silver")

        #add up total number of medals obtained
        totalNumOfMedal += 1 

        #store participants to new queue
        lastRound.enqueue(finalQ.dequeue()) 

    #check if each participant score is more than 40, and if its more than 40, print the participant name, score and bronze medal
    elif(score2 >= 40):
        print("Participant #"+str(i+1)+":"+finalQ.peek()+ " - " + str(score2) + " -" + " Bronze")

        #add up total number of medals obtained
        totalNumOfMedal += 1 

        #store participants to new queue
        lastRound.enqueue(finalQ.dequeue()) 

    #if participants score is less than 40, print only the participants name and score only without medal
    else :
        print("Participant #"+str(i+1)+":"+finalQ.peek()+ " - " + str(score2))

        #store participants to new queue
        lastRound.enqueue(finalQ.dequeue())

#print average score of preliminary round
print (" \nThe average/mean score for preliminary round is " + str(preliminaryTotalScore / 10) + ".")    

#print percentage of participants getting into final round
print(" \nThe percentage of participants getting into final round is " + str((lastRound.size() / 10) * 100) + "%"  + ".")

#print total number of participants that get a medal
print(" \nThe number of participants getting a medal is " + str(totalNumOfMedal) + ".")