class TableRowP211SPO:
    def __init__(self, name, str_number, code, budget_amount, contract_amount, total_accepted, disabled_accepted,
                 basic_level_amount, advanced_level, total_fed_amount, disabled_fed_amount, total_subject_amount,
                 disabled_subject_amount, local_budget_amount, budget_contract_amount, women_amount):
        self.name = name
        self.str_number = str_number
        self.code = code
        self.budget_amount = budget_amount
        self.contract_amount = contract_amount
        self.total_accepted = total_accepted
        self.disabled_accepted = disabled_accepted
        self.basic_level_amount = basic_level_amount
        self.advanced_level = advanced_level
        self.total_fed_amount = total_fed_amount
        self.disabled_fed_amount = disabled_fed_amount
        self.total_subject_amount = total_subject_amount
        self.disabled_subject_amount = disabled_subject_amount
        self.local_budget_amount = local_budget_amount
        self.budget_contract_amount = budget_contract_amount
        self.women_amount = women_amount


class YearSPO:
    def __init__(self, year):
        self.year = year
        self.areas = []


class TableRowP2121SPO:
    def __init__(self, name, str_number, code):
        self.name = name
        self.str_number = str_number
        self.code = code


class TableRowP2124SPO:
    def __init__(self, name, total_accepted, disabled_accepted, basic_level_amount, advanced_level, total_fed_amount,
                 disabled_fed_amount, total_subject_amount, disabled_subject_amount, local_budget_amount,
                 contract_amount, women_amount, targeted_education):
        self.name = name
        self.total_accepted = total_accepted
        self.disabled_accepted = disabled_accepted
        self.basic_level_amount = basic_level_amount
        self.advanced_level = advanced_level
        self.total_fed_amount = total_fed_amount
        self.disabled_fed_amount = disabled_fed_amount
        self.total_subject_amount = total_subject_amount
        self.disabled_subject_amount = disabled_subject_amount
        self.local_budget_amount = local_budget_amount
        self.contract_amount = contract_amount
        self.women_amount = women_amount
        self.targeted_education = targeted_education


class TableRowP2141SPO:
    def __init__(self, name, str_number, code, serial_number, total_amount, total_fed_amount, total_subject_amount,
                 local_budget_amount, legal_representative_amount, individual_amount, legal_entity_amount):
        self.name = name
        self.str_number = str_number
        self.code = code
        self.serial_number = serial_number
        self.total_amount = total_amount
        self.total_fed_amount = total_fed_amount
        self.total_subject_amount = total_subject_amount
        self.local_budget_amount = local_budget_amount
        self.legal_representative_amount = legal_representative_amount
        self.individual_amount = individual_amount
        self.legal_entity_amount = legal_entity_amount


class TableRowP2142SPO:
    def __init__(self, name, str_number, code, serial_number, women_amount, accelerated_learning, total_disabled_amount,
                 disabled_amount, disabled_children_amount, excepted_disabled, excepted_disabled_children):
        self.name = name
        self.str_number = str_number
        self.code = code
        self.serial_number = serial_number
        self.women_amount = women_amount
        self.accelerated_learning = accelerated_learning
        self.total_disabled_amount = total_disabled_amount
        self.disabled_amount = disabled_amount
        self.disabled_children_amount = disabled_children_amount
        self.excepted_disabled = excepted_disabled
        self.excepted_disabled_children = excepted_disabled_children


class AreaSPO:
    def __init__(self, name):
        self.name = name
        self.p211 = []
        self.p2121 = []
        self.p2124 = []
        self.p2141 = []
        self.p2142 = []


class AreaOldSPO:
    def __init__(self, name):
        self.name = name
        self.p211 = []
        self.p212 = []
        self.p2122 = []
        self.p27 = []


