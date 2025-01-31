class CollegeAdmissionsChatbot:
    def __init__(self):
        self.admissions_requirements = {
            "high_school_diploma": "A high school diploma or equivalent",
            "gpa": "A minimum GPA of 3.0",
            "sat_or_act_scores": "SAT or ACT scores (test-optional)",
            "letters_of_recommendation": "Letters of recommendation from a guidance counselor and a teacher",
            "personal_statement": "A personal statement or essay"
        }
        self.application_deadlines = {
            "early_decision": "November 1st",
            "early_action": "December 1st",
            "regular_decision": "February 1st"
        }
        self.financial_aid_options = {
            "merit_based_scholarships": "Merit-based scholarships",
            "need_based_grants": "Need-based grants",
            "federal_student_loans": "Federal student loans",
            "work_study_programs": "Work-study programs"
        }

    def get_admissions_requirements(self):
        print("Our admissions requirements include:")
        for requirement, description in self.admissions_requirements.items():
            print(f"- {description}")

    def get_application_deadlines(self):
        print("Our application deadlines are:")
        for deadline, date in self.application_deadlines.items():
            print(f"- {deadline.capitalize().replace('_', ' ')}: {date}")

    def get_financial_aid_options(self):
        print("We offer the following financial aid options:")
        for option, description in self.financial_aid_options.items():
            print(f"- {description}")

    def chat(self):
        print("Welcome to our college admissions chatbot!")
        while True:
            print("What would you like to know?")
            print("1. Admissions requirements")
            print("2. Application deadlines")
            print("3. Financial aid options")
            print("4. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.get_admissions_requirements()
            elif choice == "2":
                self.get_application_deadlines()
            elif choice == "3":
                self.get_financial_aid_options()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    chatbot = CollegeAdmissionsChatbot()
    chatbot.chat()
```
