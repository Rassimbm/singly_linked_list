# Create a new Python file and recreate the Node and SList classes
class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    # Add the add_to_front method to your SList class
    def add_to_front(self,val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    # Add the print_values method to your SList class
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self


