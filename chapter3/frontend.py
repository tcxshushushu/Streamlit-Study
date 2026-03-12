import streamlit as st
from backend import convert, list_quantities, list_units, format_value

quantity = st.sidebar.radio("Select a Quantity", list_quantities())

st.title("Unit Converter")
input_num = float(st.text_input("Value to convert", value="0"))

units = list_units(quantity)
from_unit_col, to_unit_col = st.columns(2)
with from_unit_col:
    from_unit = st.selectbox("From", units)
with to_unit_col:
    to_unit = st.selectbox("To", units, index=1)

places = None
if st.checkbox("Round the result?", value=False): 
    places = st.number_input("Decimal places to round to", min_value=0, value=2)
    

result = convert(quantity, from_unit, to_unit, input_num)
from_display = format_value(input_num, result.from_unit.abbrev)
to_display = format_value(result.to_value, result.to_unit.abbrev, places)
    
from_value_col, to_value_col = st.columns(2)
from_value_col.metric("From", from_display, delta=None)
to_value_col.metric("To", to_display, delta=None)
    