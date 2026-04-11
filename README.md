This NiceGUI Template is meant for small tools and offers:

1. CLI interface and optional GUI (with independent installable packages, already created by uv add nicegui --optional gui)

Install small CLI version with:

    pipx install niceguitest
    
    or 

    pip install niceguitest

Install full GUI version with:

    pipx install niceguitest[gui]
    
    or 
    
    pip install niceguitest[gui]

2. Handling of command line arguments

3. Workaround for two NiceGUI malfunctions, offering usage of pyproject.toml Entry Points (standard with uv)

## Where to start:

1. Put your (nicegui) GUI code in gui.py
2. Adjust the command line code handling in cli.py -> parse_arguments
3. Ready to go. 

Run the app with:

    uv run niceguitest
    
    or 

    uv run niceguitest-gui

or just run gui_launcher.py or cli.py