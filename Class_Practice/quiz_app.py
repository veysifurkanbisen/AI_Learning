class Question:
    def __init__(self, question, answer, point):
        self.question = question
        self.answer = answer
        self.point = point


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.total_score = 0

    def score(self):
        return "Your score is " + str(self.total_score)

    def make_quiz(self):
        for i in self.questions:
            print(i.question)
            answer = int(input("Your answer = "))
            if answer == i.answer:
                self.total_score += i.point
        print("\n", self.score())


def main():
    q1 = Question("What is 1 + 1 ?", 2, 10)
    q2 = Question("What is 1 + 2 ?", 3, 10)
    q3 = Question("What is 1 + 3 ?", 4, 10)
    q4 = Question("What is 1 + 4 ?", 5, 10)
    q5 = Question("What is 1 + 5 ?", 6, 10)

    quiz = Quiz([q1, q2, q3, q4, q5])
    quiz.make_quiz()


if __name__ == '__main__':
    main()
