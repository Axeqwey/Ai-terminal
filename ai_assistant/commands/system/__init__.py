from .help import run as help_cmd
from .exit import run as exit_cmd
from .clear import run as clear_cmd

system_commands = {
    "help": help_cmd,
    "exit": exit_cmd,
    "clear": clear_cmd,
}
