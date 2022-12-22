import category

class notebook(category.stationery):
    def __init__(self) -> None:
        super().__init__()
        self.price = 200
        self.discount = 20
        self.quantity_purchased = 0

class pen(category.stationery):
    def __init__(self) -> None:
        super().__init__()
        self.price = 300
        self.discount = 10
        self.quantity_purchased = 0

class marker(category.stationery):
    def __init__(self) -> None:
        super().__init__()
        self.price = 500
        self.discount = 5
        self.quantity_purchased = 0