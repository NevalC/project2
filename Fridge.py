class Fridge:
    def __init__(self) -> None:
        '''
        Attributes created.
        '''
        self.__fridge_items: Dict[str, int] = {
            'banana' : 4,
            'strawberry' : 8,
            'chicken' : 1
        }
        self.__adjacency: bool = False

    def open(self) -> None:
        '''
        Function to open the fridge.
        '''
        if self.__adjacency == False:    # Open the fridge
            self.__adjacency: bool = True
            self.check()

    def take(self, lineEdit: str, number: int) -> None:                      # Take items out of fridge (item, num)
        '''
        Function to take items from the fridge.
        :param lineEdit: Parameter that takes the lineEdit input from gui2.
        :param number: Parameter that takes the comboBox input from gui2.
        '''
        self.__lineEdit: str = lineEdit.lower()
        self.validity: bool = self.only_str(self.__lineEdit)
        if self.validity == True:                                            # checking for non-strings
            print(f'\n{self.__lineEdit} contains non-strings! Please enter a string.')
        else:
            self.__number: int = int(number)
            if self.__lineEdit == '':
                print('\nYou did not enter an item to take!')
                self.__adjacency: bool = False
            if type(self.__lineEdit) != str:
                print('\nYou did not enter an item to take!')
                self.__adjacency: bool = False
            if self.__number == 0:
                print(f'\nYou tried taking zero {self.__lineEdit}!')
                self.__adjacency: bool = False
            else:
                self.open()
                if self.__adjacency == True:
                    if self.__lineEdit not in self.__fridge_items:                            # checks for existing item
                        print(f'\n{self.__lineEdit} was not found. Spelling mistake?')
                    else:
                        self.__retrieved_number: int = self.__fridge_items[self.__lineEdit]   # gets value of key item
                        self.__new_number: int = self.__number - self.__retrieved_number      # gets number according to inputted number and value of key
                        if self.__new_number >= 0 and self.__lineEdit in self.__fridge_items: # removes all of item from dictionary if none exist
                            self.__removed_item: str = self.__fridge_items.pop(self.__lineEdit)
                            print(f'\n{self.__removed_item} {self.__lineEdit} were removed! Zero {self.__lineEdit} remain!')
                            self.check()
                        else:                                                                 # records items according to remaining number
                            self.__new_number = abs(self.__new_number)
                            self.__fridge_items[self.__lineEdit] = self.__new_number
                            if self.__new_number == 1:
                                print(f'\n{self.__new_number} {self.__lineEdit} remains!')
                                self.check()
                            else:
                                print(f'\n{self.__new_number} {self.__lineEdit} remain!')
                                self.check()

    def deposit(self, lineEdit: str, number: int) -> None:                     # deposit items in the fridge (item, num)
        '''
        Function to add items to the fridge.
        :param lineEdit: Parameter that takes the lineEdit_2 input from gui2.
        :param number: Parameter that takes the comboBox_2 input from gui2.
        '''
        self.__lineEdit: str = lineEdit.lower()
        self.validity: bool = self.only_str(self.__lineEdit)
        if self.validity == True:                                        # checking for non-strings
            print(f'\n{self.__lineEdit} contains non-strings! Please enter a string.')
        else:
            self.__number: int = int(number)
            if self.__lineEdit == '':                                    # blank lineEdit
                print('\nYou did not enter an item to deposit!')
                self.__adjacency: bool = False
            if type(self.__lineEdit) != str:                             # lineEdit is not a string value
                print('\nYou did not enter an item to deposit!')
                self.__adjacency: bool = False
            if self.__number == 0:                                       # if number is equal to 0
                print(f'\nYou tried adding zero {self.__lineEdit}!')
                self.__adjacency: bool = False
            else:
                self.open()
                if self.__adjacency == True:
                    if self.__lineEdit.lower() in self.__fridge_items:                   # adding to existing item
                        self.__retrieved_number: int = self.__fridge_items[self.__lineEdit]
                        self.__new_number: int = self.__retrieved_number + self.__number
                        if self.__new_number > 8:
                            print(f'\nYou tried adding too many {self.__lineEdit}. The value must be less than or equal to 8.')
                        else:
                            self.__fridge_items[self.__lineEdit] = self.__new_number
                            print(f'\nAdded {self.__number} {self.__lineEdit}!')
                            self.check()
                    elif len(self.__fridge_items) < 5:                                   # reassuring that the item can be added to the dictionary
                        self.__fridge_items[self.__lineEdit] = self.__number
                        print(f'\nAdded {self.__number} {self.__lineEdit}!')
                        self.check()
                    elif len(self.__fridge_items) == 4:                                  # last slot taken in dictionary
                        self.__fridge_items[self.__lineEdit] = self.__number
                        print(f'\nAdded {self.__number} {self.__lineEdit}!')
                        print('The fridge is now full!')
                        self.check()
                        print('If you would like to add more you must remove some items first!')
                    else:                                                                # dictionary is full
                        print('\nThe fridge is at capacity! Try taking items out!')


    def check(self) -> None:                     # Check inside of fridge
        '''
        Function to print contents of fridge.
        '''
        self.open()
        if self.__adjacency == True:
            print('\nContents:\n')
            try:
                if len(self.__fridge_items) == 0:
                    raise IndexError
                else:
                    print(self.__fridge_items)
            except IndexError:
                print('\n\nThere is nothing in the fridge!!')

    def only_str(self, input) -> bool:
        '''
        Function returns a boolean value according to whether a non-string exists.
        :param input: Input from lineEdit.
        :return: Returns a boolean value in search of digits.
        '''
        for char in input:
            if char.isdigit():
                return True
        return False
