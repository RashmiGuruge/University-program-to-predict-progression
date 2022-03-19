# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID : 

# Date : 22/11/2020

# Create variables
vol_pass   = 0
vol_defer  = 0
vol_fail   = 0
count_progress  = 0
count_trailer   = 0
count_retriever = 0
count_exclude   = 0
count_all       = 0

print("\n\tStaff Version with Vertical Histogram\n")

# Difine the function for outcomes            
def outcomes():

    # Define global variable
    global count_progress  
    global count_trailer   
    global count_retriever 
    global count_exclude   
    global count_all      

    # Displaying the progression outcomes(Progress, Progress(module trailer), Do not Progress–module retriever, Exclude)
    
    if (vol_pass == 120):
        print ("Progress\n")
        # count the progress 
        count_progress += 1
            
    elif (vol_pass == 100 and vol_defer <= 20 and vol_fail <= 20):
        print ("Progress (module trailer)\n")
        # count the trailer
        count_trailer += 1 
            
    elif (vol_pass <= 80 and vol_defer <= 120 and vol_fail <= 60):
        print ("Do not Progress – module retriever\n")
        # count the retriever
        count_retriever += 1
            
    elif (vol_pass <= 40 and vol_defer <= 40 and vol_fail >= 80):
        print ("Exclude\n")
        # count the exclude
        count_exclude += 1
        
    # count the all outcomes   
    count_all += 1
    

# Difine the function for checking the validation     
def input_validation():

    # Define global variable
    global vol_pass   
    global vol_defer  
    global vol_fail

    # Continuous loop with break statement    
    while True:

        # while loop with break statement
        while True :
            # Checking the user inputs are Integers
            try :
                # Getting the input from the user for pass
                vol_pass = int(input("Enter your total PASS credits  :"))
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
                vol_defer = int(input("Enter your total DEFER credits :"))
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
                vol_fail = int(input("Enter your total FAIL credits  :"))
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
        break


# Difine the function for print the vertical histogram         
def vertical_histogram ():

    # Define global variable
    global count_progress  
    global count_trailer   
    global count_retriever 
    global count_exclude

    # Displaying histogram detail
    print("\n\t....Vertical Histogram....\n") 
    print("Progress",count_progress,"| Trailer",count_trailer,"| Retriever",count_retriever,"| Exclude",count_exclude)

    # Finding the maximum outcome using the while loop
    while (max(count_progress,count_trailer,count_retriever,count_exclude) > 0):

        # Checking if the number of count are greater than 0
        # then print the star and subtract from the count
        # if not in the greater than 0 then print the space and subtract from the count
        if count_progress > 0:
            pro = "*"
            count_progress -= 1
        else :
            pro = " "
            count_progress -= 1

        if count_trailer > 0:
            tra = "*"
            count_trailer -= 1
        else :
            tra = " "
            count_trailer -= 1

        if count_retriever > 0:
            ret = "*"
            count_retriever -= 1
        else :
            ret = " "
            count_retriever -= 1

        if count_exclude > 0:
            exc = "*"
            count_exclude -= 1
        else :
            exc = " "
            count_exclude -= 1

        # Displaying the vertical histogram
        print("  ",pro,"          ",tra,"           ",ret,"           ",exc)


# Continuous loop with break statement                   
while True:

    # calling a function for checking the validation
    input_validation()

    # Displaying histogram detail
    print ("Would you like to enter another set of data ?")
    # Getting the user choice
    choice = input("Enter 'y' for yes or 'q' to quit and view results : ")

    # Selection
    if choice == "y" or choice == "Y" :
        print("\n")
        continue   
    elif choice == "q" or choice == "Q" :
        print("\n")
        # calling a function for print the histogram
        vertical_histogram ()
        
        # Displaying the total outcomes
        print(count_all,"outcomes in total.")
        break    
    else:
        print("\n\t....Invalid Input....\n")
        continue
        
