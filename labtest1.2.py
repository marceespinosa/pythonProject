# Created by Ana Marcela Espinosa
# October 28th 2021
# Student Number: C20306516
# Object Oriented Programming Lab Test 1.

class Words:


    def __init__(self):
        self.my_dict = self.find_words()
        self.find_words(self.my_dict)

    def load_file(self):
        file = open('herbert1.txt' , "rt")
        data = file.read()
        print(data)


        file.close()

    def find_words(self):

        my_dict = {}
        file = open('herbert1.txt', "rt")
        file_two = open('herbert2.txt' , "rt")

        # data = file.read()
        # words = data.split()
        # print('The number of words in the txt file', len(words))
        # for line in file:
            # print(line)
        # file.close()

        for line in file:
            words = line.split()
            print(words)
            for word in words:
                if word in my_dict:
                    my_dict[word] = my_dict[word] + 1
                else:
                    my_dict[word] = 1
        for key in list(my_dict.keys()):
            print(key, ":", my_dict[key])
        file.close()

        file = open('herbert2.txt' , "rt")
        my_dict = {}

        for straight in file_two:
            words = straight.split()
            print(words)
            for look in my_dict:
                if look in my_dict:
                    my_dict[look] = my_dict[look] + 1
                else:
                    my_dict[look] = 1
        for keys in list(my_dict.keyss()):
            print(keys, ":", my_dict[keys])
            file.close()










       # file.close

        return my_dict


      #file = open('herbert2.txt' , "rt")


wc = Words()







