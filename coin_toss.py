import random
def coinToss(number):
    recordList = []
    heads = 0
    tails = 0
    for i in range(number):
         flip = random.randint(0, 1)
         if (flip == 0):
              print("Heads")
              recordList.append("Heads")
         else:
              print("Tails")
              recordList.append("Tails")
    print(str(recordList))
    print((str(recordList.count("Heads")) +" "+ str(recordList.count("Tails"))))

number = int(input("Number of times to flip coin: "))    
coinToss(number)
