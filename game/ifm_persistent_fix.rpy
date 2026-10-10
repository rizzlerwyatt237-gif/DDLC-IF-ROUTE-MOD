# Compatibility repair for classic Ren'Py / DDLC persistent data.
# Some older runs can contain a persistent variable with the value None.
# This file runs before if_route_mod.rpy's initialization and normalizes them.

init -3 python:
    if not hasattr(persistent, "ifm_unlocked") or persistent.ifm_unlocked is None:
        persistent.ifm_unlocked = []
    if not hasattr(persistent, "ifm_endings_seen") or persistent.ifm_endings_seen is None:
        persistent.ifm_endings_seen = []
    if not hasattr(persistent, "ifm_runs_started") or persistent.ifm_runs_started is None:
        persistent.ifm_runs_started = 0
    if not hasattr(persistent, "ifm_last_route") or persistent.ifm_last_route is None:
        persistent.ifm_last_route = ""
    if not hasattr(persistent, "ifm_last_ending") or persistent.ifm_last_ending is None:
        persistent.ifm_last_ending = ""
    if not hasattr(persistent, "ifm_pressure_last_run") or persistent.ifm_pressure_last_run is None:
        persistent.ifm_pressure_last_run = 0
