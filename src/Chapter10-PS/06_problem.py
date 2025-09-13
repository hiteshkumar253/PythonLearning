# try to update self to slf or any other name (abc) and see if it works. What is the impact?
# we are just changing the name of the first argument of the method. It can be anything, but by convention we use 'self'.

import random
class Train:

    def __init__(slf, TrainNo):
        slf.TrainNo = TrainNo
    
    def bookTrain(slf, source, destination):
        print(f"Success! Train number {slf.TrainNo} is booked from {source} to {destination}.")

    def getStatus(slf):
        print(f"Train number {slf.TrainNo} is on time.")

    def getFare(slf, source, destination):
        print(f"Train fare of train no. {slf.TrainNo} from {source} to {destination} is {random.randint(100,1000)}")

train = Train(23434)
train.bookTrain("Delhi", "Mumbai")
train.getStatus()
train.getFare("Delhi", "Mumbai")
