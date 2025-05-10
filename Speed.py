class Speed:
    def get_distance(self):
        self.km = float(input("Enter Kilometers : "))
    def print_distance(self):
        m = self.km*1000
        print(m)
mtr = Speed()
mtr.get_distance()
mtr.print_distance()
