print("Welcome to the CO652 Knwoledge based systems collaborative project expert system") 
print(". . . ")
print(". . . . . . ")
print(". . . . . . . . . ")
print(". . . . . . . . . . . . . . . . . .")
print(". . . . . . . . . . . . . . . . . . . . . . .")
print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ")
print("What type of technical issue are you facing with to start with ?")
print("1. Blue Screen of Death (BSOD)\n2. Crashes or Freezing\n3. Display Errors\n4. Slow PC/Performance Issues\n5. Network Issues\n6. Other")
choice = int(input("Enter the number corresponding to your issue: "))

if choice == 1:
    print("Have you got the error code of the blue screen of death that is diplayed typically on the monitor (Y/N)")
    error_code = input("What is the blue screen of death error code appearing on screen? 'N': ").strip()

BSOD_CODES = {
    "0x0000000A": "IRQL_NOT_LESS_OR_EQUAL",
    "0x0000000D": "EXCEPTION_DOUBLE_FAULT",
    "0x0000001E": "KMODE_EXCEPTION_NOT_HANDLED",
    # fill all error codes we gonna explain -- not all thousands xD --
}

error_code = input("Enter the BSOD error code (e.g., 0x0000000A): ").strip()
if error_code in BSOD_CODES:
    print(f"Description: {BSOD_CODES[error_code]}")
    print(" instructions instructions instructions")
else:
    print("Error not recognised or existing on dataset of system please search the code on :" "('https://www.hp.com/us-en/shop/tech-takes/how-to-fix-blue-screen-of-death') and consult with your IT technician")







# test test 















