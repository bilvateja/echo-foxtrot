import category

class tshirt(category.clothing):
    def __init__(self) -> None:
        super().__init__()
        self.price = 1000
        self.discount = 10
        self.quantity_purchased = 0

class jacket(category.clothing):
    def __init__(self) -> None:
        super().__init__()
        self.price = 2000
        self.discount = 5
        self.quantity_purchased = 0

class cap(category.clothing):
    def __init__(self) -> None:
        super().__init__()
        self.price = 500
        self.discount = 20
        self.quantity_purchased = 0