list_file = open("Movie_List.txt", "a")

print("Did you watch a movie? y/n")
check = input("")
if check != "y":
    print ("Ok. Goodbye")
    print ("program terminated")
else:
    print ("What movie did you watch?")
    movie = input("")
    movie = str(movie)
list_file.write(movie + "\n")
print()
print ("Got it! That movie is added to the list")
print()
list_file.close()
list_file = open("Movie_list.txt", "r")
print ("Would you like to see your list? y/n")
check2 = input("")
if check2 != "y":
    print ("Ok. Goodbye!")
    print ("program terminated")
else:
    movie_list = list_file.read()
    print()
    print (movie_list)
list_file.close()
