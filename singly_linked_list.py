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
    # Add the add_to_back method to your SList class
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        else:
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node
            return self
        
my_list = SList()
my_list.add_to_front("is").add_to_front("name").add_to_front("My").add_to_back("Rassim").print_values()


