import pm4py

def xes_dfg(xes_path: str) -> dict:

    event_log = pm4py.read_xes(xes_path)

    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)

    nodes = []
    edges = []

    unique_activities = set([k[0] for k in dfg.keys()] + [k[1] for k in dfg.keys()])

    for activity in unique_activities:
        nodes.append({"data": {"id": activity, "label": activity}})
    
    for (source,target),count in dfg.items():
        edges.append({"data" : {"source":source, "target": target, "label": f"Count:{count}", "count":count}})


    cytoscape_graph = {
        "nodes": nodes,
        "edges": edges
    }

    return cytoscape_graph