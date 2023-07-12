import random


class RandomNumberGussGame:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self):
        print(self.OKBLUE+ 'Welcome to Gaming World')
        self.num = 0
        self.start()

    def start(self):
        self.counter = 0
        self.num = self.generateNumer()
        self.checkAndResponse()

    def askTorestart(self):
        ques = input("Would you like to restart? yes/no \n")
        if(ques == 'yes'):
            self.start()
        else:
            print("Thank you for playing")
            exit()
        pass

    def checkAndResponse(self):
        guess = int(self.guessNumber())
        self.counter +=  1
        if(self.num < guess):
            print(self.FAIL + "Number is less than "+ str(guess))
            self.checkAndResponse()
        elif(self.num > guess):
            print(self.FAIL + "Number is greater than "+ str(guess))
            self.checkAndResponse()
        else:
            print(self.OKGREEN + self.HEADER + "Wow! you entered correct number")
            print(self.BOLD + "You have used " + str(self.counter) + " attempts.")
            self.askTorestart()


    def generateNumer(self) -> int:
        return random.randint(1,100)

    def guessNumber(self):
        return input(self.WARNING + "Enter number\n")



game = RandomNumberGussGame()

