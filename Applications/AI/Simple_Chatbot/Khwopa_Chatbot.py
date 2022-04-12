import pickle
import random
class Khwopa_Chatbot:
    sorry = ["I can not answer that question.", "I'm so sorry i have no answers.",
             "I'm unauthorize to answer that questions"]
    thank =["Have a good day.","Namaste.", "Thank you for your time."]

    def __init__(self):
        self.greetings()


        with open("Questions.pickle", "rb") as file:
            self.questions = pickle.load(file)

        with open("Answers.pickle", "rb") as file:
            self.answers = pickle.load(file)

        self.Q_and_A = dict(zip(self.questions, self.answers))

    def greetings(self):
        print("------" * 20)
        print("Namaste.")
        print("------" * 20)
        print("I'm Khwopa Chatbot.")
        print("You can ask any questions related to Khwopa College of Engineering.")

    def chat(self):
        print("-------"*20)
        question = input("Enter the question you would like to ask:").lower().strip() # converting to lower case and striping white spaces
        question = question.replace("?","")
        if len(question) == 1: #single character question is not valid
            self.fail()
            return
        temp = 0
        for i in self.Q_and_A.keys():
            if question in i.lower(): # there is answer in dataset condition
                print(f"\n{self.Q_and_A[i]}")
                temp = 1

        if temp == 0: # there is no answer in dataset condition
            self.fail()

    def fail(self):
        print(f"\n{self.sorry[random.randint(0,2)]}")
        print("\nPlease contact to Khwopa Administrator for more details.")
        print("\nContact Numbers: (+977) 1-5122094, 5122098"
                "\nContact Email: info@khwopa.edu.np, khce.tu@gmail.com")

if __name__ == "__main__":
    s = Khwopa_Chatbot()
    while True:
        s.chat()
        opt = input("\nDo you have any other questions(yes/no):").lower()
        if opt == 'yes':
            continue
        else:
            print(f"\nThank you for the question.\n{s.thank[random.randint(0, 2)]}")
            break

