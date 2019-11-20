print("program started")
try:
    print("outer try block entered")
    try:
        print("inner try block entered")
        raise IndexError
    except IndexError as e:
        print("something went wrong",e)
    else:
        print("no exceptions")
    print(2/0)
except ZeroDivisionError:
    print("caught in outer except")
finally:
    print("end of the program")
