import debts

def json_defaults(obj):
    if isinstance(obj,debts.Debt):
        return {'__Debt__' :True, 'name': obj.name,
                'total': obj.total, 'monthly_payment': obj.monthly_payment,
                'target_payment': obj.target_payment,
                'months_left': obj.months_left}
    raise TypeError(f'Cannot serialize object of {type(obj)}')


def json_object_hook(json_dict):
    if '__Debt__' in json_dict:
        return