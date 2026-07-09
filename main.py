def jumlahkan(num_1, num_2=10):
    num_1 = int(num_1)
    num_2 = int(num_2)
    return num_1 + num_2

class Angka:
    def __init__(self, number):
        self.number = int(number)
        
    def add_new(self, other_num):
        self.number = jumlahkan(self.number, other_num)