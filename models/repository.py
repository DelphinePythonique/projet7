from typing import TYPE_CHECKING

from utils import combination_index_list

if TYPE_CHECKING:
    from equity import Equity


class Repository:
    def __init__(self):
        self.equities = []

    def _number_of_equities(self):
        return len(self.equities)

    def _list_of_combination(self):
        return combination_index_list(self._number_of_equities()-1)

    def _list_of_combination_with_profit(self):
        list_of_combination_with_profit = []
        for combination in self._list_of_combination():
            list_of_combination_with_profit.append ({
                'combination': combination,
                'equities': self._get_equities_from_index_tuple(combination),
                'cost': self._get_sum_cost_from_index_tuple(combination),
                'profit': self._get_sum_profit_from_index_tuple(combination)
            })
        return sorted(list_of_combination_with_profit, key=lambda element: element['profit'], reverse=True)

    def _get_equities_from_index_tuple(self, index_tuple):
        return tuple([equity for equity in self.equities if self.equities.index(equity) in index_tuple])

    def _get_sum_profit_from_index_tuple(self, index_tuple):
        return sum([equity.profit for equity in self.equities if self.equities.index(equity) in index_tuple])

    def _get_sum_cost_from_index_tuple(self, index_tuple):
        return sum([equity.cost for equity in self.equities if self.equities.index(equity) in index_tuple])

    def add_equity(self, equity: "Equity"):
        self.equities.append(equity)

    def get_best_combination_by_brute_force(self, max_investment):
        for item in self._list_of_combination_with_profit():
            if item['cost'] < max_investment:
                return item
        return False



