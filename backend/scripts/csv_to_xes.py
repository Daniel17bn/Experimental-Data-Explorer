import pm4py
import pandas as pd

def csv_to_xes(csv_path:str, xes_path:str):

    try:
        csv_file = csv_path

        #column_names = ["Timestamp","CaseID", "Activity"]
        column_names = ["time:timestamp","case:concept:name","concept:name"]
        df = pd.read_csv(csv_file, names = column_names, header = None)

        df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])

        filtered_df = df.dropna(subset=['time:timestamp', 'case:concept:name', 'concept:name'])

        event_log = pm4py.format_dataframe(filtered_df,
                                        case_id = "case:concept:name",
                                        activity_key = "concept:name",
                                        timestamp_key = "time:timestamp")
        
        pm4py.write_xes(event_log, xes_path)

    except Exception as e:
        return f"An error occurred: {e}"


    
    