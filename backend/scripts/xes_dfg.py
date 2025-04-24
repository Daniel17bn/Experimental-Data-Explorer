import pm4py

def xes_dfg(xes_path: str) -> dict:
    """
    Reads an XES file, discovers the Directly Follows Graph (DFG),
    and formats it for frontend use.

    Args:
        xes_path (str): Path to the XES file.

    Returns:
        dict: A dictionary containing the DFG, start activities, and end activities.
    """
    # Read the XES file
    event_log = pm4py.read_xes(xes_path)

    # Discover the DFG
    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)

    # Format the DFG into a JSON-serializable structure
    dfg_dict = {
        "dfg": [{"from": k[0], "to": k[1], "count": v} for k, v in dfg.items()],
        "start_activities": [{"activity": k, "count": v} for k, v in start_activities.items()],
        "end_activities": [{"activity": k, "count": v} for k, v in end_activities.items()]
    }

    return dfg_dict
