from pydantic import BaseModel, Field
from typing import Literal, Annotated

class UserInput(BaseModel):
    Age: Annotated[int, Field(..., gt=0, lt=120)]
    BMI: Annotated[Literal['Normal', 'Overweight', 'Underweight','Obese'], Field(...)]
    menstrual_regularity: Annotated[Literal['Regular', 'Irregular'], Field(..., alias='Menstrual Regularity')]
    hirsutism: Annotated[Literal['Yes', 'No'], Field(..., alias='Hirsutism')]
    acne_severity: Annotated[Literal['Unknown', 'Mild', 'Moderate', 'Severe'], Field(..., alias='Acne Severity')]
    family_history_of_pcos: Annotated[Literal['Yes', 'No'], Field(..., alias='Family History of PCOS')]
    insulin_resistance: Annotated[Literal['Yes', 'No'], Field(..., alias='Insulin Resistance')]
    stress_levels: Annotated[Literal['Low', 'Medium', 'High'], Field(..., alias='Stress Levels')]
    urban_or_rural: Annotated[Literal['Urban', 'Rural'], Field(..., alias='Urban/Rural')]
    socioeconomic_status: Annotated[Literal['Low', 'Middle', 'High'], Field(..., alias='Socioeconomic Status')]

    class Config:
        allow_population_by_field_name = True  # lets you use Pythonic names as well