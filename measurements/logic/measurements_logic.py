from ..models import Measurement
import variables.logic.variables_logic as vg

def get_variables():
    measurements = Measurement.objects.all()
    return measurements

def get_variable(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_variable(mea_pk, new_mea):
    measurement = get_variable(mea_pk)
    measurement.unit = new_mea["unit"]
    measurement.value = new_mea["value"]
    measurement.save()
    return measurement

def create_variable(mea):
    measurement = Measurement(variable=vg.get_variable(mea["variable"]),
                              unit= mea["unit"],
                              value= mea["value"])
    measurement.save()
    return measurement