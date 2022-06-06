# is brute force O(e)
import csv
from functools import wraps
from time import time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"{func.__name__}  execution time: {end_ if end_ > 0 else 0} ms")

    return _time_it


def extract_percent(param):
    return float(param.split("%")[0])


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


class Repository:
    def __init__(self):
        self.equities = []

    def _number_of_equities(self):
        return len(self.equities)

    def add_equity(self, equity: "Equity"):
        self.equities.append(equity)

    def get_equities_sorted_by_percent_cost(self):
        return sorted(self.equities, key=lambda equity: equity.percent_profit, reverse=True)

    @measure
    def get_best_combination(self, max_investment):
        total_profit = 0
        total_cost = 0
        combination = []
        equities = []
        i = 0
        equities_sorted = self.get_equities_sorted_by_percent_cost()
        """
         {
                    "combination": combination,
                    "equities": self._get_equities_from_index_tuple(combination),
                    "cost": self._get_sum_cost_from_index_tuple(combination),
                    "profit": self._get_sum_profit_from_index_tuple(combination),
                }
        """
        while i < len(equities_sorted) :
            new_total_cost = total_cost + equities_sorted[i].cost
            if new_total_cost <= max_investment:
                total_cost = new_total_cost
                total_profit += equities_sorted[i].profit
                combination.append(i)
                equities.append(equities_sorted[i])
            i += 1

        return {"combination": tuple(combination),
                "equities": tuple(equities),
                "cost": total_cost,
                "profit": total_profit}


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

    def populate_equities(self):
        self.actions_repository.add_equity(Equity("Action-1", 20, 5))
        self.actions_repository.add_equity(Equity("Action-2", 30, 10))
        self.actions_repository.add_equity(Equity("Action-3", 50, 15))
        self.actions_repository.add_equity(Equity("Action-4", 70, 20))
        self.actions_repository.add_equity(Equity("Action-5", 60, 17))

        self.actions_repository.add_equity(Equity("Action-6", 80, 25))
        self.actions_repository.add_equity(Equity("Action-7", 22, 7))
        self.actions_repository.add_equity(Equity("Action-8", 26, 11))
        self.actions_repository.add_equity(Equity("Action-9", 48, 13))
        self.actions_repository.add_equity(Equity("Action-10", 34, 27))
        self.actions_repository.add_equity(Equity("Action-11", 42, 17))
        self.actions_repository.add_equity(Equity("Action-12", 110, 9))
        self.actions_repository.add_equity(Equity("Action-13", 38, 23))
        self.actions_repository.add_equity(Equity("Action-14", 14, 1))
        self.actions_repository.add_equity(Equity("Action-15", 18, 3))
        self.actions_repository.add_equity(Equity("Action-16", 8, 8))
        self.actions_repository.add_equity(Equity("Action-17", 4, 12))
        self.actions_repository.add_equity(Equity("Action-18", 10, 14))
        self.actions_repository.add_equity(Equity("Action-19", 24, 21))
        self.actions_repository.add_equity(Equity("Action-20", 114, 18))


if __name__ == "__main__":
    app = App()
    app.populate_equities_with_csv("dataset1_Python+P7.csv")
    result = app.actions_repository.get_best_combination(500)
    print(
        f"{result['equities']}: for profit of {result['profit']} from cost {result['cost']} "
    )
