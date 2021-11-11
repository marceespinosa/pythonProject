# course: Object-oriented programming, year 2, semester 1
# academic year: 202122
# author: B. Schoen-Phelan
# date: 14-10-2021
# purpose: Lab 4
import random
import sys

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        #my_list = list(self.user_input)
        #print(my_list[2])

        #temp = my_list[1]
        #my_list[1] = my_list[2]
        #my_list[2] = temp


        #print(my_list)





        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        my_list = self.user_input.split()
        print(my_list)

        print(my_list[0])

        second_list = my_list[0]
        print(second_list[2])
        second_list[1] = second_list[2]
        second_list[2] = second_list[1]
        print(second_list)




word_scrambler = WordScramble()
word_scrambler.scramble()

