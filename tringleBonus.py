#time lib i will use it for delay the code
import time

#def is to make function fliploop the function name value:int value if you call the function you will give the value
def fliploop(value:int):
    #it will add string to string then return it as one
    fullstring = ''
    while True:
        #empty string
        x = ''
        #get the original value without changing thing
        orValue = value
        #loop to get the first line example 10 9 8 7....1
        while True:
            #if the value equal to 0 it will leave the loop
            if value == 0:
                break
            #if the value not equal 0 it will complete the loop
            elif value != 0:
                #it will print the value in one string like "10 9 ......" and each loop will add a number
                x = f"{x + ' ' + str(value)}"
                #remove number if you enter 10 it will be 9 to the next tringle
            value = value - 1
        time.sleep(0.1)
        #it will add the old string 10 9 8 7 and go to new line until finish the full tringle the you can print the tringle without back to the loop
        fullstring = f"{fullstring + x}\n"
        value = orValue - 1
        if value == 0:
            break

    return fullstring

print(fliploop(10))