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


def profit_to_percent(cost, profit):
    if cost == 0:
        return 0
    else:
        return 100 * profit / cost


def extract_percent(param):
    return float(param.split("%")[0])


class Equity:
    def __init__(self, name: "string", cost: "float", percent_profit: "float", id: int):
        self.id = id
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

    def populate_equities_with_csv_new(self, csv_enquiries):
        with open(csv_enquiries, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
              self.add_equity(
                    Equity(
                        row["action"],
                        float(row["cost"]),
                        extract_percent(row["percent"]),
                        len(self.equities),
                    )
                )

    def populate_equities_with_csv_old(self, csv_enquiries):
        with open(csv_enquiries, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if float(row["price"]) > 0:
                    self.add_equity(
                        Equity(
                            row["name"],
                            float(row["price"]),
                            float(row["profit"]),
                            len(self.equities),
                        )
                    )

    def _number_of_equities(self):
        return len(self.equities)

    def add_equity(self, equity: "Equity"):
        self.equities.append(equity)

    def get_equities_sorted(self, key):
        return sorted(
            self.equities, key=lambda equity: getattr(equity, key), reverse=True
        )

    @measure
    def get_best_combination(self, max_investment, sorted_key):
        total_profit = 0
        total_cost = 0
        equities = []
        i = 0
        equities_sorted = self.get_equities_sorted(sorted_key)

        while i < len(equities_sorted):
            new_total_cost = total_cost + equities_sorted[i].cost
            if new_total_cost <= max_investment:
                total_cost = new_total_cost
                total_profit += equities_sorted[i].profit
                equities.append(equities_sorted[i])
            i += 1

        return {"equities": tuple(equities), "cost": total_cost, "profit": total_profit}


class App:
    def __init__(self):
        self.actions_repository = Repository()


if __name__ == "__main__":
    app = App()
    app.actions_repository.populate_equities_with_csv_old("dataset1_Python+P7.csv")
    print('there are ', len(app.actions_repository.equities), 'equities')
    result = app.actions_repository.get_best_combination(500, "percent_profit")
    print(
        f"solution by percent_profit for profit of {result['profit']} from cost {result['cost']} "
    )

    print(f"name, id,cost, .percent_profit,profit")
    print(
        "\n".join(
            [
                f"{equities.name}, {equities.id}, {equities.cost}, {equities.percent_profit}, {equities.profit}"
                for equities in result["equities"]
            ]
        )
    )

    result = app.actions_repository.get_best_combination(500, "cost")
    print(
        f":solution by cost: for profit of {result['profit']} from cost {result['cost']} "
    )

    print(f"name, id,cost, .percent_profit,profit")
    print(
        "\n".join(
            [
                f"{equities.name}, {equities.id}, {equities.cost}, {equities.percent_profit}, {equities.profit}"
                for equities in result["equities"]
            ]
        )
    )

    result = app.actions_repository.get_best_combination(500, "profit")
    print(
        f": solution by profit for profit of {result['profit']} from cost {result['cost']} "
    )

    print(f"name, id,cost, .percent_profit,profit")
    print(
        "\n".join(
            [
                f"{equities.name}, {equities.id}, {equities.cost}, {equities.percent_profit}, {equities.profit}"
                for equities in result["equities"]
            ]
        )
    )
