import numpy as n
class deque:

    def __init__(self):
        self.args = []
        self.max = 20

    def add_to_front(self, data):
        if len(self.args) == self.max:
            return "Full Deck"
        else:
            self.args.insert(0,data)
        
    def add_to_rear(self, data):
        if len(self.args) == self.max:
            return "Full Deck"
        else:
            self.args.append(data)

    def remove_from_front(self):
        if self.args != []:
            self.args.pop()
        else:
            return "Deque Empty"
        
    def remove_from_rear(self):
        if self.args != []:
            self.args.pop(0)
        else:
            return "Deque Empty"
        
    def size(self):
        if self.args == []:
            return None
        elif len(self.args) == self.max:
            return "Deck Full ( Max size of deck is 20)"
        else:
            return len(self.args)
    
    def isEmpty(self):
        
        if(self.items) == []:
            return True
        else:
            return False
    
    def peek_front(self):
        return self.args[-1]
    
    def peek_back(self):
        return self.args[0]
    
    def __repr__(self):
        "Object : {}".format(self.args)
        
if __name__ == "__main__":
    dq = deque()
    pro = n.random.randint(1,100, 1)
    dq.add_to_front(pro)
    dq.add_to_front(pro)
    print("peekfront", dq.peek_front())
    print("Size", dq.size())

    