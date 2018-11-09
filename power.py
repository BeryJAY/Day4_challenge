def power(a,b):
#user given a priority of entering their own values using the keyword "input" and then the same numbers are passed a argments to a recursive function to find the power of the number

    a=int(input())
    b=int(input())
#The condition is such that if b is equal to 1, b is returned
    if(b==1):
        return(a)
#If b is not equal to 1, a is multiplied with the power function and called recursively with arguments as the base and power minus 1
    if(b!=1):
        return(a*power(a,b-1))
#the final result is then output
print("Result:",power(a,b))