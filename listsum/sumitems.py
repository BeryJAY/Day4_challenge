def sumlist(first_list):
    if not isinstance (first_list,list):
        return "This must be a list"
    sum=0
    for x in first_list:
        if isinstance(x,int):
            sum+=x
        elif isinstance(x,list):
            sum+=sumlist(x)
        
    return sum

if __name__ == '__main__':
    print(sumlist(['a',7,[5,9,10]]))