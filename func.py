def find_total_days():
    # Ask the user for input and convert the input to integers
    years = int(input("Enter number of years: "))
    months = int(input("Enter number of months: "))
    days = int(input("Enter number of days: "))
    
    # Assign a variable to hold the calculations for the number of days in
    # a year (years*365) plus the number of days in a month (months*30) plus
    # the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
    
    # Use the "return" keyword to send the result of the "my_days"  
    # calculation to the function call. 
    return my_days

# Call the function
print(find_total_days()