from random import randint

class Elevator(object):
    """An elevator class. Elevator has a registered customer list, a current floor, a moving direction, and number of floors.
    For scale-up consideration, elevators can also be given min and max floor numbers."""
    # TODO: Make sub-classes that inherit from Elevator parent class, like an express elevator or double-speed elevator,
    # or allow for multiple independently operating elevators.

    def __init__(self, register_list=list(), current_floor=0, direction=1):
        self.register_list = register_list
        self.current_floor = current_floor
        self.direction = direction
        # TODO: If we wanted to assign operational zones to multiple elevators, we could do so:
        # self.min_floor = min_floor
        # self.max_floor = max_floor

    def move(self):
        """Move the elevator. With each step, elevator moves one floor up or one floor down."""
        # TODO: If different sub-classes of elevators existed, this could be adjusted to move elevators faster or slower,
        # or to move elevators to only even or odd floors, etc.

        self.current_floor += self.direction

    def set_direction(self):  
        """SCAN algorithm for setting elevator direction. Elevator proceeds to top floor, then once at top switches directions
        to proceed to bottom floor."""
        if self.current_floor >= building.num_of_floors - 1:
            self.direction = -1
        elif self.current_floor <= 0:
            self.direction = 1

    def add_customer(self, customer):
        """Adds customers to elevator list"""
        self.register_list.append(customer)

    def cancel_customer(self, customer):
        """Removes customer from elevator list"""
        self.register_list.remove(customer)

    def exit_customers(self):
        """Once customers arrive at their end floors, they are removed from the elevator list."""
        for customer in list(self.register_list):
            if customer.end_floor == self.current_floor:
                self.cancel_customer(customer)


class Customer(object):
    """A customer class. A customer has an ID, start floor number, and end floor number."""

    def __init__(self, id=None, total_floors, start_floor=None, end_floor=None):
        """Initializes customer and selects random values for start and end floors."""
        self.id = id
        self.start_floor = randint(0, total_floors-1)
        self.end_floor = randint(0, total_floors-1)
        #Code to handle case where the same start and end floors are randomly selected:
        if self.end_floor == self.start_floor and self.end_floor == total_floors-1:
            self.end_floor -= 1 
        elif self.end_floor == self.start_floor:
            self.end_floor += 1


class Building(object):
    """A building class. Building has a number of floors, a customer list, and its own elevator object."""
    # TODO: If we wanted to allow for multiple elevators, use a parameter such as "elevator_array = []".

    def __init__(self, num_of_floors=None, customer_list=list(), elevator=None):
        """Initializes building class and adds customer list, which is sorted by starting floor value."""
        self.num_of_floors = self.get_value("How many floors are in the building? ",
                                            "Incorrect value. Number of floors should be integer higher than 1.", 2)
        customers_num = self.get_value("How many customers are in the building? ",
                                       "Incorrect value. Number of customers should be non-negative integer.", 0)
        for i in range(customers_num):
            self.customer_list.append(Customer(i, self.num_of_floors))
        self.customer_list = sorted(self.customer_list, key=lambda x: x.start_floor)
        self.elevator = Elevator()
        # TODO: To scale up, we could create multiple elevator objects, each of which has its own min and max floors, for example:
        # self.elevator_array = [Elevator(1, 50, self.num_of_floors), Elevator(51, 100, self.num_of_floors)]

    def get_value(self, message, incorrect_message, minimal_value):
        """Interface method for getting valid integer input from user."""
        val = None
        try:
            val = int(input(message))
        except ValueError:
            print(incorrect_message)
            return self.get_value(message, incorrect_message, minimal_value)
        if val < minimal_value:
            print(incorrect_message)
            return self.get_value(message, incorrect_message, minimal_value)
        else:
            return val

    def enter_customers(self):
        """When the elevator gets to a customer's floor, the customer is added to the elevator and remove from the customer list."""
        for customer in list(self.customer_list):
            if customer.start_floor == self.elevator.current_floor:
                self.elevator.add_customer(customer)
                self.customer_list.remove(customer)

    def run(self):
        """Runs the program. Each time it is called:
            - Awaiting customers enter the elevator (register_customer is called)
            - Elevator direction value (up=1, down=-1) is determined
            - Elevator moves one floor up or one floor down depending on direction value
            - Any customer who has reached their end floor leaves the elevator (cancel_customer is called)
        """
        # TODO: Restructure classes to allow self.customer_actions() that lets customers make floor selections,
        # activate an emergency brake, etc.
        self.enter_customers()
        self.set_direction() 
        self.elevator.move() 
        self.elevator.exit_customers()


    def output(self):
        """Returns total number of steps done by elevator."""
        total_number = 0
        while self.awaiting_customers():
            self.run()
            total_number += 1
        return total_number

    def awaiting_customers(self):
        """Returns True if there is at least one customer not on her floor. Otherwise returns False."""
        if len(self.customer_list) > 0 or len(self.elevator.register_list) > 0:
            return True
        return False


def main():
    """main function"""

    building_def = Building()

    print("Number of steps:", building_def.output())

if __name__ == "__main__":
    main()
