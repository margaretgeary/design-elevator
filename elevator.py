import random

class Elevator(object):
    """An elevator class."""
    def __init__(self, total_floors, request_list = [], direction = "up", current_floor = 1):
        #An elevator can have the attributes total floors, request list, direction (up/down), and current floor.
        self.total_floors = total_floors
        self.request_list = request_list
        self.current_floor = current_floor
        self.direction = direction

    def move(self):
        """Move elevator one floor up or down"""
        if self.direction == "up":
            self.current_floor += 1
        else:
            self.current_floor -= 1
        #If we're at the top floor, the elevator direction must be "down."
        if self.total_floors == self.current_floor:
            self.direction = "down"

    #We can add and remove user requests from the request list
    def add_request(self, user):
        self.request_list.append(user)

    def remove_request(self, user):
        self.request_list.remove(user)


class Building(object):
    """A building class"""
    def __init__(self, total_floors, users, elevator):
        self.total_floors = total_floors
        self.users = users
        self.elevator = elevator

    def run(self):
        #print the elevator's current floor and direction
        while Elevator.current_floor != 0:
            print(Elevator.current_floor, elevator.direction)
            for user in self.users:
                # if the elevator is on the same floor as the user, the elevator direction is the same as the user direction, and the user has not yet boarded:
                if elevator.current_floor == user.on_floor and user.fin == 0 and elevator.direction == user.direction:
                    #add user to elevator request list
                    elevator.request_list.append(user)


#
