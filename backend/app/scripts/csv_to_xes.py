import pm4py
import pandas as pd

from typing import Dict

EVENT_TRANSLATION: Dict[str, int] = {
        "rest_start": 34, "rest_end": 66,
        "freeviewing_start": 36, "freeviewing_end": 68,
        "cube-sync_start": 38, "cube-sync_end": 70, "cube-sync_flash": 39,
        "toilet-sync_start": 40, "toilet-sync_end": 72, "toilet-sync_flash": 41,
        "avatar-sync_start": 42, "avatar-sync_end": 74, "avatar-sync_flash": 43,
        "scan-sync_start": 44, "scan-sync_end": 76, "scan-sync_flash": 45,
        "cube-async_start": 46, "cube-async_end": 78, "cube-async_flash": 47,
        "toilet-async_start": 48, "toilet-async_end": 80, "toilet-async_flash": 49,
        "avatar-async_start": 50, "avatar-async_end": 82, "avatar-async_flash": 51,
        "scan-async_start": 52, "scan-async_end": 84, "scan-async_flash": 53,
        "baseline_start": 62, "baseline_end": 94,
        "bse_trial_1": 54, "bse_trial_2": 56, "bse_trial_3": 58, "bse_trial_4": 60,
        "bse_trial_end": 86
}


R_EVENT_TRANSLATION: Dict[int, str] = {v: k for k, v in EVENT_TRANSLATION.items()}


def csv_to_xes(csv_path:str, xes_path:str):

    try:
        csv_file = csv_path

        column_names = ["time:timestamp","data_type","concept:name"]
        df = pd.read_csv(csv_file, names = column_names, header = None)

       
        df = df[df["data_type"] == "event"]

        
        df["concept:name"] = [R_EVENT_TRANSLATION[int(x)] if int(x) in R_EVENT_TRANSLATION else pd.NA for x in df["concept:name"]]

        
        df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])

        
        df['case:concept:name'] = 1

        filtered_df = df.dropna(subset=['time:timestamp', 'case:concept:name', 'concept:name'])

        event_log = pm4py.format_dataframe(filtered_df,
                                        case_id = "case:concept:name",
                                        activity_key = "concept:name",
                                        timestamp_key = "time:timestamp")

        pm4py.write_xes(event_log, xes_path)

    except Exception as e:
        return f"An error occurred: {e}"

