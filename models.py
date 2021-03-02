class Year:
    def __init__(self, year):
        self.year = year
        self.areas = []


class Area:
    def __init__(self, name):
        self.name = name
        self.institutes = []


class Institute:
    def __init__(self, name):
        self.name = name
        self.indicators = []
        self.directions = []


class Indicator:
    def __init__(self, indicator, value):
        self.indicator = indicator
        self.value = value


class Direction:
    def __init__(self, direction):
        self.direction = direction


class TableRowP211:
    def __init__(self, code, budget_amount=0, contract_amount=0, total_fed_amount=0, gr_contract_amount=0,
                 women_amount=0):
        self.code = code
        self.budget_amount = budget_amount
        self.contract_amount = contract_amount
        self.total_fed_amount = total_fed_amount
        self.gr_contract_amount = gr_contract_amount
        self.women_amount = women_amount


class TableRowP2121:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class TableRowOldP211:
    def __init__(self, name, code, total_amount=0, total_fed_amount=0, contract_amount=0):
        self.name = name
        self.code = code
        self.total_amount = total_amount
        self.total_fed_amount = total_fed_amount
        self.contract_amount = contract_amount


class TableRowOldP212:
    def __init__(self, name, classification, code, total_fed_amount=0, contract_amount=0):
        self.name = name
        self.classification = classification
        self.code = code
        self.total_fed_amount = total_fed_amount
        self.contract_amount = contract_amount


class TableRowOldP212P:
    def __init__(self, name, classification, code, total_fed_amount=0, contract_amount=0, women_amount=0):
        self.name = name
        self.classification = classification
        self.code = code
        self.total_fed_amount = total_fed_amount
        self.contract_amount = contract_amount
        self.women_amount = women_amount


class TableRowOldP25:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class TableRowOldP210:
    def __init__(self, country, row_number, code, accepted_students_amount, a_fed_budget, a_rf_budget,
                 total_students_amount, t_fed_budget, t_rf_budget,
                 grad_students_amount, g_fed_budget, g_rf_budget):
        self.country = country
        self.row_number = row_number
        self.code = code
        self.accepted_students_amount = accepted_students_amount
        self.a_fed_budget = a_fed_budget
        self.a_rf_budget = a_rf_budget
        self.total_students_amount = total_students_amount
        self.t_fed_budget = t_fed_budget
        self.t_rf_budget = t_rf_budget
        self.grad_students_amount = grad_students_amount
        self.g_fed_budget = g_fed_budget
        self.g_rf_budget = g_rf_budget


class TableRowP2124:
    def __init__(self, code, total_fed_amount=0, contract_amount=0, women_amount=0):
        self.code = code
        self.total_fed_amount = total_fed_amount
        self.contract_amount = contract_amount
        self.women_amount = women_amount


class TableRowP213:
    def __init__(self, code, total_grad_amount=0, magistracy_amount=0, total_fed_amount=0, contract_amount=0,
                 women_amount=0):
        self.code = code
        self.total_grad_amount = total_grad_amount
        self.magistracy_amount = magistracy_amount
        self.total_fed_amount = total_fed_amount
        self.contract_amount = contract_amount
        self.women_amount = women_amount


class TableRowP212:
    def __init__(self, graduation_type, country, row_number, code, accepted_students_amount, a_fed_budget, a_rf_budget,
                 a_local_budget, a_contract_amount, total_students_amount, t_fed_budget, t_rf_budget, t_local_budget,
                 t_contract_amount, grad_students_amount, g_fed_budget, g_rf_budget, g_local_budget, g_contract_amount):
        self.graduation_type = graduation_type
        self.country = country
        self.row_number = row_number
        self.code = code
        self.accepted_students_amount = accepted_students_amount
        self.a_fed_budget = a_fed_budget
        self.a_rf_budget = a_rf_budget
        self.a_local_budget = a_local_budget
        self.a_contract_amount = a_contract_amount
        self.total_students_amount = total_students_amount
        self.t_fed_budget = t_fed_budget
        self.t_rf_budget = t_rf_budget
        self.t_local_budget = t_local_budget
        self.t_contract_amount = t_contract_amount
        self.grad_students_amount = grad_students_amount
        self.g_fed_budget = g_fed_budget
        self.g_rf_budget = g_rf_budget
        self.g_local_budget = g_local_budget
        self.g_contract_amount = g_contract_amount


class AreaVPO:
    def __init__(self, name):
        self.name = name
        self.subjects = []
        self.bachelor = []
        self.spec = []
        self.magistracy = []


class Subject:
    def __init__(self, code, p211, p2124, p213):
        self.p211 = p211
        self.p2124 = p2124
        self.p213 = p213
        self.code = code


class OldSubject:
    def __init__(self, code, old_p211, old_p212, old_p212P):
        self.old_p211 = old_p211
        self.old_p212 = old_p212
        self.old_p212P = old_p212P
        self.code = code


