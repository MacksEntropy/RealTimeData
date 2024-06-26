from pydantic import BaseModel, Field


class ChemicalLevels(BaseModel):
    """Model for chemical level measurements"""
    H2S_level: float = Field(..., lt=4, description="ppm")
    H2O_level: float = Field(..., lt=120, description="ppm")
    CO2_level: float = Field(..., lt=3.0, description="Percent of volume")

class Measurement(BaseModel):
    """Model containing data collected from a sensor"""
    temperature: float = Field(..., gt=10.0, lt=16.0, description="Degrees Fahrenheit")
    preassure: float = Field(..., gt=200, lt=1500, description="Psi")
    btu_measurement: float = Field(..., gt=1000, description="Btu")
    sensor_id: int = Field(..., ge=1, lt=100) 
    chemical_measurements: ChemicalLevels


if __name__ == "__main__":

    dummy_cls = {
        "H2S_level" : 2,
        "H2O_level" : 70,
        "CO2_level" : 1.2
    }

    dummy_measurement = {
        "temperature" : 14.2,
        "preassure" : 750,
        "chemical_measurements" : dummy_cls,
        "btu_measurement" : 2000.8,
        "sensor_id" : 50
    }
    m = Measurement(**dummy_measurement)
    print("Success")