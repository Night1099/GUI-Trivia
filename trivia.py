import tkinter as tk
import csv
import random

class Quiz:
    def __init__(self, master, filename):
        self.master = master
        self.questions = []
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.questions.append(row)
        random.shuffle(self.questions)
        self.current_question = 0
        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question]
        options = [question['answer'], question['decoy1'], question['decoy2'], question['decoy3']]
        random.shuffle(options)

        label = tk.Label(self.master, text=question['question'])
        label.pack()

        for option in options:
            button = tk.Button(self.master, text=option, command=lambda option=option: self.check_answer(option))
            button.pack()

    def check_answer(self, answer):
        if answer == self.questions[self.current_question]['answer']:
            print('Correct!')
        else:
            print('Incorrect')
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            for widget in self.master.winfo_children():
                widget.destroy()
            self.display_question()
        
if __name__ == '__main__':
    import sys
    root = tk.Tk()
    quiz = Quiz(root, sys.argv[1])
    root.mainloop()