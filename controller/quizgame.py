
print("Welcome to Quiz Game")

# playing = input("Do you want to play? (yes/no)\n")
# if(playing == "yes"):
#     print("Welcome to Digital Gaming")
# elif(playing == "no"):
#     print("Come Back Soon, We are waiting!")
#     quit()
# else:
#     print("You Entered wrong input")
#     quit()


questionSet = [
    {
        "question" : "What is CPU stands for1 ",
        "ans1" : "ABC",
        "ans2" : "BCS",
        "ans3" : "XCS",
        "ans4" : "XOR",
        "correct" : 1
    },
    {
        "question" : "What is CPU stands for2",
        "ans1" : "ABC",
        "ans2" : "BCS",
        "ans3" : "XCS",
        "ans4" : "XOR",
        "correct" : 2
    },
    {
        "question" : "What is CPU stands for3",
        "ans1" : "ABC",
        "ans2" : "BCS",
        "ans3" : "XCS",
        "ans4" : "XOR",
        "correct" : 4
    },
    {
        "question" : "What is CPU stands for4",
        "ans1" : "ABC",
        "ans2" : "BCS",
        "ans3" : "XCS",
        "ans4" : "XOR",
        "correct" : 2
    },
    {
        "question" : "What is CPU stands for5",
        "ans1" : "ABC",
        "ans2" : "BCS",
        "ans3" : "XCS",
        "ans4" : "XOR",
        "correct" : 3
    }
]



def askQuestion(index):

    print("Ques: "+ questionSet[index]["question"])
    print("Option 1 "+questionSet[index]["ans1"])
    print("Option 2 "+questionSet[index]["ans2"])
    print("Option 3"+questionSet[index]["ans3"])
    print("Option 4"+questionSet[index]["ans4"])
    print("\n")
    outans = int(input("Enter Correct Answer? (1/2/3/4)\n"))
    if(outans == questionSet[index]["correct"]):
        print("Wow! Correct Answer")
        return 1
    else:
        print("correct ans is "+ str(questionSet[index]["correct"]) + " for question "+ str(index))

    print("\n")
    print("\n")
    return 0

score = 0
score += askQuestion(0)
score += askQuestion(1)
score += askQuestion(2)
score += askQuestion(3)
score += askQuestion(4)

print("You Scored "+ str(score))





