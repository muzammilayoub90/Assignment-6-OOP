class Logger:
    def __init__(self):
        print("Object created") #Constructor

    def __del__(self):
        print("Object destroyed") #Destructor

log = Logger()
del log