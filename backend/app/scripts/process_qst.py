import pandas as pd
import json


def process_qst(q_csv_path:str,q_json_path):

    df = pd.read_csv(q_csv_path)

    grouped_data = {}

    for (questionnaire,condition), group in df.groupby(["Questionnaire","Condition"]):
        if questionnaire not in grouped_data:
            grouped_data[questionnaire] = {}
        if condition not in grouped_data[questionnaire]:
            grouped_data[questionnaire][condition]=[]
        
        for index,row in group.iterrows():
            grouped_data[questionnaire][condition].append({
                "Question Number": row["Question Number"],
                "Question": row["Question"],
                "Answer": row["Answer"]
                })
    

    with open(q_json_path,"w") as f:
        json.dump(grouped_data,f,indent=2)


    

   

