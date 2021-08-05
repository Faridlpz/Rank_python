class Customer:
    def __init__(self, name, membership_type) -> None:
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        
        return self.name + " "+self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, o: object) -> bool:
        if self.name == o.name and self.membership_type == o.membership_type:
            return True

        return False

    __hash__ = None

    __repr__ = __str__

customers = [Customer("Farid","Diamond"),
            Customer("Jair", "GOLD")]

Customer.print_all_customers(customers)
#customers[1].update_membership("Bronze")

print(customers)