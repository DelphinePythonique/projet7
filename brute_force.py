# is brute force O(e)
import csv
from time import perf_counter


def measure(func):

    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = perf_counter() - start
            print(f"{func.__name__}  execution time: {end_ if end_ >0 else 0} s")

    return wrapper


def combination_index_list(n):
    list_n = []
    if n == 0:
        return [(0,)]
    else:
        list_minus_one = combination_index_list(n - 1)
        list_n.extend(list_minus_one)
        for combination in list_minus_one:
            combination_format_list = list(combination)
            combination_format_list.append(n)
            list_n.append(tuple(combination_format_list))
        list_n.append((n,))
        return list_n


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

    def _list_of_combination(self):
        return combination_index_list(self._number_of_equities() - 1)

    def _list_of_combination_with_profit(self):
        list_of_combination_with_profit = []
        for combination in self._list_of_combination():
            list_of_combination_with_profit.append(
                {
                    "combination": combination,
                    "equities": self._get_equities_from_index_tuple(combination),
                    "cost": self._get_sum_cost_from_index_tuple(combination),
                    "profit": self._get_sum_profit_from_index_tuple(combination),
                }
            )
        return sorted(
            list_of_combination_with_profit,
            key=lambda element: element["profit"],
            reverse=True,
        )

    def _get_equities_from_index_tuple(self, index_tuple):
        return tuple(
            [
                equity
                for equity in self.equities
                if self.equities.index(equity) in index_tuple
            ]
        )

    def _get_sum_profit_from_index_tuple(self, index_tuple):
        return sum(
            [
                equity.profit
                for equity in self.equities
                if self.equities.index(equity) in index_tuple
            ]
        )

    def _get_sum_cost_from_index_tuple(self, index_tuple):
        return sum(
            [
                equity.cost
                for equity in self.equities
                if self.equities.index(equity) in index_tuple
            ]
        )

    def add_equity(self, equity: "Equity"):
        self.equities.append(equity)

    @measure
    def get_best_combination_by_brute_force(self, max_investment):
        for item in self._list_of_combination_with_profit():
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
    app.populate_equities_with_csv("equities.csv")
    result = app.actions_repository.get_best_combination_by_brute_force(500)
    print(
        f"{result['equities']}: for profit of {result['profit']} from cost {result['cost']} "
    )
