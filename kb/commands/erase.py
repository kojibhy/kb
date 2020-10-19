# -*- encoding: utf-8 -*-
# kb v0.1.5
# A knowledge base organizer
# Copyright © 2020, gnc.
# See /LICENSE for licensing information.

"""
kb erase command module

:Copyright: © 2020, gnc.
:License: GPLv3 (see /LICENSE).
"""

from typing import Dict
import kb.filesystem as fs
from kb.actions.erase import erase_kb


def erase(args: Dict[str, str], config: Dict[str, str]):
    """
    Erase the entire kb knowledge base (or only the database).

    Arguments:
    args:           - a dictionary containing the following fields:
                      db -> a boolean, if true, only the database
                      will be deleted
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB           - the main path of KB
                      PATH_KB_DB        - the database path of KB
                      PATH_KB_HIST      - the history menu path of KB
    """

    if args["db"]:
        answer = input(
            "Are you sure you want to erase the kb database ? [YES/NO]")
        if answer.lower() == "yes":
            response = erase_kb("db", config)
            if response == -200:
                print("kb database deleted successfully!")
    else:
        answer = input(
            "Are you sure you want to erase the whole kb knowledge base ? [YES/NO]")
        if answer.lower() == "yes":
            response = erase_kb("all", config)
            if response == -200:
                print("kb knowledge base deleted successfully!")
