# this program creates a loop to accept customer names



def main():
    customerstofile()
    
    
def customerstofile():
    #open file named customer.txt
    outfile = open('customer.txt', 'w+')

    # create a loop to accept customer names
    while True:
        CustName = input("Enter Customer Name: ")
        outfile.write(CustName + '\n')
        
        enterMore = input("do you wish to enter more? enter y to continue: ")
        if enterMore == "y":
            continue
        else:
            break
        
        
    #close the file
    outfile.close()
    
main()

