from nicegui import ui
from niceguitest import logic

def init_gui(test_add: logic.myTestAdd) -> None:
    a_input.set_value(str(test_add.a))
    b_input.set_value(str(test_add.b))
    calculate_sum()

def calculate_sum():
    try:
        a = int(a_input.value)
        b = int(b_input.value)
        result = a + b
        result_label.set_text(f"Result: {result}")
    except ValueError:
        result_label.set_text("Please enter valid integers.")

a_input = ui.input(label="First number")
b_input = ui.input(label="Second number")
result_label = ui.label("Result will be shown here.")
ui.button("Calculate", on_click=calculate_sum)