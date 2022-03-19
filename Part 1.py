# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID : 

# Date : 7/11/2020

# Create variables
vol_pass  = 0
vol_defer = 0
vol_fail  = 0

# Getting user input
vol_pass  = int(input("Please enter your credit at pass  :"))
vol_defer = int(input("Please enter your credit at defer :"))
vol_fail  = int(input("Please enter your credit at fail  :"))


# Displaying the progression outcomes(Progress, Progress(module trailer), Do not Progress–module retriever, Exclude)
if (vol_pass == 120):
    print ("Progress")
    
elif (vol_pass == 100 and vol_defer <= 20 and vol_fail <= 20):
    print ("Progress (module trailer)")
    
elif (vol_pass <= 80 and vol_defer <= 120 and vol_fail <= 60):
    print ("Do not Progress – module retriever")
    
elif (vol_pass <= 40 and vol_defer <= 40 and vol_fail >= 80):
    print ("Exclude")
        
