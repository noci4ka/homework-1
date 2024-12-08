class cats:
    def __init__(self, type, eyes):
        self.type = type
        self.eyes = eyes

    def meow(self):
        print(f"hello I am {self.type} cat and i have {self.eyes} eyes! meowwww")



cat_1= cats(type = "persian", eyes="blue")
cat_1.meow()
cat_2 = cats(type = "calico", eyes="brown")
cat_2.meow()
