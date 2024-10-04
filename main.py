from terminal import *
from utils import load_terminal, save_terminal, load_player_data


def load_game(terminal: Terminal) -> None:
    states = []


def settings(terminal: Terminal) -> None:
    setting_values = {
        "Option Colour": "option_colour",
        "Option BG Colour": "option_bg",
        "Text Colour": "text_colour",
        "Text BG Colour": "text_bg",
    }
    while True:
        option = terminal.option_terminal(
            "Which setting would you like to configure?",
            (
                "Option Colour",
                "Option BG Colour",
                "Text Colour",
                "Text BG Colour",
                "Text Speed",
                "Menu",
            ),
            (ReturnType.LITERAL,),
        )
        if option == "Text Speed":
            inp = terminal.option_terminal(
                "Choose the text speed",
                ("No Delay", "Fast", "Medium", "Slow"),
                (ReturnType.LITERAL,),
            )
            terminal.text_delay = {
                "No Delay": 0,
                "Fast": 0.02,
                "Medium": 0.03,
                "Slow": 0.07,
            }[inp]

        elif option == "Menu":
            return

        else:
            inp = terminal.option_terminal(
                f"Choose the {option.lower()} you want-",
                [colour.title() for colour in Colour.__members__],
                (ReturnType.LITERAL,),
            )
            terminal.__dict__[setting_values[option]] = Colour.__members__[inp.upper()]

        save_terminal(terminal=terminal)


def main() -> None:
    data = load_terminal()
    data["def_text_end"] = "Press Enter To Continue"
    terminal = Terminal(**data)

    while True:
        inp = terminal.option_terminal(
            "Welcome to Text RPG!\nChoose an option to get started-",
            ("Load Game", "Settings", "Exit"),
            (ReturnType.LITERAL,),
        )
        if inp == "Load Game":
            load_game(terminal=terminal)

        elif inp == "Settings":
            settings(terminal=terminal)

        elif inp == "Exit":
            exit()


if __name__ == "__main__":
    main()
