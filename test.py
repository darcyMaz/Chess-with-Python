
class Test:
    def __init__(self, name):
        self.name = name
        self.id = 0

    def incr_id(self):
        self.id = self.id + 1

    def print_name(self):
        print(self.name)

    def print_id(self):
        print(self.id)

    def get_id(self) -> int:
        if self.id == 3:
            return None
        return self.id

class Test_(Test):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id
    def double_incr_id(self):
        self.incr_id()
        self.incr_id()

def main():
    #test = Test_('darcy', 3)
    #test.print_name()
    #test.print_id()
    #test.double_incr_id()
    #test.print_id()
    #print(test.get_id())
    #print(ord('A'))
    list = [1,2,4,5,6,2]
    print(list)
    two = list.pop(2)
    print(list, two)



if __name__ == "__main__":
    main()