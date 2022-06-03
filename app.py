from models.repository import Repository
from models.equity import Equity


class App:
    def __init__(self):
        self.actions_repository = Repository()

    def populate_enquiries(self):
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
    app.populate_enquiries()
    result = app.actions_repository.get_best_combination_by_brute_force(500)
    print(f"{result['equities']}: for profit of {result['profit']} from cost {result['cost']} ")
