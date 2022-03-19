# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID : 

# Date : 12/11/2020

# Create variables
vol_pass   = 0
vol_defer  = 0
vol_fail   = 0

# Difine the function for outcomes
def outcomes():
    
    # Displaying the progression outcomes(Progress, Progress(module trailer), Do not Progress–module retriever, Exclude)
    if (vol_pass == 120):
        print ("Progress\n")
        # print seperater
        print ("--"*35)            
    elif (vol_pass == 100 and vol_defer <= 20 and vol_fail <= 20):
        print ("Progress (module trailer)\n")
        # print seperater
        print ("--"*35)            
    elif (vol_pass <= 80 and vol_defer <= 120 and vol_fail <= 60):
        print ("Do not Progress – module retriever\n")
        # print seperater
        print ("--"*35)            
    elif (vol_pass <= 40 and vol_defer <= 40 and vol_fail >= 80):
        print ("Exclude\n")
        # print seperater
        print ("--"*35)

# Difine the function for checking the validation   
def input_validation():

    # Define global variable
    global vol_pass   
    global vol_defer  
    global vol_fail

    # Continuous loop     
    while True:

        # while loop with break statement
        while True :
            # Checking the user inputs are Integers
            try :
                # Getting the input from the user for pass
                vol_pass = int(input("Please enter your credit at pass  :"))
                # Checking if the user inputs are in the required range of values
                if ((vol_pass) not in range (0,125,20)):
                    print("Out of Range\n")
                else :
                    break
            except:
                print("Integer Required\n")
                continue


        # while loop with break statement    
        while True :
            # Checking the user inputs are Integers
            try :
                # Getting the input from the user for defer
                vol_defer = int(input("Please enter your credit at defer :"))
                # Checking if the user inputs are in the required range of values
                if ((vol_defer) not in range (0,125,20)):
                    print("Out of Range\n")
                else :
                    break
            except:
                print("Integer Required\n")
                continue


        # while loop with break statement    
        while True :
            # Checking the user inputs are Integers
            try :
                # Getting the input from the user for fail
                vol_fail = int(input("Please enter your credit at fail  :"))
                # Checking if the user inputs are in the required range of values
                if ((vol_fail) not in range (0,125,20)):
                    print("Out of Range\n")
                else :
                    break
            except:
                print("Integer Required\n")
                continue
            
        # Checking all user inputs are equal to 120 
        if((vol_pass + vol_defer + vol_fail) != 120):
            print("Total Incorrect\n")
            continue
        
        # calling a function for displaying outcomes
        outcomes()
        
# calling a function for checking the validation            
input_validation()
        



 
