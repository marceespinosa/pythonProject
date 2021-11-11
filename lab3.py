#course: Object-oriented programming, year 2, semester 1
#academic year: 2021-22
#author: B. Schoen-Phelan
#date: 07-10-2021
#purpose: Lab 3

# Tasks:
#  1. Run the file as is
#  2. Follow the comments in the file and try to solve the
#     exercises. Use the Python documentation to identify
#     functions that could help you.
#  3. Answer the quiz questions.


class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # 1. print only first and last of the sentence:

        last_char = message[-1]
        print('Last letter is:', last_char)

        first_char = message[0]
        print('Fist letter is: ', first_char)





        # 2. use slice notation:
        print('The first letter of the message is: ', message[0:3], message[3:6], message[6:9])



        # 3. escaping a character, such as an apostrophe or & sign:

        str = 'It\'s Thursday and I\'m sick'
        print(str)


        # 4. find all a's in the input word and count how many there are:

        x = message.count('a')
        print('count for the a\'s in the word:', x)




        # 5. replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():

        y = message.replace("a", "-")
        print("This is the word replaced: ", y)



    # to run the tasks associated with this file, you must first
    # uncomment line number 75 and comment line 74
    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # 6. hand the input string to a list and print it out:
        z = message.split()
        print(z)


        # 7. append a new element to the list and print:
        z.append('hi!')
        print(z)


        # 8. remove from the list in 3 ways:
        z.remove('ana')
        print(z)

        z.pop(0)
        print(z)



        # 9. check if the word cake is in your input list:
        c = z.count("cake")
        print("This is the count for the word cake", c)


        # 10. reverse the items in the list and print using a function:
        z.reverse()
        print(z)


        # 11. reverse the list with the slicing trick:

        print(z[::-1])

        # 12. print the list 3 times by using multiplication:
        for i in range(3):
            print(z)




tas = Types_and_Strings() # creates an instance of the object
#tas.play_with_strings() # calls the method play_with_strings()
tas.play_with_lists()
