import os
import openai
import json
import datetime
import streamlit as st
import config as cfg
import networkx as nx
import matplotlib.pyplot as plt
from neo4j import GraphDatabase
from collections import Counter

openai.api_key = cfg.openai_api_key
uri = cfg.neo4j_uri
username = cfg.neo4j_username
password = cfg.neo4j_password

def extract_graph(text,filename):
    prompt = f"{cfg.prompt} {text}"
    system_role = cfg.system_role
    model = cfg.model
    response = openai.ChatCompletion.create(
      model=model,
      messages=[
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt},
        ]
        )
    out = response["choices"][0]["message"]["content"]  
    json_object = json.loads(out)
    with open('./data/output/' + filename + '.json', 'w') as file:
        json.dump(json_object, file)
        pretty_json = json.dumps(json_object, indent=4)
        print(pretty_json)
    graph = json_object
    return graph 

def save_graph(graph,filename):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    now =  datetime.datetime.now()
    start = int(now.timestamp())

    def create_graph(tx, data):      
        for node in data["nodes"]:
            tx.run("CREATE (:{} {{id: '{}', name: '{}'}})".format(node["label"], str(node["id"]+start), node["name"])) 
        for rel in data["edges"]:
            print (rel)
            rel["startLabels"] = data["nodes"][rel["source"]-1]["label"]
            rel["endLabels"] = data["nodes"][rel["target"]-1]["label"]
            tx.run("MATCH (a:{} {{id: {}}}), (b:{} {{id: {}}}) CREATE (a)-[:{} {{type: '{}'}}]->(b)".format(rel["startLabels"], rel["source"]+start, rel["endLabels"], rel["target"]+start, rel["type"], rel["type"]))
        tx.run("CREATE (:{} {{id: {}, name: '{}'}})".format("Article", start+500, filename))  
        tx.run("MATCH (a:Article {{id: {}}}) MATCH (n:material) CREATE (a)-[:MENTIONS]->(n) RETURN a, n".format(start+500))

    with driver.session() as session:
        session.execute_write(create_graph, graph)
    driver.close()

def show_graph(text):
    with open('./data/output/L141.json', 'r') as file:
        output_data = json.load(file)

        nodes = output_data['nodes']
        edges = output_data['edges']
        node_labels = [n["label"] for n in nodes]
        node_label_counts = Counter(node_labels)
        edge_types = [e["type"] for e in edges]
        edge_type_counts = Counter(edge_types)
       
        #Display nodes and edges information
        st.write("**Nodes**")       
        node_count_str = ' '.join([f"{item}: {count}" for item, count in node_label_counts.items()])
        st.write(node_count_str)
        st.write("**Edges**")
        edge_count_str = ' '.join([f"{item}: {count}" for item, count in edge_type_counts.items()])
        st.write(edge_count_str)
        
        #Display graph
        G = nx.Graph()
        for node in nodes:
            G.add_node(node['id'],label=node['name'])
        for edge in edges:
            G.add_edge(edge['source'], edge['target'], **edge)            
        fig, ax = plt.subplots(figsize=(8, 8))
        pos = nx.spring_layout(G, k=1.8)
        labels = nx.get_node_attributes(G, 'label')        
        nx.draw(G, pos, with_labels=True, labels=labels, font_size=8, node_size=500, node_color='red', edge_color='blue', width=5)
        edge_labels = {(edge['source'], edge['target']): edge['type'] for edge in edges}        
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,verticalalignment='top',font_size=8,alpha=0.5)
        st.pyplot(fig)
       
       
    
def main():
    st.title("GraphInsight!")
    st.header("A visual journey through Materials Articles.")
    st.write("View details [link](https://browser.graphapp.io)")
    input = ""
    filename = ""
    with st.sidebar:
        st.sidebar.title("Upload the abstract")
        file_path = st.sidebar.file_uploader(label="", type='txt')
        if file_path is not None:
            with file_path:
                text = file_path.read().decode('utf-8')
                filename = os.path.basename(file_path.name)
                st.write(text)
                input = text
                

    if input and filename:             
        graph = extract_graph(text,filename)
        save_graph(graph,filename)
        show_graph(text)

    
if __name__ == '__main__':
    main()
