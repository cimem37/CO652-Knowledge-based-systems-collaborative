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

# These are our problems below, the user will select one of them by entering the corresponding rule number.
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
                    "Reinstall/update display and network drivers through device manager. (consideration message) :  different processes depending on dedicated or integrated gpu.  Otherwise uninstall through device manager on Windows right click ( uninstall option ) on both network & display as drivers will be installed automatically (as you removed all existing driver / settings of the machine ).",
                    "Run Checkdisk:  Disk scan- right click local drive, properties, tools - check /Will do an check disk / error check on the next reboot, if required before you get to the desktop.  That fixes corrupt files on machine that cause blue screen.",
                    "Run the following command in CMD using administrator mode in order to load the most recent windows restoration point: DISM /ONLINE /CLEANUP-IMAGE /RESTOREHEALTH ",
                    "Run the SFC /SCANNOW command in CMD with administrator mode- This is a windows file system scan, it reinstalls any corrupt system files.",

                ]
            },
            {
                "code": "0x0000000D: EXCEPTION_DOUBLE_FAULT",
                "solutions": [
                    "Restore your most recent backup.",
                    "Create a Windows Media Creation tool using a USB stick or a dvd. Install the Media Creation tool from: https://support.microsoft.com/en-gb/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d.",
                    "Run the following command in Windows powershell while in administrator mode: Get-AppxPackage -AllUsers| Foreach {Add-AppxPackage -DisableDevelopmentMode -Register",
                    "Reboot the system and see if the issue persists."
                    "Reset your OS to factory default settings by doing the following: Hold the shift button while clicking restart, click advanced options when the menu appears, click reset this pc. Follow the onscreen instruction.",
                ]
            },
            {
                "code": "0x0000001E: KMODE_EXCEPTION_NOT_HANDLED",
                "solutions": [
                    "Update or rollback your network and display drivers using device manager",
                    "Run a memory diagnostic using the Windows memory diagnostic tool",
                    "Run a malware scan using Windows defender or your anti virus of choice. I reccomend using MalwareBytes",
                    
                    
                ]
                
            },
            {
                
            }
        ]
    }
]

expert_system = ExpertSystem(rules)

while True:  # This is our main menu loop, stops the menu from closing after the user has made a choice
    # List of problems menu
    print("\nWelcome to the Technical support expert system by Brunaldo Cimo and Hishaam Mehmood!") # Welcome message
    print("--------------------------------------------------------------------------------------")
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