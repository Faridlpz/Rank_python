class Computer:

    def __init__(self):
        self.__maxprice = 900  #Aqui hago mi encapsulacion con los dos __ en mi atributo aqui se utiliza la abstraccion de datos

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()