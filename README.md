# ranpy
Random python projects


welcome to the end of the line. simple projects, to very complex, organized with little to no thought.

If you want good code: beware.

Here is an exerpt from one of my first programs, a timer:

    import time as t
    try:
        x = 0
        print("control + c to stop - times in accuracy of 0.01")
        while True:
            y = float(x + .01)
            w = round(y,2)
            z = str(w)
            x = y
            t.sleep(.01)
    except KeyboardInterrupt:
        print("Your time is "+ z + " seconds.")
        exit()
        
        
yeah
