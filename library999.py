# book = " "
#
# while True:
#     print("\nУправління бібліотекою")
#     print("1. Додати книгу")
#     print("2. Видалити книгу")
#     print("3. Переглянути книгу")
#     print("4. Очистити книгу")
#     print("5. Вийти")
#
#     choice = input("Виберіть опцію (1-5): ")
#
#     if choice == '1':
#         book = input("Введіть назву книги: ")
#
#     elif choice == '2':
#         book = None
#         print("Книга видалена.")
#
#     elif choice == '3':
#         if book:
#             print(f"Поточна книга в бібліотеці: {book}")
#         else:
#             print("В бібліотеці немає книги.")
#
#     elif choice == '4':
#         book = None
#         print("Книга очищена з бібліотеки.")
#
#     elif choice == '5':
#         print("Вихід з програми.")
#         break
#
#     else:
#         print("Невірний вибір. Будь ласка, оберіть дійсну опцію.")
#
#
#
#
#
#
#
#
#
#
class Pet:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def info(self):
        print(f"Мій улюбленець - це {self.type}, його звати {self.name} і йому {self.age} років.")

    # def celebrate_birthday(self):
    #     self.age += 1
    #     print(f"З Днем народження, {self.name}! Тепер тобі {self.age} років!")

# #
my_pet = Pet("Бобик", "собака", 5)
my_pet2 = Pet("Шарік", "собака", 2)
#
#
my_pet.info()
my_pet2.info()
# my_pet.celebrate_birthday()


# # my_pet.info()
#
#
# # Initialize empty books
# book1 = ""
# book2 = ""
# book3 = ""
#
# while True:
#     print("\nLibrary List Management")
#     print("1. Add book")
#     print("2. Remove book")
#     print("3. View books")
#     print("4. Clear all books")
#     print("5. Exit")
#
#     choice = input("Choose an option (1-5): ")
#
#     if choice == "1":
#         position = input("Enter position (1, 2, or 3): ")
#         if position == "1":
#             book1 = input("Enter book name: ")
#         elif position == "2":
#             book2 = input("Enter book name: ")
#         elif position == "3":
#             book3 = input("Enter book name: ")
#         else:
#             print("Invalid position. Please choose 1, 2, or 3.")
#
#     elif choice == "2":
#         position = input("Enter position to remove (1, 2, or 3): ")
#         if position == "1":
#             book1 = ""
#             print("Book at position 1 removed.")
#         elif position == "2":
#             book2 = ""
#             print("Book at position 2 removed.")
#         elif position == "3":
#             book3 = ""
#             print("Book at position 3 removed.")
#         else:
#             print("Invalid position. Please choose 1, 2, or 3.")
#
#     elif choice == "3":
#         print("\nCurrent Books in Library:")
#         if book1:
#             print(f"Position 1: {book1}")
#         else:
#             print("Position 1: [Empty]")
#         if book2:
#             print(f"Position 2: {book2}")
#         else:
#             print("Position 2: [Empty]")
#         if book3:
#             print(f"Position 3: {book3}")
#         else:
#             print("Position 3: [Empty]")
#
#     elif choice == "4":
#         book1 = ""
#         book2 = ""
#         book3 = ""
#         print("All books cleared from the Library.")
#
#     elif choice == "5":
#         print("Exiting the program.")
#         break
#
#     else:
#         print("Invalid selection. Please select a correct option (1-5).")


# y = input(("Привіт! Давай зіграємо у гру на перевірку парнлсті числа"))
#
# if y == "Давай":
#     print("Чудово, тоді почнемо")
# elif y == "давай":
#     print("Чудово, тоді почнемо")
# elif y == "Так":
#     print("Чудово, тоді почнемо")
# elif y == "так":
#     print("Чудово, тоді почнемо")
# else:
#     print("Всеодно давай зіграємо")
#
# while True:
#     num = int(input(("Введіть число:")))
#     if num % 2 == 0:
#         print("Молодець! Число є парним")
#         break
#     else:
#         print("Число не є парним")