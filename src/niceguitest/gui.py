# This file is the main entry point for the GUI version of the niceguitest package. It defines a simple NiceGUI application that allows users to input two numbers and see their sum. The logic for the addition is defined in the logic.py module, and this file focuses on setting up the GUI and handling user interactions.
from niceguitest.logic import myTestAdd

def main() -> None:
    # This entry point is used when the user runs the command "niceguitest-gui" after installing the package with the "gui" extra.
    try:
        from nicegui import ui
        run_gui_app(ui, reload=False)
    except ImportError:
        # Fallback to CLI if NiceGUI is not installed, which allows the user to still use the application without the GUI features. It also provides a helpful message about how to install the GUI features.
        print("NiceGUI is not installed. Please install the 'gui' extra to use the GUI features with 'pip install niceguitest[gui]' .")
        from niceguitest.cli import main as cli_main
        cli_main()

def run_gui_app(ui, reload: bool = False) -> None:
    # Necessary workaround to allow the use of NiceGUI's reload feature which does not work when starting the app from an entry point in pyproject.toml.
    print("Starting NiceGUI app using a root function with reload =", reload)
    ui.run(reload=reload, root=lambda: setup_gui(ui))

def setup_gui(ui) -> None:
    # root function that sets up the GUI layout and components. Workaround for the fact that NiceGUI's reload feature only works with a root function. 
    ui.label("Please enter two numbers to add:")
    a_input = ui.input(label="First number")
    b_input = ui.input(label="Second number")
    result_label = ui.label("Result will be shown here.")
    ui.button("Calculate", on_click=lambda: calculate_sum(a_input, b_input, result_label))

def calculate_sum(a_input, b_input, result_label) -> None:
    # Example logical function that takes two inputs, converts them to integers, and updates the result label with the sum. It also handles invalid input by showing an error message.
    try:
        a = int(a_input.value)
        b = int(b_input.value)
        result = myTestAdd(a, b).add()
        result_label.set_text(f"Result: {result}")
    except ValueError:
        result_label.set_text("Please enter valid integers.")

if __name__ in {'__main__', '__mp_main__'}:
    #This is called when the user runs the command "python -m niceguitest.gui" to start the GUI application. Here you can use the reload feature of NiceGUI for development purposes, which allows you to see changes in real-time without restarting the app. In production, you would typically set reload to False for better performance.
    try:
        from nicegui import ui
        run_gui_app(ui, reload=True)
    except ImportError:
        print("NiceGUI is not installed. Please install the 'gui' extra to use the GUI features with 'pip install niceguitest[gui]' .")
        from niceguitest.cli import main as cli_main
        cli_main()