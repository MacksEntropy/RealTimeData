from pydantic import BaseModel, validator, PositiveInt, Field
from datetime import datetime


class PhysicalMeasurement(BaseModel):
    time: datetime
    preassure: PositiveInt
    chemical_measurements: dict[str, PositiveInt] # H2S_level and CO2_level
    BTU_measurement: float


if __name__ == "__main__":

    chem_measurement = {
        "H2S_level" : 25,
        "CO2_level" : 12
    }

    print("hello")
    x = PhysicalMeasurement(time=datetime.now(), preassure=1, chemical_measurements=chem_measurement, BTU_measurement=0.1)