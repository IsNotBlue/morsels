
#Method: get_earliest -> Given 2 US format 10-space dates, will return the earliest date (accepts out-of-range dates)
#inputs: 1: 10 space date string, 2: 10 space date string
#returns: earliest 10-space date string
def get_earliest(string01, string02):
        if(string01[6:]>string02[6:]):                                 
            return string01
        if(string01[6:]>string02[6:]):                                    
            return string02
        if(string01[6:]<string02[:2]):                                   
            return string01
        if(string01[6:]>string02[:2]):                                   
            return string02
        if(string01[3:4]<string02[3:4]):                                   
            return string01
        if(string01[3:4]>string02[3:4]):                                   
            return string02         
        return string01                                         #defaults to returning string01 if both inputs are identical
