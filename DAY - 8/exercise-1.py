# Take user marks from user within 0 to 50
# If user enter outside [0-50] raise Error InvalidMarks using Custom Exception
# Give chance to the user till, he/she entered valid marks


#Chatgpt version hehe (long version)
# Custom Exception Class
# Custom Exception Class
# class InvalidMarksError(Exception):
#     pass

# while True:
#     try:
#         subjects = ["Math", "Science", "English"]
#         marks_list = []

#         for subject in subjects:
#             while True:
#                 try:
#                     marks = float(input(f"Enter marks for {subject} (0 - 50): "))

#                     # Check range
#                     if marks < 0 or marks > 50:
#                         raise InvalidMarksError("Marks must be between 0 and 50.")

#                     marks_list.append(marks)
#                     break  # exit this subject’s loop if valid

#                 except InvalidMarksError as ime:
#                     print("Error:", ime)
#                 except ValueError:
#                     print("Error: Please enter a number only.")
#                 except Exception as ex:
#                     print("Unexpected Error:", ex)

#         print("\nAll marks entered successfully!")
#         print("Your Marks:", marks_list)
#         print("🎉 Congratulations! You’ve entered all valid marks! 🎉")

#     except ZeroDivisionError as ze:
#         print("Division by 0 not allowed")
#     except ValueError as ve:
#         print("Error in values", ve)
#     except Exception as ex:
#         print("Error!!!", ex)

#     choice = input("Do you wanna continue? (press 'y' to continue): \t").lower()
#     if choice != "y":
#         print("Bye 👋")
#         break


#Chatgpt version hehe (short version)
class InvalidMarksError(Exception): pass

while True:
    try:
        subs = ["Math", "Science", "English"]
        marks = []
        for s in subs:
            while True:
                try:
                    m = float(input(f"Enter {s} marks (0-50): "))
                    if not 0 <= m <= 50: raise InvalidMarksError
                    marks.append(m); break
                except (ValueError, InvalidMarksError):
                    print("Invalid! Enter number 0-50.")
        print("Marks:", marks, "\n🎉 Congratulations! You've passed. 🎉")
    except Exception as ex:
        print("Error!", ex)
    if input("Continue? (y): ").lower() != "y":
        print("Bye"); break