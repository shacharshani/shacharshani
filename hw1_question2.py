
def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    for num in range(100000,999997):
        #first cond
        str_num = str(num)
        if str_num[2] == str_num[5] and str_num[3] == str_num[4]:
            #second cond
            str_num = str(num+1)
            if str_num[1] == str_num[5] and str_num[2] == str_num[4]:
                #third cond
                str_num = str(num+2)
                if str_num[1] == str_num[4] and str_num[2] == str_num[3]:
                    #fourth cond
                    str_num = str(num+3)
                    if str_num[0] == str_num[5] and str_num[1] == str_num[4]\
                       and str_num[2] == str_num[3]:
                        print(num)

if __name__ == "__main__":
    
    result = check_palindrome()
    print("Result: ", result)