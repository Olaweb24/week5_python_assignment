
class Clothes:
    def __init__(self, cloth_type, size, color, price):
        self.cloth_type = cloth_type
        self.size = size
        self.color = color
        self.__price = price   
    
    def display_info(self):
        print(f"{self.color} {self.cloth_type} (Size: {self.size}) - Price: ${self.__price}")
    
    def wash(self):
        print(f"The {self.cloth_type} is being washed 🧼")

class DesignerClothes(Clothes):
    def __init__(self, cloth_type, size, color, price, designer):
        super().__init__(cloth_type, size, color, price)
        self.designer = designer

    
    def display_info(self):
        print(f"{self.designer} {self.cloth_type} (Size: {self.size}, Color: {self.color})")
        


cloth1 = Clothes("T-Shirt", "M", "Blue", 50)
cloth2 = DesignerClothes("Dress", "S", "Red", 200, "Gucci")

cloth1.display_info()
cloth1.wash()

print("----")

cloth2.display_info()
cloth2.wash()



