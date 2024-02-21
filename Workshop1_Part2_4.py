#4.Write a Python program that prompts the user to enter a UTF-8 value between 32 and 126,
#and displays the corresponding character.
# Prompt the user to enter a UTF-8 value between 32 and 126
utf=int(input("Enter a UTF-8 value between 32 and 126"))
if 32<=utf<=126:
    char=chr(utf)
    print(f"The corresponding character is: {char}")
else:
    print("Enter a valid UTF-8 value between 32 and 126.")
