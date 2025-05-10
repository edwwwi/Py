class Math:
    def add(self, a=0, b=0):
        print("Sum is:", a + b)

# Create object
m = Math()

m.add()        # Sum is: 0
m.add(5)       # Sum is: 5
m.add(3, 7)    # Sum is: 10
