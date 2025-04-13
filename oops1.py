class mobile: 

    # class variable -> variable that is shared by all the instances of the class.
    charger = "yes" # common in all the objects  

    # init is constructor it gets called whenever object gets created/
    def __init__(self, name, colour):
        self.name = name  # self acts like object 
        self.colour = colour  # instance variable. 
       # print("i am init")
# instance method
    def mobile_purchase(self, name, colour): # instance method
        print("thanks for purchasing", name, "with", colour, "colour")

    def mobile_p(self): # instance method.
        print("thanks for buying ", self.name,"with", self.colour, "colour")

# class method 
    @classmethod # decorator tells it is classmethod.
    def verification(cls):
        print("charger is available ?", cls.charger)

# static method -> this type of method takes neither self nor cls.
# helpful when we want to access other class objects.
# when i have nothing to do with instance variables, class variables 

    @staticmethod # decorator for static method 
    def add(a,b):
        print(a+b)



sam = mobile("samsung", "red")
sam.name= "samsung" # instance variable
sam.colour = "red" # instace variable -> belongs to object or instance 
#sam.mobile_purchase(sam.name, sam.colour)

deepak = mobile("apple", "black")
deepak.name = "apple"
deepak.colour = "black"
#deepak.mobile_purchase(deepak.name,deepak.colour) #
deepak.mobile_p()

ram = mobile("google", "blue") 
ram.mobile_p() 
ram.verification() # accessing class method by object

print(ram.charger) # class variable common among all the objects 

# Instance methond -> belongs to the object of class no to the class can be used after creating object

print(mobile.charger) # can be accessed using class only do not need object for accessing class variable.

mobile.verification() # accessing class method without the object. 

mobile.add(5,5) # accessing static method using class only 
ram.add(2,3) # acessing static method using object 







