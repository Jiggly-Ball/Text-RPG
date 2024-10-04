import pickle
from typing import Union
from terminal import Colour, Terminal


def load_terminal() -> dict:
    try:
        with open("data/formats.bin", "rb") as f:
            return pickle.load(f)

    except FileNotFoundError:
        with open("data/formats.bin", "wb") as f:
            pickle.dump(
                {
                    "def_option_colour": Colour.BLUE,
                    "def_option_bg": Colour.BLACK,
                    "def_text_colour": Colour.BLUE,
                    "def_text_bg": Colour.BLACK,
                    "text_delay": 0.03,
                },
                f,
            )
        return load_terminal()


def save_terminal(terminal: Terminal) -> None:
    with open("data/formats.bin", "wb") as f:
        pickle.dump(
            {
                "def_option_colour": terminal.option_colour,
                "def_option_bg": terminal.option_bg,
                "def_text_colour": terminal.text_colour,
                "def_text_bg": terminal.text_bg,
                "text_delay": terminal.text_delay,
            },
            f,
        )


def load_player_data(slot: int) -> Union[dict]:
    try:
        with open(f"data/player{slot}.bin", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return


def save_player_data(slot: int) -> None: ...
