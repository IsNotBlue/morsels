
#Method: get_earliest -> Given 2 US format 10-space dates, will return the earliest date (accepts out-of-range dates)
#inputs: 1: 10 space date string, 2: 10 space date string
#returns: earliest 10-space date string
def get_earliest(string01, string02):
    for i in range(0, 3):                                   #iterate through compared dates maximum of 3 times  
        if(i == 0):                                         #first iteration, compare the years
            nString01 = string01[6:]
            nString02 = string02[6:]
        elif(i == 1):                                       #second iteration, compare the months
            nString01 = string01[:2]
            nString02 = string02[:2]
        else:                                               #third iteration, compare the days
            nString01 = string01[3:4]
            nString02 = string02[3:4]          
        if(int(nString01) > int(nString02)):               #compare strings as ints and return lowest (if one is lowest)
            return string02
        elif(int(nString01) < int(nString02)):
            return string01
    return string01                                         #defaults to returning string01 if both inputs are identical
