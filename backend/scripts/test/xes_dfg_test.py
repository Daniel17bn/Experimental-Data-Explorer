import pm4py
import json  # Import the JSON module

def xes_dfg():
    """
    Reads an XES file, discovers the Directly Follows Graph (DFG),
    and saves it as a JSON file.

    Args:
        xes_path (str): Path to the XES file.
        output_json_path (str): Path to save the output JSON file.

    Returns:
        None
    """
    # Read the XES file
    xes_path = r"C:\Users\danie\OneDrive - University of Luxembourg\BSP\backend\data\xes\example.xes"
    output_json_path = r"C:\Users\danie\OneDrive - University of Luxembourg\BSP\backend\data\dfg_json\example.json"
    event_log = pm4py.read_xes(xes_path)

    # Discover the DFG
    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)

    # Format the DFG into a JSON-serializable structure
    dfg_dict = {
        "dfg": [{"from": k[0], "to": k[1], "count": v} for k, v in dfg.items()],
        "start_activities": [{"activity": k, "count": v} for k, v in start_activities.items()],
        "end_activities": [{"activity": k, "count": v} for k, v in end_activities.items()]
    }

    # Write the dictionary to a JSON file
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(dfg_dict, json_file, indent=4)
    print(f"JSON file successfully written to {output_json_path}")


if __name__ == "__main__":
    xes_dfg()
    print("DFG extraction and JSON conversion completed successfully.")