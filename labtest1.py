# Created by Ana Marcela Espinosa
# October 28th 2021
# Student Number: C20306516
# Object Oriented Programming Lab Test 1.

class Words:
    def __init__(self):
        self.dict = self.create_dict

    def load_file(self):
        create_dict = {}
        file = open('herbert1.txt', "rt")
        data = file.read()
        words = data.splt()

        for line in file:
            words = line.split()
            print (words)
            for word in words:
                if word in create_dict:
                    create_dict[word] = create_dict[word] + 1
                else: create_dict[word] = 1
        for key in list(create_dict.keys()):
            print(key, ":" , dict[key])


        file.close

        return create_dict

