from sys import argv
import purchase

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]

    # Initialize cart Object
    cart = purchase.cart() 

    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        # Add your code here to process input commands.
        cmd = line.strip()
        keys = cmd.split(" ")

        if keys[0] == "ADD_ITEM":
            #ADD_ITEM command
            cart.addItem(item= keys[1], quantity= keys[2])
            pass
        elif keys[0] == "PRINT_BILL":
            #PRINT_BILL command
            cart.printBill() #process the input command and get the output
    
if __name__ == "__main__":
    main()