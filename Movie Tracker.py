print("Did you watch a movie? y/n")
check = input("")
if check != "y":
    print ("Ok. Goodbye")
    print ("program terminated")
else:
    print ("What movie did you watch?")
    movie = input("")
movie_list = []
movie_list.append(movie)
print()
print ("Got it! That movie is added to the list")
print()
print ("Would you like to see your list? y/n")
check2 = input("")
if check2 != "y":
    print ("Ok. Goodbye!")
    print ("program terminated")
else:
    print ("your list: " + str(movie_list))