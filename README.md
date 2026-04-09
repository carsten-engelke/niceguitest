Demonstration of nicegui failure to be called by Entry Points.

SOLUTION: When using an entry point to start nicegui app set reload=False. Also load the ui in a root function as reload=False triggers an internal server error otherwise.
Now working!

Steps to perform:

    mkdir niceguitest
    cd niceguitest
    uv init --package

Create files in src/niceguitest:

logic.py

    class myTestAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
cli.py

    from niceguitest import logic
    
    def main() -> None:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"Result: {logic.myTestAdd(a, b).add()}")

    if __name__ == "__main__":
        main()

gui.py

    # This file is the main entry point for the GUI version of the niceguitest package. It defines a simple NiceGUI application that allows users to input two numbers and see their sum. The logic for the addition is defined in the logic.py module, and this file focuses on setting up the GUI and handling user interactions.
    from niceguitest.logic import myTestAdd

    def main() -> None:
        # This entry point is used when the user runs the command "niceguitest-gui" after installing the package with the "gui" extra.
        try:
            from nicegui import ui
            run_gui_app(ui)
        except ImportError:
            print("NiceGUI is not installed. Please install the 'gui' extra to use the GUI features with 'pip install niceguitest[gui]' .")
            from niceguitest.cli import main as cli_main
            cli_main()

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
    if __name__ in {"__main__", "__mp_main__"}:
        main()

Adjust pyproject.toml:

    [project]
    name = "niceguitest"
    version = "0.1.0"
    description = "Test for entry points and optional dependencies for nicegui"
    readme = "README.md"
    authors = [
        { name = "Carsten Engelke", email = "carsten.engelke@gmail.com" }
    ]
    requires-python = ">=3.13"
    dependencies = []

    [project.scripts]
    niceguitest = "niceguitest.cli:main"
    niceguitest-gui = "niceguitest.gui:main"

    [project.optional-dependencies]
    gui = [
        "nicegui>=3.10.0",
    ]

    [build-system]
    requires = ["uv_build>=0.10.2,<0.11.0"]
    build-backend = "uv_build"

Things that work:

 - Call: niceguitest -> calls the CLI Version which runs fine.
 - Call: python -m niceguitest.cli -> calls the CLI Version which runs fine.
 - Call python -m niceguitest.gui -> calls the GUI Version which runs fine.

Things that do not work:

 - Call niceguitest-gui -> fails due to
 
    RunTimeError: You must call ui.run() to start the server. If ui.run() is behind a main guard 
    if __name__ == "__main__":
    remove the guard or replace it with
    if __name__ in {"__main__", "__mp_main__"}:
    to allow for multiprocessing.

As the main guard is already altered for multiprocessing this advice seems not helpful. Where is my error? Shouldn't nicegui come up with a more helpful advice? I do think this needs some clarification as this setup seems pretty standard but does not work with nicegui.

PS: Love it anyway, 