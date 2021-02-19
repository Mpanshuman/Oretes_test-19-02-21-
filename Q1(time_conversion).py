'''
take input in 12hr format 
'''

time = input('Enter time in hh/mm/ss AM/PM format:')

def convert_time(time): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if time[-2:] == "AM" and time[:2] == "12": 
        return "00" + time[2:-2] 
          
    # remove the AM     
    elif time[-2:] == "AM": 
        return time[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif time[-2:] == "PM" and time[:2] == "12": 
        return time[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(time[:2]) + 12) + time[2:8] 

if __name__ == "__main__":
    print(convert_time(time)) 