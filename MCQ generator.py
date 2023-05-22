import tkinter as tk
import random


class MCQGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['A. London', 'B. Paris', 'C. Rome', 'D. Berlin'],
                'answer': 'B'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['A. Mars', 'B. Jupiter', 'C. Venus', 'D. Saturn'],
                'answer': 'A'
            },
            {
                'question': 'Who painted the Mona Lisa?',
                'options': ['A. Leonardo da Vinci', 'B. Vincent van Gogh', 'C. Pablo Picasso', 'D. Claude Monet'],
                'answer': 'A'
            }
        ]

        self.mcq_label = tk.Label(master, text="Multiple Choice Questions")
        self.mcq_label.pack()

        self.mcq_frame = tk.Frame(master)
        self.mcq_frame.pack()

        self.generate_button = tk.Button(master, text="Generate MCQs", command=self.generate_mcqs)
        self.generate_button.pack()

    def generate_mcqs(self):
        mcqs = random.sample(self.questions, 2)  # Generate 2 random MCQs

        # Clear existing MCQs from the frame
        for child in self.mcq_frame.winfo_children():
            child.destroy()

        # Display the generated MCQs
        for i, mcq in enumerate(mcqs, start=1):
            question_label = tk.Label(self.mcq_frame, text=f"Question {i}: {mcq['question']}")
            question_label.pack()

            for option in mcq['options']:
                option_label = tk.Label(self.mcq_frame, text=option)
                option_label.pack()

            separator = tk.Label(self.mcq_frame, text="------------------")
            separator.pack()


# Create the main window
root = tk.Tk()
root.title("MCQ Generator")

# Create an instance of MCQGeneratorGUI
mcq_generator_gui = MCQGeneratorGUI(root)

# Run the GUI application
root.mainloop()