
def is_answer_num():
    answer = input("Please type in a number")

    try: #the programm will try to complete the following actions:
        print(int(answer)) #covert the user's answer to an integer
        print(type(int(answer))) #print out the data type of the answer - which should always be int in this case
        #if it can do them without an error occuring, it will
    except: #if when the above is tried an error occures, the following actions will occur:
        print("try again")
        is_answer_num() #the function will be called again to allow the user to try again

is_answer_num()