class TableRowP211OldSPO:
    def __init__(self, name, str_number, code, applications_submitted, total_accepted, basic_level_amount,
                 advanced_level, fed_accepted, subject_budget_accepted, local_budget_accepted, full_refund):
        self.name = name
        self.str_number = str_number
        self.code = code
        self.applications_submitted = applications_submitted
        self.total_accepted = total_accepted
        self.basic_level_amount = basic_level_amount
        self.advanced_level = advanced_level
        self.fed_accepted = fed_accepted
        self.subject_budget_accepted = subject_budget_accepted
        self.local_budget_accepted = local_budget_accepted
        self.full_refund = full_refund


class TableRowP212OldSPO:
    def __init__(self, name, str_number, code, total_course_1, budget_course_1, total_course_2, budget_course_2,
                 total_course_3, budget_course_3, total_course_4, budget_course_4, total_course_5, budget_course_5,
                 total_student_amount, total_course_6, budget_course_6):
        self.name = name
        self.str_number = str_number
        self.code = code
        self.total_course_1 = total_course_1
        self.budget_course_1 = budget_course_1
        self.total_course_2 = total_course_2
        self.budget_course_2 = budget_course_2
        self.total_course_3 = total_course_3
        self.budget_course_3 = budget_course_3
        self.total_course_4 = total_course_4
        self.budget_course_4 = budget_course_4
        self.total_course_5 = total_course_5
        self.budget_course_5 = budget_course_5
        self.total_course_6 = total_course_6
        self.budget_course_6 = budget_course_6
        self.total_student_amount = total_student_amount


class TableRowP2122OldSPO:
    def __init__(self, name, str_number, code, basic_graduated, advanced_graduated, total_graduated):
        self.name = name
        self.str_number = str_number
        self.code = code
        self.basic_graduated = basic_graduated
        self.advanced_graduated = advanced_graduated
        self.total_graduated = total_graduated


class TableRowP27OldSPO:
    def __init__(self, name, str_number, country_code, total_accepted, budget_accepted, subject_budget_accepted,
                 full_refund_accepted, total_amount, budget_amount, subject_budget_amount, full_refund_amount,
                 total_graduated, budget_graduated, subject_budget_graduated, full_refund_graduated):
        self.name = name
        self.str_number = str_number
        self.country_code = country_code

        self.total_accepted = total_accepted
        self.fed_budget_accepted = budget_accepted
        self.subject_budget_accepted = subject_budget_accepted
        self.full_refund_accepted = full_refund_accepted

        self.total_amount = total_amount
        self.fed_budget_amount = budget_amount
        self.subject_budget_amount = subject_budget_amount
        self.full_refund_amount = full_refund_amount

        self.total_graduated = total_graduated
        self.fed_budget_graduated = budget_graduated
        self.subject_budget_graduated = subject_budget_graduated
        self.full_refund_graduated = full_refund_graduated


