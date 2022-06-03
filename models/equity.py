class Equity:
    def __init__(self, name: "string", cost: "float", percent_profit: "float"):
        self.name = name
        self.cost = cost
        self.percent_profit = percent_profit

    @property
    def profit(self):
        return self.cost * self.percent_profit / 100

    def __repr__(self):
        return f"{self.name}"
