#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    #replace this for solution

    if ((number % 15) == 0 ):
        print('"Fizz Buzz", "%d is divisible by 3 and 5"' % number)
        return "Fizz Buzz"
    elif (number % 3 == 0):
        print('"Fizz", "%d is divisible by 3"' % number)
        return "Fizz"
    elif (number % 5 == 0):
        print('"Buzz", "%d is divisible by 5"' % number)
        return "Buzz"

    print('"%d", "%d is not divisible by 3 and 5"' % (number, number))    
    return str(number)

