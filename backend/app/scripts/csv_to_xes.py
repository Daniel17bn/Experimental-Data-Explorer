import pm4py
import pandas as pd
import os
import json

def csv_to_xes(csv_path: str, xes_path: str):
    """
    Converts a CSV file to an XES file, including only rows with 'event' and a number,
    and embedding additional information as attributes.

    Args:
        csv_path (str): Path to the input CSV file.
        xes_path (str): Path to save the output XES file.

    Returns:
        str: Success message or error message.
    """
    try:
        # Validate if the CSV file exists
        if not os.path.exists(csv_path):
            return f"Error: The file '{csv_path}' does not exist."

        # Read the CSV file
        column_names = ["timestamp", "event", "details"]
        df = pd.read_csv(csv_path, names=column_names, header=None)

        # Filter rows where 'event' contains a number
        filtered_df = df[df['event'].str.contains(r'\d+', na=False)]

        # Parse additional details into JSON (if applicable)
        def parse_details(details):
            try:
                return json.loads(details)
            except (ValueError, TypeError):
                return {}

        filtered_df['details'] = filtered_df['details'].apply(parse_details)

        # Format the DataFrame for PM4Py
        event_log = []
        for _, row in filtered_df.iterrows():
            event = {
                "time:timestamp": pd.to_datetime(row["timestamp"]),
                "concept:name": row["event"],
                "details": row["details"],  # Additional attributes
            }
            event_log.append(event)

        # Convert to PM4Py event log format
        event_log = pm4py.convert_to_event_log(pd.DataFrame(event_log))

        # Write the event log to an XES file
        pm4py.write_xes(event_log, xes_path)

        return f"Successfully converted '{csv_path}' to '{xes_path}'."

    except Exception as e:
        return f"An error occurred: {e}"



