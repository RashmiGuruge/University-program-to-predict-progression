# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID : 

# Date : 6/12/2020

# Define global variable
global vol_pass   
global vol_defer  
global vol_fail
global count_progress  
global count_trailer   
global count_retriever 
global count_exclude   
global count_all

# Create variables
count_progress  = 0
count_trailer   = 0
count_retriever = 0
count_exclude   = 0
count_all       = 0
row        = 0
list_index = 0

# Creating a list 
use_data = [[120,100,100,80,60,40,20,20,20,0],
            [0,20,0,20,40,40,40,20,0,0,],
            [0,0,20,20,20,40,60,80,100,120]]

# counting the list index range using the while loop
while list_index < 10  :

    # Reading the list
    vol_pass  = use_data [0][row]
    vol_defer = use_data [1][row]
    vol_fail  = use_data [2][row]
    
    # counting the row
    row += 1
    
    # counting the list index
    list_index += 1

    # Displaying the outcomes(Progress, Progress(module trailer), Do not Progress–module retriever, Exclude)
    
    if (vol_pass == 120):
        print ("Progress")
        # counting the number of progress
        count_progress += 1
            
    elif (vol_pass == 100 and vol_defer <= 20 and vol_fail <= 20):
        # counting the number of module trailer
        print ("Progress (module trailer)")
        count_trailer += 1 
            
    elif (vol_pass <= 80 and vol_defer <= 40 and vol_fail <= 60):
        # counting the number of module retriever
        print ("Do not Progress – module retriever")
        count_retriever += 1
            
    elif (vol_pass <= 20 and vol_defer <= 20 and vol_fail <= 120):
        # counting the number of Exclude
        print ("Exclude")
        count_exclude += 1

    # counting the all outcomes       
    count_all += 1

# Difine the function for print the histogram    
def histogram ():
    print("\n")   
    print("Progress  " ,count_progress ,":" , count_progress * "*") 
    print("Trailer   " ,count_trailer  ,":", count_trailer * "*")
    print("Retriever " ,count_retriever,":"  , count_retriever * "*")
    print("Exclude   " ,count_exclude  ,":", count_exclude * "*")
    print("\n")
    print(count_all,"outcomes in total.")    

# calling a function for print the histogram
histogram ()    
