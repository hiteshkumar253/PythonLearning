# Problem 5: Create a class Train which has methods to book a ticket, get status of the train and get fare of the train.    
import random
class Train:

    def __init__(self, TrainNo):
        self.TrainNo = TrainNo
    
    def bookTrain(self, source, destination):
        print(f"Success! Train number {self.TrainNo} is booked from {source} to {destination}.")

    def getStatus(self):
        print(f"Train number {self.TrainNo} is on time.")

    def getFare(self, source, destination):
        print(f"Train fare of train no. {self.TrainNo} from {source} to {destination} is {random.randint(100,1000)}")

train = Train(23434)
train.bookTrain("Delhi", "Mumbai")
train.getStatus()
train.getFare("Delhi", "Mumbai")
