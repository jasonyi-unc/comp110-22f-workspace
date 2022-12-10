class Basket:

    eggs: list[int]

    def __init__(self, eggs: list[int] = []):
        self.eggs = eggs

    def same_colors(self, rhs) -> bool:
        for i in range(len(self.eggs)):
            for j in range(len(rhs.eggs)):
                if self.eggs[i] == rhs.eggs[j]:
                    return True
        return False

p1: Basket = Basket(["red", "white", "blue", "pink", "purple"])
p2: Basket = Basket([])

print(p1.same_colors(p2))