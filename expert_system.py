# ==========================================
# PC Tech Support Expert System by Bruno Cimo and Hishaam Mehmood 
# ==========================================
import sys
from knowledge_base import *


# -----------------------------
#  BACKWARD CHAINING FUNCTION -NETWORK ISSUES
# -----------------------------
def backward_chaining_network():
    
    print("\nLet's resolve your network issues...")
    
    problem = input("\nWhat is the network issue you're facing? \nOptions: "
                    "\n1) Weak Wi-Fi signal"
                    "\n2) High latency"
                    "\n3) Unable to access a website"
                    "\n4) Slow download speeds"
                    "\n5) Inconsistent connection"
                    "\n6) Missing Wi-Fi option \nEnter the number of your issue:").strip()
    
    if problem == "1":  # Weak Wi-Fi signal
        if input("\nAre you far from the router? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Move closer to the router or use an Ethernet cable.")
        elif input("\nAre there walls or obstacles blocking the signal? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Remove obstacles or place the router in a central, open area.")
        elif input("\nIs the router outdated or damaged? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Consider upgrading your router.")
        else:
            print("\n Solution: Reset your router and check for firmware updates.")

    elif problem == "2":  # High latency
        if input("\nAre you connected to a server in a far region? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Switch to a server region closer to you.")
        elif input("\nIs your internet connection speed low? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Contact your ISP to upgrade your plan or troubleshoot slow speeds.")
        elif input("\nAre background applications consuming bandwidth? (yes/no): ").strip().lower() == "yes":
            print("\nSolution: Close unnecessary applications and downloads.")
        else:
            print("\n Solution: Restart your router and prioritize devices on your network.")

    elif problem == "3":  # Unable to access a website
        if input("\nIs the website blocked by a firewall? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Configure your firewall to whitelist the website.")
        elif input("\nIs the website blocked in your region? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Use a VPN to access the website.")
        elif input("\nIs your DNS server misconfigured? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Switch to a public DNS (e.g., Google DNS: 8.8.8.8).")
        else:
            print("\n Solution: Clear your browser cache or try accessing the website from a different device.")

    elif problem == "4":  # Slow download speeds
        if input("\nAre you using a 2.4GHz Wi-Fi band? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Switch to the 5GHz band or use an Ethernet cable.")
        elif input("\nAre there too many devices on your network? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Disconnect unused devices to free up bandwidth.")
        elif input("\nIs your internet plan sufficient for your needs? (yes/no): ").strip().lower() == "no":
            print("\n Solution: Upgrade to a higher-speed internet plan.")
        else:
            print("\n Solution: Restart your router and avoid peak usage times.")

    elif problem == "5":  # Inconsistent connection
        if input("\nHave you tried flushing your DNS cache? (yes/no): ").strip().lower() == "no":
            print("\nSolution: Open the command prompt and enter 'ipconfig /flushdns'.")
        elif input("\nIs your router overheating or old? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Replace the router or ensure proper ventilation.")
        elif input("\nIs your ISP experiencing outages? (yes/no): ").strip().lower() == "yes":
            print("\nSolution: Contact your ISP for updates on the issue.")
        else:
            print("\nSolution: Test your connection with another device or network.")

    elif problem == "6":  # Missing Wi-Fi option
        if input("\nIs your network driver up to date? (yes/no): ").strip().lower() == "no":
            print("\nSolution: Open Device Manager, reinstall your network driver, and reboot.")
        elif input("\nIs your Wi-Fi card properly installed? (yes/no): ").strip().lower() == "no":
            print("\nSolution: Ensure your Wi-Fi card is correctly connected to the motherboard.")
        elif input("\nIs airplane mode enabled? (yes/no): ").strip().lower() == "yes":
            print("\nSolution: Disable airplane mode in your system settings.")
        else:
            print("\nSolution: Check your BIOS settings to ensure the Wi-Fi card is enabled.")

    else:
        print("\nNo solution found. Consider contacting your Internet Service Provider (ISP).")









# -----------------------------
# FRAME-BASED REPRESENTATION 
# -----------------------------


class Motherboard:
    """Base class representing a motherboard brand and its beep codes."""
    def __init__(self, brand):
        self.brand = brand
        self.beep_codes = {}  # Dictionary to store beep codes and their meanings

    def add_beep_code(self, code, meaning):
        """Adds beep code error information to the motherboard class (stored in lowercase for case-insensitivity)."""
        self.beep_codes[code.lower()] = meaning  # Store beep codes in lowercase for case-insensitive matching

    def diagnose_beep_code(self, code):
        """Checks the beep code against the stored rules and returns the diagnosis (case insensitive)."""
        code_lower = code.lower()  # Convert user input to lowercase
        if code_lower in self.beep_codes:
            return f"Detected Issue for {self.brand}: {self.beep_codes[code_lower]}"
        return "Beep code not recognized. Check the manufacturer’s manual."







