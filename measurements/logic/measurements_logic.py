from ..models import Measurement

def get_variables():
    measurements = Measurement.objects.all()
    return measurements

def get_variable(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_variable(mea_pk, new_var):
    measurement = get_variable(mea_pk)
    measurement.name = new_var["name"]
    measurement.save()
    return measurement

def create_variable(mea):
    measurement = Measurement(name=mea["name"])
    measurement.save()
    return measurement