class Animal: # parent class (Animal)
    def __init__(self, name, animal_id, date_rescued, location,
                 microchipped, favourite_food, vaccinated, neutered): # animal parameters

        self.name = name
        self.animal_id = animal_id
        self.date_rescued = date_rescued
        self.location = location
        self.microchipped = microchipped
        self.favourite_food = favourite_food
        self.__vaccinated = vaccinated # private variable
        self.__neutered = neutered # private variable

    def get_vaccinated(self): # getter for vaccinated variable
        return self.__vaccinated

    def get_neutered(self): # getter for neutered variable
        return self.__neutered

    def set_vaccinated(self, value): # setter for vaccinated variable
        self.__vaccinated = value

    def set_neutered(self, value): # setter for neutered variable
        self.__neutered = value

class Dog(Animal): # dog subclass
    def __init__(self, name, animal_id, date_rescued, location,
                 microchipped, favourite_food, vaccinated, neutered,
                 bark_type):

        super().__init__(name, animal_id, date_rescued, location,
                         microchipped, favourite_food, vaccinated, neutered) # inherited parameters

        self.bark_type = bark_type # exclusive parameter for dog class




class Cat(Animal): #subclass
    def __init__(self, name, animal_id, date_rescued, location,
                 microchipped, favourite_food, vaccinated, neutered,
                 meow_type):

        super().__init__(name, animal_id, date_rescued, location,
                         microchipped, favourite_food, vaccinated, neutered) # inherited parameters

        self.meow_type = meow_type # exclusive parameter for cat class



rescued_animals = [] # rescued animals array



def save_to_file(): # saving the data to a file
    try:
        with open("rescued_animals.txt", "w") as file:
            for animal in rescued_animals:

                if hasattr(animal, "bark_type"): # hasattr from chatgpt, checks if an object has a specified attribute
                    file.write(
                        f"Dog,{animal.name},{animal.animal_id},{animal.date_rescued}," # does the dog have all the nessesary attributes, add them to file
                        f"{animal.location},{animal.microchipped},"
                        f"{animal.favourite_food},{animal.get_vaccinated()},"
                        f"{animal.get_neutered()},{animal.bark_type}\n"
                    )
                elif hasattr(animal, "meow_type"):
                    file.write(
                        f"Cat,{animal.name},{animal.animal_id},{animal.date_rescued}," # does the cat have all the nessesary attributes, add them to file
                        f"{animal.location},{animal.microchipped},"
                        f"{animal.favourite_food},{animal.get_vaccinated()},"
                        f"{animal.get_neutered()},{animal.meow_type}\n"
                    )
    except IOError: # except the file doesnt exist or disc is full and inputs cant be made
        print("Error saving file.\n")

# choice functions

def yes_no_input(question): # yes or no function, can add a choice of 1 or 2 to any question
    while True:
        try:
            print(question)
            print("1. Yes")
            print("2. No")
            choice = int(input("Choose 1 or 2: "))

            if choice == 1:
                return True
            elif choice == 2:
                return False
            else:
                print("Enter 1 or 2.\n")

        except ValueError:
            print("Invalid input. Enter a number.\n") # exeption handling


def location_input(): # adds a choice, 1 or 2, for household types
    while True:
        try:
            print("Rescue location:")
            print("1. Stray")
            print("2. Unstable household")
            choice = int(input("Choose 1 or 2: "))

            if choice in [1, 2]:
                return choice
            else:
                print("Enter 1 or 2.\n")

        except ValueError:
            print("Invalid input. Enter a number.\n")



