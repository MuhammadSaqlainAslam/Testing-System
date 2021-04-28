class Testing_System:
    def __init__(self):
        self.question_prompt = []
        self.score_table = {}

    def do_quiz(self):
        def run_test(quiz_lst, ans_lst):
            score = 0
            for question, gt_answer in zip(quiz_lst, ans_lst):
                answer = input(question)
                if answer == gt_answer:
                    score += 1
            return score

        stud_name = input("Type your name : ")
        print ("Select the level of Question: ")
        question_level = -1
        while question_level not in [0, 1, 2]:
            question_level = int(input("(0) Simple  (1) Medium (2) Hard: \n"))
        quiz_lst = []; ans_lst = []
        for lst in self.question_prompt:
            if lst[0] == question_level:
                quiz_lst.append(lst[1]) ; ans_lst.append(lst[2])

        final_score = run_test(quiz_lst, ans_lst)
        if stud_name not in self.score_table.keys():
            self.score_table[stud_name] = [final_score]
        else:
            self.score_table[stud_name].append(final_score)
        print("You got " + str(final_score) + "/" + str(len(quiz_lst)) + " correct ")

    def add_quiz(self):

        question_level = -1
        print("Select question level\n")
        while question_level not in [0, 1, 2]:
            question_level = int(input("(0) Simple  (1) Medium (2) Hard: \n"))

        problem_statement = input("Enter Problem Statement: ")
        answers = input("Enter corresponding answers: ")
        self.question_prompt.append( [question_level, problem_statement, answers] )

    def get_stud_score(self):
        stud_name = input("Type the student name")
        score_lst = self.score_table[stud_name]
        for score in score_lst:
            print("The score : {} \n".format(score))

## pre-define q :
'''
question_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]
'''


if __name__ == "__main__":
    tst_sys = Testing_System()
    tst_sys.add_quiz()
    tst_sys.do_quiz()
    tst_sys.get_stud_score()
