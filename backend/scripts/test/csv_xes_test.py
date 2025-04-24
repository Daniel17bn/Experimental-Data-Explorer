import pm4py
import pandas as pd

def csv_to_xes():
    xes_path = r"C:\Users\danie\OneDrive - University of Luxembourg\BSP\backend\data\xes\example.xes"

    try:
        csv_file = r"C:\Users\danie\OneDrive - University of Luxembourg\BSP\test\vrbias-example-user\vrbias-example-user\01\2024-08-29T18-05-00-41\experiment_log.csv"

        #column_names = ["Timestamp","CaseID", "Activity"]
        column_names = ["time:timestamp","case:concept:name","concept:name"]
        df = pd.read_csv(csv_file, names = column_names, header = None)

        df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])

        filtered_df = df.dropna(subset=['time:timestamp', 'case:concept:name', 'concept:name'])

        event_log = pm4py.format_dataframe(filtered_df,
                                        case_id = "case:concept:name",
                                        activity_key = "concept:name",
                                        timestamp_key = "time:timestamp")
        
        pm4py.write_xes(event_log, xes_path )

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    csv_to_xes()
    print("Conversion completed successfully.")
    
#test comment