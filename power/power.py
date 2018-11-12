def power(a,b):
#checking data type
    if not((isinstance(a,int) or isinstance(a,float)) and isinstance(b,int)):
       return "invalid input"

#The condition is such that if b is equal to 1, b is returned
    if(b==1):
        return(a)
#If b is not equal to 1, a is multiplied with the power function and called recursively with arguments as the base and power minus 1
    if(b!=1):
        return(a*power(a,b-1))
#the final result is then output


if __name__ == '__main__':
    print("Result:",power(2,5))
    