import csv
from time import perf_counter
from itertools import combinations


def measure(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = perf_counter() - start
            print(f"{func.__name__}  execution time: {end_ if end_ >0 else 0} s")

    return wrapper


def extract_percent(param):
    return float(param.split("%")[0])


class Equity:
    def __init__(self, name: "str", cost: "float", percent_profit: "float"):
        self.name = name
        self.cost = cost
        self.percent_profit = percent_profit

    @property
    def profit(self):
        return self.cost * self.percent_profit / 100

    def __repr__(self):
        return f"{self.name}"


class Repository:
    def __init__(self):
        self.equities = []

    def _list_of_combination(self):
        list_of_combination_with_sum= []
        for i in range(len(self.equities)):
            combinations_ = combinations(self.equities, r=i + 1)
            for combination in combinations_:
                list_of_combination_with_sum.append(self._populate_sum_combination(combination))
        print("il y a ", len(list_of_combination_with_sum), "combinations")
        return sorted(
            list_of_combination_with_sum,
            key=lambda element: element["profit"],
            reverse=True,
        )

    def _populate_sum_combination(self, combination):

        return  {
                    "equities": combination,
                    "cost": self._get_sum_cost(combination),
                    "profit": self._get_sum_profit(combination),
                }

    def _get_sum_profit(self, combination):
        return sum([equity.profit for equity in combination])

    def _get_sum_cost(self, combination):
        return sum([equity.cost for equity in combination])

    def add_equity(self, equity: "Equity"):
        self.equities.append(equity)

    @measure
    def get_best_combination_by_brute_force(self, max_investment):
        for item in self._list_of_combination():
            if item["cost"] <= max_investment:
                return item
        return False


class App:
    def __init__(self):
        self.actions_repository = Repository()

    def populate_equities_with_csv(self, csv_enquiries):
        with open(csv_enquiries, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.actions_repository.add_equity(
                    Equity(
                        row["action"],
                        float(row["cost"]),
                        extract_percent(row["percent"]),
                    )
                )


if __name__ == "__main__":
    app = App()
    app.populate_equities_with_csv("equities.csv")
    result = app.actions_repository.get_best_combination_by_brute_force(500)
    print(
        f"{result['equities']}: for profit of {result['profit']} from cost {result['cost']} "
    )
