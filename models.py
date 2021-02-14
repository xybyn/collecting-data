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
    def __init__(self, code, budget_amount, contract_amount, total_fed_amount, gr_contract_amount, women_amount):
        self.code = code
        self.budget_amount = budget_amount
        self.contract_amount = contract_amount
        self.total_fed_amount = total_fed_amount
        self.gr_contract_amount = gr_contract_amount
        self.women_amount = women_amount


class TableRowP2121:
    def __init__(self, code):
        self.code = code


class TableRowP2124:
    def __init__(self, code, total_fed_amount, contract_amount, women_amount):
        self.code = code
        self.total_fed_amount = total_fed_amount
        self.contract_amount = contract_amount
        self.women_amount = women_amount


class TableRowP213:
    def __init__(self, code, total_grad_amount, magistracy_amount, total_fed_amount, contract_amount,
                 women_amount):
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
        self.table_row_p12 = []


class Subject:
    def __init__(self, code, budget_amount_p211, contract_amount_p211, total_fed_amount_p211, gr_contract_amount_p211,
                 women_amount_p211, total_fed_amount_p2124, contract_amount_p2124, women_amount_p2124, 
                 total_grad_amount_p213, magistracy_amount_p213, total_fed_amount_p213, contract_amount_p213,
                 women_amount_p213):

        self.code = code

        self.budget_amount_p211 = budget_amount_p211
        self.contract_amount_p211 = contract_amount_p211
        self.total_fed_amount_p211 = total_fed_amount_p211
        self.gr_contract_amount_p211 = gr_contract_amount_p211
        self.women_amount_p211 = women_amount_p211

        self.total_fed_amount_p2124 = total_fed_amount_p2124
        self.contract_amount_p2124 = contract_amount_p2124
        self.women_amount_p2124 = women_amount_p2124

        self.total_grad_amount_p213 = total_grad_amount_p213
        self.magistracy_amount_p213 = magistracy_amount_p213
        self.total_fed_amount_p213 = total_fed_amount_p213
        self.contract_amount_p213 = contract_amount_p213
        self.women_amount_p213 = women_amount_p213


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
            "code": obj.code,
            "budget_amount": obj.budget_amount,
            "contract_amount": obj.contract_amount,
            "total_fed_amount": obj.total_fed_amount,
            "gr_contract_amount": obj.gr_contract_amount,
            "women_amount": obj.women_amount
        }
    if isinstance(obj, TableRowP2121):
        return {
            "code": obj.code
        }

    if isinstance(obj, TableRowP2124):
        return {
            "code": obj.code,
            "contract_amount": obj.contract_amount,
            "total_fed_amount": obj.total_fed_amount,
            "women_amount": obj.women_amount
        }

    if isinstance(obj, TableRowP213):
        return {
            "code": obj.code,
            "total_grad_amount": obj.total_grad_amount,
            "magistracy_amount": obj.magistracy_amount,
            "total_fed_amount": obj.total_fed_amount,
            "contract_amount": obj.contract_amount,
            "women_amount": obj.women_amount
        }

    if isinstance(obj, TableRowP212):
        return {
            "graduation_type": obj.graduation_type,
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
    
    if isinstance(obj, Subject):
        return {
           "code": obj.code,

            "self.budget_amount_p211": obj.budget_amount_p211,
            "self.contract_amount_p211": obj.contract_amount_p211,
            "self.total_fed_amount_p211": obj.total_fed_amount_p211,
            "self.gr_contract_amount_p211": obj.gr_contract_amount_p211,
            "self.women_amount_p211": obj.women_amount_p211,

            "self.total_fed_amount_p2124": obj.total_fed_amount_p2124,
            "self.contract_amount_p2124": obj.contract_amount_p2124,
            "self.women_amount_p2124": obj.women_amount_p2124,

            "self.total_grad_amount_p213": obj.total_grad_amount_p213,
            "self.magistracy_amount_p213": obj.magistracy_amount_p213,
            "self.total_fed_amount_p213": obj.total_fed_amount_p213,
            "self.contract_amount_p213": obj.contract_amount_p213,
            "self.women_amount_p213": obj.women_amount_p213
        }
