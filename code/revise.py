import csv
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to get a question and answer from the user
def get_question_and_answer():
    question = input("Enter a question: ")
    answer = input("Enter the answer: ")
    return question, answer

# Function to quiz the user on existing questions
def quiz_user(qa_dict):
    questions = list(qa_dict.keys())
    random.shuffle(questions)

    for question in questions:
        user_answer = input(f"{Fore.YELLOW}Question: {question}\n{Style.RESET_ALL}{Fore.CYAN}Enter your answer: ")
        correct_answer = qa_dict[question]

        if user_answer.lower() == correct_answer.lower():
            print(f"{Fore.GREEN}Correct!\n{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Incorrect. The correct answer is: {correct_answer}\n{Style.RESET_ALL}")

# Ask the user for a CSV file path
csv_path = input("Enter the path to an existing CSV file (leave blank for a new file): ")
csv_filename = 'qa_data.csv'


# Initialize the dictionary
qa_dict = {}

# If the user provided a CSV file path, load existing data
if csv_path:
    try:
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                qa_dict[row['Question']] = row['Answer']
        print(f"{Fore.GREEN}Existing data loaded successfully.{Style.RESET_ALL}")

        # Ask the user if they want to input new data or study
        action = input(f"{Fore.YELLOW}Do you want to input new data (input) or study existing questions (study)? {Style.RESET_ALL}").lower()

        if action == 'study':
            quiz_user(qa_dict)
            exit()

    except FileNotFoundError:
        print(f"{Fore.RED}File not found. Creating a new dictionary.{Style.RESET_ALL}")
        csv_filename = csv_path


# Main loop to keep asking for questions and answers until the user decides to stop
while True:
    question, answer = get_question_and_answer()

    # Store the question and answer in the dictionary
    qa_dict[question] = answer

    # Ask the user if they want to add more questions and answers
    another = input(f"{Fore.YELLOW}Do you want to add another question and answer? (yes/no): {Style.RESET_ALL}").lower()

    # If the user enters anything other than "yes", exit the loop
    if another != 'yes':
        break

# Save the questions and answers in a CSV file

with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Question', 'Answer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for question, answer in qa_dict.items():
        writer.writerow({'Question': question, 'Answer': answer})

print(f"{Fore.GREEN}Your dictionary has been saved to {csv_filename}.{Style.RESET_ALL}")