def my_default_SPO(obj):
    if isinstance(obj, TableRowP211SPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code,
            "budget_amount": obj.budget_amount,
            "contract_amount": obj.contract_amount,
            "total_accepted": obj.total_accepted,
            "disabled_accepted": obj.disabled_accepted,
            "basic_level_amount": obj.basic_level_amount,
            "advanced_level": obj.advanced_level,
            "total_fed_amount": obj.total_fed_amount,
            "disabled_fed_amount": obj.disabled_fed_amount,
            "total_subject_amount": obj.total_subject_amount,
            "disabled_subject_amount": obj.disabled_subject_amount,
            "local_budget_amount": obj.local_budget_amount,
            "budget_contract_amount": obj.budget_contract_amount,
            "women_amount": obj.women_amount
        }

    if isinstance(obj, TableRowP2121SPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code
        }

    if isinstance(obj, TableRowP2124SPO):
        return {
            "name": obj.name,
            "total_accepted": obj.total_accepted,
            "disabled_accepted": obj.disabled_accepted,
            "basic_level_amount": obj.basic_level_amount,
            "advanced_level": obj.advanced_level,
            "total_fed_amount": obj.total_fed_amount,
            "disabled_fed_amount": obj.disabled_fed_amount,
            "total_subject_amount": obj.total_subject_amount,
            "disabled_subject_amount": obj.disabled_subject_amount,
            "local_budget_amount": obj.local_budget_amount,
            "contract_amount": obj.contract_amount,
            "women_amount": obj.women_amount,
            "targeted_education": obj.targeted_education
        }

    if isinstance(obj, TableRowP2141SPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code,
            "serial_number": obj.serial_number,
            "total_amount": obj.total_amount,
            "total_fed_amount": obj.total_fed_amount,
            "total_subject_amount": obj.total_subject_amount,
            "local_budget_amount": obj.local_budget_amount,
            "legal_representative_amount": obj.legal_representative_amount,
            "individual_amount": obj.individual_amount,
            "legal_entity_amount": obj.legal_entity_amount
        }

    if isinstance(obj, TableRowP2142SPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code,
            "serial_number": obj.serial_number,
            "women_amount": obj.women_amount,
            "accelerated_learning": obj.accelerated_learning,
            "total_disabled_amount": obj.total_disabled_amount,
            "disabled_amount": obj.disabled_amount,
            "disabled_children_amount": obj.disabled_children_amount,
            "excepted_disabled": obj.excepted_disabled,
            "excepted_disabled_children": obj.excepted_disabled_children
        }

    if isinstance(obj, AreaSPO):
        return {
            "name": obj.name,
            "p211": obj.p211,
            "p2121": obj.p2121,
            "p2124": obj.p2124,
            "p2141": obj.p2141,
            "p2142": obj.p2142
        }

    if isinstance(obj, YearSPO):
        return {
            "year": obj.year,
            "areas": obj.areas
        }

    if isinstance(obj, AreaOldSPO):
        return {
            "name": obj.name,
            "p211": obj.p211,
            "p212": obj.p212,
            "p2122": obj.p2122,
            "p27": obj.p27,
        }

    if isinstance(obj, TableRowP211OldSPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code,
            "applications_submitted": obj.applications_submitted,
            "total_accepted": obj.total_accepted,
            "basic_level_amount": obj.basic_level_amount,
            "advanced_level": obj.advanced_level,
            "fed_accepted": obj.fed_accepted,
            "subject_budget_accepted": obj.subject_budget_accepted,
            "local_budget_accepted": obj.local_budget_accepted,
            "full_refund": obj.full_refund
        }

    if isinstance(obj, TableRowP212OldSPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code,
            "total_course_1": obj.total_course_1,
            "budget_course_1": obj.budget_course_1,
            "total_course_2": obj.total_course_2,
            "budget_course_2": obj.budget_course_2,
            "total_course_3": obj.total_course_3,
            "budget_course_3": obj.budget_course_3,
            "total_course_4": obj.total_course_4,
            "budget_course_4": obj.budget_course_4,
            "total_course_5": obj.total_course_5,
            "budget_course_5": obj.budget_course_5,
            "total_course_6": obj.total_course_6,
            "budget_course_6": obj.budget_course_6,
            "total_student_amount": obj.total_student_amount
        }

    if isinstance(obj, TableRowP2122OldSPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "code": obj.code,
            "basic_graduated": obj.basic_graduated,
            "advanced_graduated": obj.advanced_graduated,
            "total_graduated": obj.total_graduated
        }

    if isinstance(obj, TableRowP27OldSPO):
        return {
            "name": obj.name,
            "str_number": obj.str_number,
            "country_code": obj.country_code,
            "total_accepted": obj.total_accepted,
            "fed_budget_accepted": obj.fed_budget_accepted,
            "subject_budget_accepted": obj.subject_budget_accepted,
            "full_refund_accepted": obj.full_refund_accepted,
            "total_amount": obj.total_amount,
            "fed_budget_amount": obj.fed_budget_amount,
            "subject_budget_amount": obj.subject_budget_amount,
            "full_refund_amount": obj.full_refund_amount,
            "total_graduated": obj.total_graduated,
            "fed_budget_graduated": obj.fed_budget_graduated,
            "subject_budget_graduated": obj.subject_budget_graduated,
            "full_refund_graduated": obj.full_refund_graduated,
        }
