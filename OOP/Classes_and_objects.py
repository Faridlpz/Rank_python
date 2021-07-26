class ComplexNumber:
    '''This is a docstring. I have created a new class'''
    # Instance attributes
    def __init__(self, r=0, i=0) -> None: # __ todos los que tengan doble guien bajo se les denomina "Magic methods" o "Special Methods"
        self.real = r
        self.imag = i
    
    #instane method
    def get_data(self):
        print(f'{self.real}+{self.imag}')

#Intance the object
num1 = ComplexNumber(2, 3)

num1.get_data()



