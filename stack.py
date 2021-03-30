import random
class Stack:

    def __init__(self):
         self.container = []  

    def isEmpty(self):
        return self.size() == 0   

    def push(self, item):
        self.container.append(item)  

    def peek(self) :
        if self.size()>0 :
            return self.container[-1]
        else :
            return None

    def pop(self):
        return self.container.pop()  

    def size(self):
        return len(self.container)

    #method with an additional arguement that can remove the peek value of a queue
    def popLast(self,itemLast):
        return self.container.remove(itemLast)

    #method to print whole stack
    def printStack(self):
        currentIndex = 0
        for items in self.container:
            temp = currentIndex +1
            print(temp,"-",items)
            currentIndex += 1

#create new gifts stack
gifts = Stack()

#boolean test if gift stack is empty
gifts.isEmpty()

#push in gifts to gifts stack
gifts.push("iPhone XS ")
gifts.push("Wireless Headphones ")
gifts.push("Stuffed Bunny Toy ")
gifts.push("Nike Cap ")
gifts.push("Silver Heart Pendant ")
gifts.push("Happy Birthday Photo Frame ")
gifts.push("Gadget Key Chain ")
gifts.push("Smart Watch ")

#print gift stack
print("~ Mystery Gift Vending Machine ~ ")
gifts.printStack()
print("")

#print obtainable gifts
print("You will get one of these gifts below.")

#create new obtainableGifts stack
obtainableGifts = Stack()

#boolean test if obtainableGifts stack is empty
obtainableGifts.isEmpty()

#record down which gifts is obtained
firstGiftIndex = -1
secondGiftIndex = -1

#generate 3 random obtainable gifts
for i in range(3):

    #generate random number from 1 - 8
    gift = random.randint(1,8)

    #while the gift has been generated before
    while gift == firstGiftIndex or gift == secondGiftIndex:
        #generate a new gift from random number 1 - 8 
        gift = random.randint(1,8)

    #if we are generated the first gift
    if i == 0:
        #record down which is the first gift generated
        firstGiftIndex = gift
    elif i == 1:
        #record down which is the second gift generated
        secondGiftIndex = gift

    #if random number generated is 1, print smart watch and store it into a variable gift1, push the variable into obtainableGifts stack
    if(gift==1): 
        gift1 = "Smart Watch "
        print(gift1)
        obtainableGifts.push(gift1)

    #if random number generated is 2, print Gadget Key Chain and store it into a variable gift2, push the variable into obtainableGifts stack
    elif(gift==2):
        gift2 = "Gadget Key Chain "
        print(gift2)
        obtainableGifts.push(gift2)

    #if random number generated is 3, print Happy Birthday Photo Frame  and store it into a variable gift3, push the variable into obtainableGifts stack
    elif(gift==3):
        gift3 = "Happy Birthday Photo Frame "
        print(gift3)
        obtainableGifts.push(gift3)

    #if random number generated is 4, print Silver Heart Pendant and store it into a variable gift4, push the variable into obtainableGifts stack
    elif(gift==4):
        gift4 = "Silver Heart Pendant "
        print(gift4)
        obtainableGifts.push(gift4)
    
    #if random number generated is 5, print Nike Cap and store it into a variable gift5, push the variable into obtainableGifts stack
    elif(gift==5):
        gift5 = "Nike Cap "
        print(gift5)
        obtainableGifts.push(gift5)
    
    #if random number generated is 6, print Stuffed Bunny Toy  and store it into a variable gift6, push the variable into obtainableGifts stack
    elif(gift==6):
        gift6 = "Stuffed Bunny Toy "
        print(gift6)
        obtainableGifts.push(gift6)
    
    #if random number generated is 7, print Wireless Headphones and store it into a variable gift7, push the variable into obtainableGifts stack
    elif(gift==7):
        gift7 = "Wireless Headphones "
        print(gift7)
        obtainableGifts.push(gift7)
       
    #if random number generated is 8, print iPhone XS and store it into a variable gift8, push the variable into obtainableGifts stack
    elif(gift==8):
        gift8 = "iPhone XS "
        print(gift8)
        obtainableGifts.push(gift8)

    else:
        obtainableGifts.pop()

#create new stack to store final gift
finalGift = Stack()

#check if finalGift stack is empty
finalGift.isEmpty()

#choose 1 of 3 gifts from obtainable gift and push to final gift stack
finalGift.push(obtainableGifts.pop())

#print the final gift by peeking the gift from finalGift stack
print("\nYour gift is " + finalGift.peek() + "\n")

#print remaining gifts 
print('Here are the remaining gifts: ')

#if finalGift is smart watch, pop smart watch from gifts stack
if (finalGift.peek() == "Smart Watch "):
    gifts.popLast(finalGift.peek())

#if finalGift is Gadget Key Chain , pop Gadget Key Chain from gifts stack
elif (finalGift.peek() == "Gadget Key Chain "):
    gifts.popLast(finalGift.peek())

#if finalGift is Happy Birthday Photo Frame, pop Happy Birthday Photo Frame from gifts stack
elif (finalGift.peek() == "Happy Birthday Photo Frame "):
    gifts.popLast(finalGift.peek())

#if finalGift is Silver Heart Pendant , pop Silver Heart Pendant  from gifts stack
elif (finalGift.peek() == "Silver Heart Pendant "):
    gifts.popLast(finalGift.peek())

#if finalGift is Nike Cap , pop Nike Cap from gifts stack
elif (finalGift.peek() == "Nike Cap "):
    gifts.popLast(finalGift.peek())

#if finalGift is Stuffed Bunny Toy , pop Stuffed Bunny Toy from gifts stack
elif (finalGift.peek() == "Stuffed Bunny Toy "):
    gifts.popLast(finalGift.peek())
    
#if finalGift is Wireless Headphones , pop Wireless Headphones from gifts stack
elif (finalGift.peek() == "Wireless Headphones "):
    gifts.popLast(finalGift.peek())

#if finalGift is iPhone XS, pop iPhone XS from gifts stack
elif (finalGift.peek() == "iPhone XS "):
    gifts.popLast(finalGift.peek())

#print the remaining gifts
gifts.printStack()