class AreaOldVPO:
    def __init__(self, name):
        self.name = name
        self.old_subjects = []
        self.old_p25 = []
        self.old_p210 = []


def my_default(obj):
    if isinstance(obj, Area):
        return {
            "name": obj.name,
            "institutes": obj.institutes
        }
    if isinstance(obj, Institute):
        return {
            "name": obj.name,
            "indicators": obj.indicators,
            "directions": obj.directions
        }
    if isinstance(obj, Indicator):
        return {
            "indicator": obj.indicator,
            "value": obj.value
        }
    if isinstance(obj, Direction):
        return {
            "direction": obj.direction

        }
    if isinstance(obj, Year):
        return {
            "year": obj.year,
            "areas": obj.areas

        }
    if isinstance(obj, TableRowP211):
        return {
            "budget_amount": obj.budget_amount,
            "contract_amount": obj.contract_amount,
            "total_fed_amount": obj.total_fed_amount,
            "gr_contract_amount": obj.gr_contract_amount,
            "women_amount": obj.women_amount
        }

    if isinstance(obj, TableRowP2124):
        return {
            "contract_amount": obj.contract_amount,
            "total_fed_amount": obj.total_fed_amount,
            "women_amount": obj.women_amount
        }

    if isinstance(obj, TableRowP213):
        return {
            "total_grad_amount": obj.total_grad_amount,
            "magistracy_amount": obj.magistracy_amount,
            "total_fed_amount": obj.total_fed_amount,
            "contract_amount": obj.contract_amount,
            "women_amount": obj.women_amount
        }

    if isinstance(obj, AreaVPO):
        return {
            "name": obj.name,
            "subjects": obj.subjects,
            "bachelor": obj.bachelor,
            "spec": obj.spec,
            "magistracy": obj.magistracy
        }

    if isinstance(obj, AreaOldVPO):
        return {
            "name": obj.name,
            "subjects": obj.old_subjects,
            "old_p25": obj.old_p25,
            "old_p210": obj.old_p210
        }

    if isinstance(obj, Subject):
        return {
            "code": obj.code,
            "p211": obj.p211,
            "p2124": obj.p2124,
            "p213": obj.p213,
        }

    if isinstance(obj, OldSubject):
        return {
            "code": obj.code,
            "old_p211": obj.old_p211,
            "old_p212": obj.old_p212,
            "old_p212P": obj.old_p212P,
        }

    if isinstance(obj, TableRowP212):
        return {
            "country": obj.country,
            "row_number": obj.row_number,
            "code": obj.code,
            "accepted_students_amount": obj.accepted_students_amount,
            "a_fed_budget": obj.a_fed_budget,
            "a_rf_budget": obj.a_rf_budget,
            "a_local_budget": obj.a_local_budget,
            "a_contract_amount": obj.a_contract_amount,
            "total_students_amount": obj.total_students_amount,
            "t_fed_budget": obj.t_fed_budget,
            "t_rf_budget": obj.t_rf_budget,
            "t_local_budget": obj.t_local_budget,
            "t_contract_amount": obj.t_contract_amount,
            "grad_students_amount": obj.grad_students_amount,
            "g_fed_budget": obj.g_fed_budget,
            "g_rf_budget": obj.g_rf_budget,
            "g_local_budget": obj.g_local_budget,
            "g_contract_amount": obj.g_contract_amount
        }

    if isinstance(obj, TableRowP2121):
        return {
            "name": obj.name,
            "code": obj.code
        }

    if isinstance(obj, TableRowOldP211):
        return {
            "name": obj.name,
            "code": obj.code,
            "total_amount": obj.total_amount,
            "total_fed_amount": obj.total_fed_amount,
            "contract_amount": obj.contract_amount
        }

    if isinstance(obj, TableRowOldP212):
        return {
            "name": obj.name,
            "classification": obj.classification,
            "code": obj.code,
            "total_fed_amount": obj.total_fed_amount,
            "contract_amount": obj.contract_amount
        }

    if isinstance(obj, TableRowOldP212P):
        return {
            "name": obj.name,
            "classification": obj.classification,
            "code": obj.code,
            "total_fed_amount": obj.total_fed_amount,
            "contract_amount": obj.contract_amount,
            "women_amount": obj.women_amount,
        }

    if isinstance(obj, TableRowOldP25):
        return {
            "name": obj.name,
            "code": obj.amount
        }

    if isinstance(obj, TableRowOldP210):
        return {
            "country": obj.country,
            "row_number": obj.row_number,
            "code": obj.code,
            "accepted_students_amount": obj.accepted_students_amount,
            "a_fed_budget": obj.a_fed_budget,
            "a_rf_budget": obj.a_rf_budget,
            "total_students_amount": obj.total_students_amount,
            "t_fed_budget": obj.t_fed_budget,
            "t_rf_budget": obj.t_rf_budget,
            "grad_students_amount": obj.grad_students_amount,
            "g_fed_budget": obj.g_fed_budget,
            "g_rf_budget": obj.g_rf_budget,
        }
