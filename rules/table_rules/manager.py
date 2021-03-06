# coding: utf-8

from utils.singleton import Singleton
from rules.define import *


class TableRulesManager(object):
    __metaclass__ = Singleton

    def __init__(self):
        from rules.table_rules.settle_for_round import SettleForRoundRule

        self.rules = {
            TABLE_RULE_READY: [],
            TABLE_RULE_DEAL: [],
            TABLE_RULE_STEP: [],
            TABLE_RULE_END: [],
            TABLE_RULE_SETTLE_FOR_ROUND: [SettleForRoundRule()],
        }

    def condition(self, table, rule_type):
        if rule_type not in self.rules.keys():
            table.logger.warn("table {0} rule {1} not exist".format(table.room_id, rule_type))
            return

        for rule in self.rules[rule_type]:
            if rule.condition(table):
                rule.action(table)
                return
        table.machine.cur_state.next_state(table)
