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
        response = input(f"Solution: {solution} - Did this solve the problem? (yes/no): ").strip().lower()
        return response == "yes"


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
        "problem": "0x0000000A: IRQL_NOT_LESS_OR_EQUAL",
        "solutions": 
            
            [
                "Restart your pc",
                "Run checkdisk",
                "Delete System 32"
            ]

}
]

# Initialize the expert system
expert_system = ExpertSystem(rules)

# List of problems
print("Select a problem to solve:")
problems = list(set(rule["problem"] for rule in rules))
for i, problem in enumerate(problems, 1):
    print(f"{i}. {problem}")

try:
    choice = int(input("Enter the number of the problem: "))
    if 1 <= choice <= len(problems):
        selected_problem = problems[choice - 1]
        print(f"\nProblem selected: {selected_problem}\n")
        
        solutions = expert_system.forward_chain(selected_problem)

        for solution in solutions:
            solved = expert_system.ask_question(solution)
            if solved:
                print(f"Problem solved with: {solution}")
                break
        else:
            print("No solution worked, consider contacting support.")
    else:
        print("Invalid choice.")
except ValueError:
    print("Please enter a valid number.")

    #test
       #test5 