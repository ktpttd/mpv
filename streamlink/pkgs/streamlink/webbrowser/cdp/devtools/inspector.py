# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all modules.
#
# CDP version: v0.0.1156692
# CDP domain: Inspector (experimental)

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from streamlink.webbrowser.cdp.devtools.util import T_JSON_DICT, event_class


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables inspector domain notifications.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Inspector.disable",
    }
    yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables inspector domain notifications.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Inspector.enable",
    }
    yield cmd_dict


@event_class("Inspector.detached")
@dataclass
class Detached:
    """
    Fired when remote debugging connection is about to be terminated. Contains detach reason.
    """
    #: The reason why connection has been terminated.
    reason: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Detached:
        return cls(
            reason=str(json["reason"]),
        )


@event_class("Inspector.targetCrashed")
@dataclass
class TargetCrashed:
    """
    Fired when debugging target has crashed
    """


    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> TargetCrashed:
        return cls(

        )


@event_class("Inspector.targetReloadedAfterCrash")
@dataclass
class TargetReloadedAfterCrash:
    """
    Fired when debugging target has reloaded after crash
    """


    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> TargetReloadedAfterCrash:
        return cls(

        )