# -----------------------------
# FORWARD CHAINING FUNCTION (Rule-Based System)
# -----------------------------
def forward_chaining(category, key):
    """Matches known error conditions with solutions using forward chaining and interactive troubleshooting."""
    
    # Define category rule sets
    rule_sets = {
        "BSOD": bsod_errors,
        "GPU": gpu_issues,
        "DirectX": directx_errors,
        "DLL Errors": dll_crashes,       
        "Malware": malware_issues,
        "Display": display_errors
    }
    
    # Check if the error exists in the selected category
    if category in rule_sets and key in rule_sets[category]:
        error_data = rule_sets[category][key]

        #  Display the detected error
        print(f"\nDetected {category} Error: {key} - {error_data['error_name']}")

        #  Display consideration message if available
        if "consideration" in error_data:
            print(f"\nConsideration: {error_data['consideration']}")

        #  Loop through solutions step-by-step
        solutions = error_data["solutions"]
        for i, solution in enumerate(solutions, start=1):
            print(f"\nSuggested Solution {i}: {solution}")
            
            #  Ask the user if the solution worked
            response = input("\nDid this solution work? (yes/no): ").strip().lower()

            # Ensure valid input
            while response not in ["yes", "no"]:
                response = input("Invalid input! Please enter 'yes' or 'no': ").strip().lower()

            #  If the solution worked, stop troubleshooting
            if response == "yes":
                print("\n Thank you for using our system! Your issue has been resolved.")
                return  

        #  If no solution worked, suggest contacting support
        print("\nNo solution worked, consider seeking further assistance.")
    else:
        print("\nError not found. Please check online resources.")








# -----------------------------
# BACKWARD CHAINING FUNCTION  
# -----------------------------
def backward_chaining_beep_code():
    """Asks the user to input beep code details and applies backward chaining to diagnose the issue."""
    motherboards = initialize_motherboard_data()
    
    print("\nMotherboard Beep Code Troubleshooting")
    print("Supported Brands: IBM, Dell, Macintosh")
    
    brand = input("\nEnter your motherboard brand: ").strip().capitalize()  # Fix: Normalize input case

    # Fix: Allow case-insensitive matching for brands
    brand_mapping = {key.lower(): key for key in motherboards.keys()}  # Create lowercase mapping
    brand_lower = brand.lower()

    if brand_lower not in brand_mapping:
        print("Unsupported motherboard brand. Please check the manufacturer’s manual.")
        return

    selected_brand = brand_mapping[brand_lower]  # Get correct key format for dictionary lookup

    beep_code = input("Enter the beep code pattern (e.g., '1x short', '3x long', 'continuous beep'): ").strip().lower()
    diagnosis = motherboards[selected_brand].diagnose_beep_code(beep_code)

    print(f"\n{diagnosis}")


def backward_chaining(problem, knowledge_base):
    """Inference Engine: Applies Backward Chaining to diagnose the issue."""
    print(f"\n Diagnosing {problem}...")

    for solution, condition in knowledge_base.items():
        response = input(f"\nDid you? {condition.replace('_', ' ').capitalize()}? (yes/no): ").strip().lower()

        while response not in ["yes", "no"]:
            response = input("Invalid input! Please enter 'yes' or 'no': ").strip().lower()

        if response == "no":
            print(f"\n Solution: {condition}")
            return  # Stop once a solution is found

    print("\n No clear cause found. Consider hardware upgrades or consulting a specialist.")

    

# -----------------------------
# GENERAL TROUBLESHOOTING WIZARD 
# -----------------------------

def general_troubleshooting_wizard():
    """Allows the user to select between Low FPS Troubleshooting and Slow PC Performance Troubleshooting."""
    print("\n General Troubleshooting Wizard")
    print("1. Troubleshoot Low FPS in Games")
    print("2. Troubleshoot Lag / Slow PC Performance")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":
        backward_chaining("Low FPS in Games", low_fps_knowledge_base)
    elif choice == "2":
        backward_chaining("Lag / Slow PC Performance", slow_pc_knowledge_base)
    else:
        print("Invalid selection. Returning to the main menu.")

















          

# -----------------------------
#  MAIN FUNCTION MENU (User Interaction)
# -----------------------------
def main(): 
    print("\nWelcome to the PC Tech Support Expert System by Bruno Cimo and Hishaam Mehmood!")
    print("\nSelect an issue:")
    print("1. BSOD Error")
    print("2. GPU Issues")
    print("3. Display Errors")
    print("4. Motherboard Beep Codes")
    print("5. Crashes & DLL Errors")
    print("6. DirectX Compatibility Issues")
    print("7. Network Issues")
    print("8. General Troubleshooting Wizard")
    print("9. Malware & Virus Issues")

    choice = input("\nEnter your choice (1-9): ").strip()

    if choice == "1":
        code = input("Enter the BSOD error code: ").strip()
        print(forward_chaining("BSOD", code))
    elif choice == "2":
        print("\n GPU Troubleshooting: GPU Driver Timeout")
        forward_chaining("GPU", "gpu driver timeout")
    elif choice == "3":
        print("\nDisplay Troubleshooting:")
        (forward_chaining("Display", "hdmi not detected"))
    elif choice == "4":
        backward_chaining_beep_code()
    elif choice == "5":
        print("\nDLL or Game Crash Troubleshooting:")
        print(forward_chaining("DLL Errors", "User32.dll crash"))
        
    elif choice == "6":
        print("\nDirectX Compatibility Troubleshooting:")

        # Automatically display DirectX troubleshooting solutions
        forward_chaining("DirectX", "directx compatibility issue")

    elif choice == "7":
        print("\nNetwork Troubleshooting:")
        backward_chaining_network()
        
    if choice == "8":
        (general_troubleshooting_wizard())
    elif choice == "9":
        print("\nMalware & Virus Troubleshooting:")
        malware_type = input("Please enter the malware type: ").strip()
        print(forward_chaining("Malware", malware_type))
    else:
        print("Invalid selection. Returning to main menu.")

# Runs the expert system
if __name__ == "__main__":
    main()
