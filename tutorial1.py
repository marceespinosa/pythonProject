# user_name = "ANA"
# print("user name :" user_name)


user_name, user_age = "Ana", 20
# [] will print out the letter by letter 0 is the first letter 1 is the second
print(user_name[1])

# will print the first and second letter and the last is always excluded
print(user_name[0:2])

print(user_name, user_age)

# where the user_name lives
print(id(user_name))

# user_name = 25
# print("false user name is age: ", user_name)
# where things live use id
# print(id(user_name))

# not allowed to be 2users
two_users = "Ana and Marcela"

# not allowed to use & you can use double and single quotation marks.
# in c there would be a printf("this is a variable )

last_name = "Espinosa"
# print(user_name + '' + last_name) this will not work and will need a casting

flight_number = 3456
print("Can passenger" + user_name + "please make her way to flight number", flight_number)

print("%30d"%(flight_number))
print("%7.2f"%(1.234567))

# format a message
message = "Can passenger {0:s} please go to gate {1:d}".format(user_name, flight_number)
print(message)

print("This is a string".count('s'))

# index of a number
print("This is a string" .index('a'))

print("Postman".endswith('man'))

print("123".isnumeric())
print("123".isdigit())

