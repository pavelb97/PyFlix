class Movie():
    def __init__(self, title, director, cast, length, rating=-1):           # Movie details as input
        self.title = str(title)
        self.director = str(director)
        self.cast = str(cast)
        self.length = int(length)
        self.rating = int(rating)

    def __str__(self):
        return ("%s\n%s" % (self.title, self.director))                     # Return basic movie details

    def get_info(self):
        return ("Title: %s; Director: %s; Cast: %s; Running time: %s minutes; Rating: %s/10" %
                (self.title,self.director,self.cast, self.length, self.rating))

class movieNode:                                                            # Node class with movie as input
    def __init__(self, movieDetails, next = None, previous = None):
        self.movieDetails = movieDetails                                   # Movie information as above
        self.nextNode = next                                               # Next node pointer
        self.prevNode = previous                                           # Previous node pointer

class PyFlix(): #DLL class
    # Need to test further past the 19 steps to ensure it is airtight & Ensure it is named and works as specified in the assignment
    def __init__(self):
        self.first_node = None                              # First movie to be added (start of list)
        self.last_node = None                               # Last movie to be added (top of list)
        self.pointer = None                                 # Points to currently selected movie
        self.list_size = 0                                  # Counter - will make return length function easier

    def __str__(self):
        count = 1                                           # Movie counter
        if self.list_size <= 0:                             # if list is empty
            return "There are no movies in your queue."
        text = "Position\tTitle\t\t\t\tDirector\n"          # text to be returned - movie details will be concatenated
        current = self.first_node                           # begin at start of list
        while current is not None:
            if current == None:                             # break statement once end is reached
                break
            if current == self.pointer:                     # Special case: idicate current position
                text += "%s  -->\t\t%s\t\t\t%s\n" % (count, current.movieDetails.title, current.movieDetails.director)
                current = current.nextNode                  # Update node
                count += 1                                  # Update movie count
            else:
                text += "%s\t\t\t%s\t\t\t\t%s\n" % (count, current.movieDetails.title, current.movieDetails.director)
                current = current.nextNode
                count += 1
        return text

    def add_movie(self, movie):
        newNode = movieNode(movie)                          # creates node
        if self.first_node is None:                         # If list is empty:
            self.first_node = newNode                       #   assign as 1st node
        else:
            self.last_node.nextNode = newNode               # Last entered node will be new node
            newNode.prevNode = self.last_node               # new node will point back to previously entered movie
        self.last_node = newNode                            # assigns new node as new last node
        self.pointer = newNode                              # assigns new node as pointer
        self.list_size += 1                                 # grows list count

    def get_current(self):
        if self.first_node is None:                                                 #if list is epmty
            print("There are no movies in your list.")
        else:
             print(self.pointer.movieDetails)                                        # retuns pointer values

    def next_movie(self):
        if self.first_node is None:                                                 # If list is empty
            return "There are no movies in your list."
        elif self.pointer == self.last_node:                                        # If at the end of list:
            self.pointer = self.first_node                                          #   set pointer to start of list
        else:
            self.pointer = self.pointer.nextNode                                    # Sets pointer to next node
            return self.pointer.movieDetails

    def prev_movie(self):
        if self.first_node is None:                                                 # If list is empty
            return "There are no movies in your list."
        elif self.first_node == self.pointer:                                       # If at the start of list
            return "You are at the start of your movie queue."
        else:
            self.pointer = self.pointer.prevNode                                    # Sets pointer to previous node
            return self.pointer.movieDetails

    def reset(self):
        if self.first_node is None:                                                     # If list is empty
            return "There are no movie in your list."
        else:
            self.pointer = self.first_node                                              # Resets pointer to 1st node

    def rate(self):
            while True:
                try:
                    userInput = int(input("Please enter your rating: "))
                except ValueError:                                                      # Ensures valid int input
                    print("That is not a valid rating. Please try again.")
                    continue
                else:
                    if userInput > 10 or userInput < 0:                                 # Ensures valid int
                        print("Please ensure your rating is between 0 and 10.")
                        False
                        continue
                    self.pointer.movieDetails.rating = userInput                        # updates rating
                    break

    def info(self):
        if self.first_node is None:                                             # Returns current movie info
            return "There are no movies in your list."
        else:
            return self.pointer.movieDetails.get_info()

    def remove_current(self):
        if self.first_node is None:                                             # Removes current (pointer)
            return "There are no movie in your list."                           # If list is empty
        elif self.list_size == 1:                                               # If list only has 1 movie
            self.first_node = None
            self.list_size = 0
        elif self.first_node == self.pointer and self.list_size > 1:            # If pointer is also 1st movie
            self.first_node = self.first_node.nextNode
            self.first_node.prevNode = None
            self.pointer = self.first_node
        elif self.last_node == self.pointer:                                    # If pointer is also last movie
            self.last_node = self.last_node.prevNode
            self.last_node.nextNode = None
            self.pointer = self.first_node                                      # As specified, if last movie deleted reset to head
        else:                                                                   # Every other case
            currentNode = self.first_node
            while currentNode.nextNode != self.pointer:                         # Iterate until node before pointer is found
                currentNode = currentNode.nextNode
            currentNode.nextNode = currentNode.nextNode.nextNode                # node.next skips pointer and assign to next node
            currentNode.nextNode.nextNode.prevNode = currentNode                # node after pointer now points back to the node before pointer
            self.pointer = currentNode                                          # update pointer
        self.list_size -= 1

    def length(self):
        return self.list_size                                                # Returns List size

    def search(self, word):
        if type(word) != type(str):
            while True:
                word = input("Invalid input. Please enter your search term again: ")
                if type(word) == type("h"):
                    break

        if self.first_node is None:
            return None
        current = self.first_node
        while current is not None:
            if current == None:
                print("No matching movie")
                break
            else:
                if word.lower() in (current.movieDetails.title).lower() or word.lower() in (current.movieDetails.director).lower():
                    self.pointer = current
                    print(self.pointer.movieDetails.get_info())
                    return
                elif word.lower() in (current.movieDetails.cast).lower():
                    self.pointer = current
                    print(self.pointer.movieDetails.get_info())
                    return
            current = current.nextNode
        print("No matching movie")

if __name__ == "__main__":



    # testing as specified in assignment brief
    PyFlixList = PyFlix()                                                       # I
    testMovie = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)
    PyFlixList.add_movie(testMovie)                                             # II
    testMovie2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
    PyFlixList.add_movie(testMovie2)                                            # III
    testMovie3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)
    PyFlixList.add_movie(testMovie3)                                            # IV

    print(PyFlixList)                                                           # V
    PyFlixList.next_movie()                                                     # VI
    print(PyFlixList.info())                                                    # VII

    PyFlixList.next_movie()                                                     # VIII
    PyFlixList.get_current()                                                    # IX
    PyFlixList.rate()                                                           # X

    PyFlixList.prev_movie()                                                     # XI
    PyFlixList.remove_current()                                                 # XII
    print(PyFlixList)                                                           # XIII

    PyFlixList.info()                                                           # XIV

    testMovie4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)  #XV
    PyFlixList.next_movie()                                                     # XVI
    PyFlixList.next_movie()                                                     # XVII

    PyFlixList.get_current()                                                    # XVIII    
    print(PyFlixList)                                                           # XIX
