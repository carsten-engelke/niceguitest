# This file is the main entry point for the GUI version of the niceguitest package. It defines a simple NiceGUI application that allows users to input two numbers and see their sum. The logic for the addition is defined in the logic.py module, and this file focuses on setting up the GUI and handling user interactions.
from niceguitest.logic import myTestAdd

def main() -> None:
    print("Empty main function due to problems with multiprocessing and nicegui. Please run the GUI app using the cli entry point instead.")

def run_gui_app(ui) -> None:
    from niceguitest import logic
    ui.label("Please enter two numbers to add:")
    a_input = ui.input(label="First number")
    b_input = ui.input(label="Second number")
    result_label = ui.label("Result will be shown here.")
    ui.button("Calculate", on_click=lambda: calculate_sum(a_input, b_input, result_label))
    ui.run()

def calculate_sum(a_input, b_input, result_label) -> None:
    try:
        a = int(a_input.value)
        b = int(b_input.value)
        result = myTestAdd(a, b).add()
        result_label.set_text(f"Result: {result}")
    except ValueError:
        result_label.set_text("Please enter valid integers.")

# This entry point is used when the user runs the command "niceguitest-gui" after installing the package with the "gui" extra.
try:
    from nicegui import ui
    run_gui_app(ui)
except ImportError:
    print("NiceGUI is not installed. Please install the 'gui' extra to use the GUI features with 'pip install niceguitest[gui]' .")
    from niceguitest.cli import main as cli_main
    cli_main()