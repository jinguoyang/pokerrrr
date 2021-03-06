# coding: utf-8

from rules.table_rules.base import TableRulesBase
from state.table_state.end import EndState


class LiujuRule(TableRulesBase):
    def condition(self, table):
        if not table.cards_on_desk:
            return True
        else:
            return False

    def action(self, table):
        table.machine.trigger(EndState())
