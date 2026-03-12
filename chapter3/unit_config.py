from typing import Dict

from quantity import Quantity
from unit import Unit

unit_config : Dict[str, Quantity] = {
    "Mass" : Quantity(
        std_unit = "Kilograms",
        units={
            "Kilograms" : Unit(abbrev="kg", value_in_std_unit=1.0),
            "Grams" : Unit(abbrev="g", value_in_std_unit=0.001),
            "Pounds" : Unit(abbrev="lb", value_in_std_unit=0.453592),
            "Ounces" : Unit(abbrev="oz", value_in_std_unit=0.0283495),
            # Add more mass units as needed
        }
    ),
    "Length" : Quantity(
        std_unit = "Meters",
        units={
            "Meters" : Unit(abbrev="m", value_in_std_unit=1.0),
            "Centimeters" : Unit(abbrev="cm", value_in_std_unit=0.01),
            "Inches" : Unit(abbrev="in", value_in_std_unit=0.0254),
            "Feet" : Unit(abbrev="ft", value_in_std_unit=0.3048),
            # Add more length units as needed
        }
    ),
    "Time" : Quantity(
        std_unit = "Seconds",
        units={
            "Seconds" : Unit(abbrev="s", value_in_std_unit=1.0),
            "Minutes" : Unit(abbrev="min", value_in_std_unit=60.0),
            "Hours" : Unit(abbrev="hr", value_in_std_unit=3600.0),
            "Days" : Unit(abbrev="d", value_in_std_unit=86400.0),
            # Add more time units as needed
        }
    )
}