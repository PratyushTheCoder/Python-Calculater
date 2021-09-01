import os
import pyttsx3  # IMPORTANT! pip install pyttsx3 do this in a powershell terminal

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


caclPath = ('C:\\Windows\\System32\\calc.exe')  # Don't Change The Path It Will Always Be The Same In All Computer

speak('Hello I am a calculater, I calculate number for you, Please choose a operration')
speak('For Multiplication Choose 3, for division 4, for addition 1 and for substraction 2')
speak('But if you want to open calculater type "calculater"')

while True:

    speak('Select an operation')
    print('Select an operation')

    n = input("Do you Want to open calculater (y/n): ")

    if n == ('y'):
        os.startfile(caclPath)


    # Function to add two numbers
    def add(num1, num2):
        return num1 + num2


    # Function to subtract two numbers
    def subtract(num1, num2):
        return num1 - num2


    # Function to multiply two numbers
    def multiply(num1, num2):
        return num1 * num2


    # Function to divide two numbers
    def divide(num1, num2):
        return num1 / num2


    print("1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n")

    # Take input from the user
    select = int(input("Select operations form 1, 2, 3, 4, :"))

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))

    elif select == 2:
        print(number_1, "-", number_2, "=",
              subtract(number_1, number_2))

    elif select == 3:
        print(number_1, "X", number_2, "=",
              multiply(number_1, number_2))

    elif select == 4:
        print(number_1, "/", number_2, "=",
              divide(number_1, number_2))

    else:
        print("Invalid input")

    i = input('Do You want to calculate again (y/n)')
    if i == "n":
        break