def add_animal(): # function for adding animals
    try:
        print("Animal type:")
        print("1. Dog")
        print("2. Cat")
        animal_choice = int(input("Choose 1 or 2: "))

        name = input("Name: ")
        animal_id = input("Animal ID: ")
        date = input("Date rescued (dd/mm/yy): ")
        location = location_input()
        micro = yes_no_input("Microchipped?")
        food = input("Favourite food: ")
        vaccinated = yes_no_input("Vaccinated?")
        neutered = yes_no_input("Neutered?")

        if animal_choice == 1:
            bark_type = input("Bark type (loud/quiet): ")
            new_animal = Dog(name, animal_id, date, location,
                             micro, food, vaccinated, neutered,
                             bark_type)

        elif animal_choice == 2:
            meow_type = input("Meow type (high pitched/low pitched): ")
            new_animal = Cat(name, animal_id, date, location,
                             micro, food, vaccinated, neutered,
                             meow_type)
        else:
            print("Invalid choice.\n")
            return

        rescued_animals.append(new_animal)
        save_to_file() # save to file method
        print("Animal added.\n")

    except ValueError: # error handling
        print("Invalid input.\n")



def view_animals(): # view animal function
    if not rescued_animals:
        print("No animals recorded.\n")
        return
# pretty table
    print("\n" + "-" * 120)
    print(f"{'Type':<6} | {'ID':<8} | {'Name':<12} | {'Rescued':<12} | "
          f"{'Location':<8} | {'Micro':<6} | {'Food':<12} | "
          f"{'Vacc':<5} | {'Neut':<5} | {'Sound':<12}")
    print("-" * 120)

    for animal in rescued_animals:

        animal_type = "Dog" if hasattr(animal, "bark_type") else "Cat"
        sound = animal.bark_type if animal_type == "Dog" else animal.meow_type

        location_text = "Stray" if animal.location == 1 else "Home"
        micro_text = "Yes" if animal.microchipped else "No"
        vac_text = "Yes" if animal.get_vaccinated() else "No"
        neut_text = "Yes" if animal.get_neutered() else "No"

        print(f"{animal_type:<6} | "
              f"{animal.animal_id:<8} | "
              f"{animal.name:<12} | "
              f"{animal.date_rescued:<12} | "
              f"{location_text:<8} | "
              f"{micro_text:<6} | "
              f"{animal.favourite_food:<12} | "
              f"{vac_text:<5} | "
              f"{neut_text:<5} | "
              f"{sound:<12}")

    print("-" * 120 + "\n")


def edit_animal(): # funtion for editing animals
    search_id = input("Enter animal ID to edit: ") # id search to edit

    for animal in rescued_animals:
        if animal.animal_id == search_id:

            animal.name = input("New name: ")
            animal.date_rescued = input("New date rescued (dd/mm/yy: ")
            animal.location = location_input()
            animal.microchipped = yes_no_input("Microchipped?")
            animal.favourite_food = input("Favourite food: ")
            animal.set_vaccinated(yes_no_input("Vaccinated?"))
            animal.set_neutered(yes_no_input("Neutered?"))

            if hasattr(animal, "bark_type"):
                animal.bark_type = input("New bark type: ")
            elif hasattr(animal, "meow_type"):
                animal.meow_type = input("New meow type: ")

            save_to_file()
            print("Animal updated.\n")
            return

    print("Animal not found.\n")



def delete_animal(): # funtion to delete animal
    search_id = input("Enter animal ID to delete: ") # id search to delete

    for animal in rescued_animals:
        if animal.animal_id == search_id:
            rescued_animals.remove(animal)
            save_to_file()
            print("Animal deleted.\n")
            return

    print("Animal not found.\n")



def menu(): # Menu UI
    while True:
        try:
            print("Animal Adoption System \nUse this to keep track of the animals under the care of your adoption centre \n")
            print("1. Add animal")
            print("2. View animals")
            print("3. Edit animal")
            print("4. Delete animal")
            print("5. Exit")

            choice = int(input("Choose option: "))

            if choice == 1:
                add_animal()
            elif choice == 2:
                view_animals()
            elif choice == 3:
                edit_animal()
            elif choice == 4:
                delete_animal()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid option.\n")

        except ValueError:
            print("Invalid input. Enter a number.\n")


menu() # start the program by running the menu function
