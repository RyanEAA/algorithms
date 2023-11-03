def main():
    customersfromfile()
    
def customersfromfile():
    #create a variable and assingn it the pato to the file
    infile = open('customer.txt', 'r')
    
    
    #read the files contents
    file_contents = infile.read()
    
    #close file
    infile.close()
    
    
    #print the data that was read into a variable
    print(file_contents)
    
main()