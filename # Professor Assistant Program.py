# Professor Assistant Program
# Created by: Sushmita Rokka
# This program helps professors create exams from a question bank.

import random

print("Welcome to professor assistant version 1.0.")
professor_name = input("Please Enter Your Name: ")

print(f"Hello Professor {professor_name}, I am here to help you create exams from a question bank.")

while True:
    choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()

    if choice == "no":
        print(f"Thank you professor {professor_name}. Have a good day!")
        break

    elif choice == "yes":
        # Ask for question bank path
        q_path = input("Please Enter the Path to the Question Bank: ")

        # Try reading the question bank
        try:
            with open(q_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            print("Yes, indeed the path you provided includes questions and answers.")

        except FileNotFoundError:
            print("The file path you entered is incorrect. Please try again.\n")
            continue

        # Prepare question and answer pairs
        qa_pairs = []
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i + 1].strip()
            qa_pairs.append((question, answer))
        # Ask how many questions the professor wants
        while True:
            try:
                num_questions = int(input("How many question-answer pairs do you want to include in your exam? "))
                if num_questions <= 0:
                    print("Please enter a positive number.")
                    continue
                if num_questions > len(qa_pairs):
                    print("Not enough questions in the question bank. Try a smaller number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        # Ask where to save the exam
        output_file = input("Where do you want to save your exam? ")

        # Select random questions
        selected = random.sample(qa_pairs, num_questions)

        # Save to file
        with open(output_file, "w", encoding="utf-8") as out:
            for q, a in selected:
                out.write("Q: " + q + "\n")
                out.write("A: " + a + "\n\n")

        print(f"Congratulations Professor {professor_name}. Your exam is created and saved in {output_file}.\n")

    else:
        print("Invalid input. Please type Yes or No.\n")