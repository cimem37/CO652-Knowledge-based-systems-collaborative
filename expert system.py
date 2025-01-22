class ExpertSystem:
    def __init__(self, rules):
        self.rules = rules

    def forward_chain(self, problem):
        solutions = []
        for rule in self.rules:
            if rule["problem"] == problem:
                solutions.extend(rule["solutions"])
        return solutions

    def ask_question(self, solution):
        while True:  # Loop until a valid response is entered
            response = input(f"Solution: {solution} - Did this solve the problem? (yes/no): ").strip().lower()
            if response in {"yes", "no"}:
                return response == "yes"
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


def get_valid_choice(prompt, choices):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(choices)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


rules = [
    {
        "problem": "computer won't start",
        "solutions": [
            "Check if the power cable is connected",
            "Try pressing the power button for 10 seconds",
            "Check if the power supply is working"
        ]
    },
    {
        "problem": "slow internet",
        "solutions": [
            "Restart the router",
            "Check for background downloads",
            "Contact your internet service provider"
        ]
    },
    {
        "problem": "high CPU usage",
        "solutions": [
            "Close unnecessary programs",
            "Scan for malware",
            "Check the task manager for any processes taking up CPU"
        ]
    },
    {
        "problem": "BSOD",
        "bsod_codes": [
            {
                "code": "0x0000000A: IRQL_NOT_LESS_OR_EQUAL",
                "solutions": [
                    "Restart your PC",
                    "Run Checkdisk",
                    "Delete System32 (Not recommended)"
                ]
            },
            {
                "code": "0x0000007B: INACCESSIBLE_BOOT_DEVICE",
                "solutions": [
                    "Check your BIOS settings",
                    "Ensure the boot drive is connected",
                    "Run Startup Repair"
                ]
            },
            {
                "code": "0x0000001E: KMODE_EXCEPTION_NOT_HANDLED",
                "solutions": [
                    "Update drivers",
                    "Run a memory diagnostic",
                    "Check recently installed software"
                ]
            }
        ]
    }
]

expert_system = ExpertSystem(rules)

while True:  # This is our main menu loop, stops the menu from closing after the user has made a choice
    # List of problems menu
    print("\nWelcome to the Technical support expert system by Brunaldo Cimo and Hishaam Mehmood!") # Welcome message
    print("Please select a problem to solve:")
    problems = list(set(rule["problem"] for rule in rules))
    for i, problem in enumerate(problems, 1):
        print(f"{i}. {problem}")
    print(f"{len(problems) + 1}. Exit")  # selec option to exit

    # Gets a valid problem choice from the user
    problem_choice = get_valid_choice("Enter the number of the problem: ", problems + ["Exit"])

    if problem_choice == len(problems) + 1:  # Exit option
        print("See ya, Boss!") # exit message
        break

    selected_problem = problems[problem_choice - 1]
    print(f"\nProblem selected: {selected_problem}\n")

    if selected_problem == "BSOD":
        print("Select a BSOD code:")
        bsod_codes = next(rule["bsod_codes"] for rule in rules if rule["problem"] == "BSOD")
        for i, bsod in enumerate(bsod_codes, 1):
            print(f"{i}. {bsod['code']}")

        # Get a valid BSOD code choice
        bsod_choice = get_valid_choice("Enter the number of the BSOD code: ", bsod_codes)
        selected_bsod = bsod_codes[bsod_choice - 1]
        print(f"\nBSOD code selected: {selected_bsod['code']}\n")

        solutions = selected_bsod["solutions"]
        for solution in solutions:
            solved = expert_system.ask_question(solution)
            if solved:
                print(f"Problem solved with: {solution}")
                break
        else:
            print("No solution worked, consider contacting your technical support administrator.")
    else:
        solutions = expert_system.forward_chain(selected_problem)
        for solution in solutions:
            solved = expert_system.ask_question(solution)
            if solved:
                print(f"Problem solved with: {solution}")
                break
        else:
            print("No solution worked, consider contacting support.")


# Test

# test

# Hishaam was here