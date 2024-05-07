class laptop:
    def __init__(self):
        self.price=""
        self.rate=""
       
    def display(self):
        print("Enter price:",self.price)
        print("Enter rate:",self.rate)
python = laptop()
python.price=5000
python.rate="sr"
python.display()

