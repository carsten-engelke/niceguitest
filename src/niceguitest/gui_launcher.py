# This file is the entry point for the GUI version of the niceguitest package. It defines a simple NiceGUI application that allows users to input two numbers and see their sum. The logic for the addition is defined in the logic.py module, and this file focuses on setting up the GUI and handling user interactions.
# Is serves only as a workaround due to some downsides of using NiceGUI's reload feature, which does not work when starting the app from an entry point in pyproject.toml. By using a root function to set up the GUI, we can ensure that the reload feature works correctly during development, while still providing a seamless experience for users who install the package with the "gui" extra.
# Put your GUI code in gui.py and import it here to keep the entry point clean and focused on launching the app. This also allows you to reuse the GUI components in other contexts if needed.
import sys

from niceguitest import cli

def main(argv=sys.argv[1:]) -> None:
    # This entry point is used when the user runs the command "niceguitest-gui" after installing the package with the "gui" extra.
    try:
        from nicegui import ui
        launch_gui_with_reload(ui, reload=False, argv=argv)
    except ImportError:
        # Fallback to CLI if NiceGUI is not installed, which allows the user to still use the application without the GUI features. It also provides a helpful message about how to install the GUI features.
        print("NiceGUI is not installed. Please install the 'gui' extra to use the GUI features with 'pip install niceguitest[gui]' .")
        from niceguitest.cli import main as cli_main
        cli_main(argv)

def launch_gui_with_reload(ui, argv, reload: bool = False) -> None:
    # Necessary workaround to allow the use of NiceGUI's reload feature which does not work when starting the app from an entry point in pyproject.toml.
    print("Starting NiceGUI app using a root function with reload =", reload)
    ui.run(reload=reload, root=lambda: setup_gui(argv))

def setup_gui(argv) -> None:
    # root function that sets up the GUI layout and components. Workaround for the fact that NiceGUI's reload feature only works with a root function. 
    import niceguitest.gui as gui
    if len(argv) > 0:
        gui.init_gui(cli.parse_arguments(argv)) # Parse CLI arguments to initialize the GUI with the provided values, if any.

if __name__ in {'__main__', '__mp_main__'}:
    #This is called when the user runs the command "python -m niceguitest.gui" to start the GUI application. Here you can use the reload feature of NiceGUI for development purposes, which allows you to see changes in real-time without restarting the app. In production, you would typically set reload to False for better performance.
    try:
        from nicegui import ui
        launch_gui_with_reload(ui, sys.argv[1:], reload=True)
    except ImportError:
        print("NiceGUI is not installed. Please install the 'gui' extra to use the GUI features with 'pip install niceguitest[gui]' .")
        from niceguitest.cli import main as cli_main
        cli_main()