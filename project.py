import getpass, random, os, csv, datetime, sys, cowsay, re, time

class Story():
  title = None
  plot = None
  characters = None

  def __init__(self, title, plot, characters):
    self.title = title
    self.plot = plot
    self.characters = characters

  def print(self):
    print(f"\n Title: {self.title}\n Plot: {self.plot}\n Character(s): {self.characters}\n")

class Person():
  name = None
  age = None
  looks = None
  clothing = None
  backstory = None

  def __init__(self, name, age, looks, clothing, backstory):
    self.name = name
    self.age = age
    self.looks = looks
    self.clothing = clothing
    self.backstory = backstory

  def print(self):
    print(f"\n Character Description\n Name: {self.name}\n Age: {self.age}\n Looks: {self.looks}\n Clothing: {self.clothing}\n Backstory: {self.backstory}\n")


def main():
    print("=== WELCOME! ===")
    print("Loading...")
    time.sleep(1)
    os.system("clear")
    #go to login menu
    login_menu()
    #once logged in, clear screen and run the main menu
    os.system("clear")
    print("===== WELCOME! =====")
    print()
    print(f"Today is {datetime.date.today()}")
    print()
    print("What would you like to do today?")
    print()
    print(" 1. Get a Genre")
    print(" 2. Create a Story")
    print(" 3. Create a Character")
    print(" 4. Exit")
    print()
    while True:
        try:
            menu = get_number()
        except ValueError:
            print("Error. Try again.")

        if menu == 1:
            genre = get_genre()
            print(f"Your Genre is...... {genre}")
            print()
        elif menu == 2:
            get_story()
        elif menu == 3:
            get_characters()
        elif menu == 4:
            cowsay.cow("Goodbye!")
            sys.exit("Thanks for using Author Helper!")


def get_number():
    menu = int(input("Enter a number > "))
    return menu


#get a genre from random list
def get_genre():
    genres = ["Fantasy", "Science Fiction", "Mystery", "Action", "Horror", "Thriller", "Historical", "Romance", "LGBTQ+", "Erotica", "Childrens", "Travel", "True Crime", "Humour", "Fictional Crime", "Non Fiction"]
    return random.choice(genres)

#make up a story using the prompts
def get_story():
    title = input("Title: ")
    plot = input("Plot: ")
    character = input("Character: ")
    story = Story(title, plot, character)
    print()
    print(" ======== ")
    story.print()
    print(" ======== ")
    print()


#get some characters for the story
def get_characters():
    quantity = int(input("How many characters? "))
    print()
    for _ in range(quantity):
        name = input("Name: ")
        age = input("Age: ")
        looks = input("Looks: ")
        clothing = input("Clothing: ")
        backstory = input("Backstory: ")
        print()
        person = Person(name,age,looks,clothing,backstory)
        print(" ======== ")
        person.print()
        print(" ======== ")
        print()


#first login menu, add a user, or login
def login_menu():
    print()
    print("###################")
    print("   AUTHOR HELPER")
    print("###################")
    print()
    print("1. Add User")
    print("2. Login")
    print("3. Close")
    print()
    try:
        menu = int(input("Enter a number > "))
    except ValueError:
        print("Error. Try again.")

    if menu == 1:
        add_user()
    elif menu == 2:
        login()
    elif menu == 3:
        cowsay.cow("Goodbye!")
        sys.exit("Thanks for using Author Helper Today!")

#add a user, adds the username and password to a csv file
def add_user():
    print()
    print("Username must begin with a capital letter and be eight characters long | Letters and Numbers ONLY!")
    print()
    username = username_check(input("Username: "))
    password = input("Enter a password: ")
    print()
    print("User Successfully Added")
    with open("cs50p project/users.csv", 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["username", "password"])
        writer.writerow({"username": username, "password": password})
    back = input("Press Y to return!").lower()
    if back == "y":
        login_menu()

#login in the user
def login():
    print()
        #open the csv file with the usernames and passwords
    with open("cs50p project/users.csv", "r+") as file:
        reader = csv.DictReader(file)
        #open a list
        user = []
        #for each row in the csv
        for row in reader:
            #write a dictionary of values to the list
            user.append({"username": row["username"], "password": row["password"]})

        #make a list of all of the values
        list_of_all_values = [value for elem in user
                      for value in elem.values()]

        print("===== LOGIN =====")
        print()
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        #if the username and password entered appear in the list then access else exit.
        if username in list_of_all_values and password in list_of_all_values:
            return
        else:
            sys.exit("Error, username or password not found!")


def username_check(username):
    if re.search(r"^[A-Z]{1}[a-z0-9]{7}$", username, re.IGNORECASE):
        return username
    else:
        print("Invalid. Try Again!")
        time.sleep(1)
        login_menu()

if __name__ == "__main__":
    main()