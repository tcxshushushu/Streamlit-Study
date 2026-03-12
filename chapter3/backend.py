from unit_config import unit_config
from result import Result 
from typing import List

def list_quantities() -> List[str]:
    return list(unit_config.keys())

def list_units(quantity_name: str) -> List[str]:
    return list(unit_config[quantity_name].units.keys())

def convert(quantity_name: str, from_unit_name: str, to_unit_name: str, value: float) -> Result:
    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]

    # Convert the input value to the standard unit
    value_in_std_unit = value * from_unit.value_in_std_unit

    # Convert from the standard unit to the target unit
    converted_value = value_in_std_unit / to_unit.value_in_std_unit

    return Result(
        from_unit=from_unit,
        to_unit=to_unit,
        from_value=value,
        to_value=converted_value
    )
    
def format_value(value: float, unit_abbrev: str, decimal_places: int = None) -> str:
    is_round = decimal_places is not None
    rounded = round(value, decimal_places) if is_round else value
    formatted = format(rounded, ",")
    return f"{formatted} {unit_abbrev}"