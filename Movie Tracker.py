import datetime

list_file = open("Movie_List.txt", "a+")

def get_movie():
    print ("What movie did you watch?")
    movie = input("")
    movie = str(movie)
    date = datetime.datetime.now()
    list_file.write("\n" + movie + "\n" + " - " + date.strftime("%x") + "\n")
    ()
    print ("Got it! That movie is added to the list")
    print()

get_movie()

def print_list():
    movie_list = list_file.read()
    print ("Would you like to see your list? y/n")
    check = input("")
    if check == "y":
        print (movie_list)
    return check

check = print_list()
while check == "n":
    print ("would you like to add another movie? y/n")
    check2 = input("")
    if check2 == "y":
        get_movie()
    if check2 != "y":
        print ("Ok. Goodbye!")
        print ("program terminated. File Closed")
        check = ""




list_file.close()
