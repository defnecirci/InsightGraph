openai_api_key = "openai_api_key"
neo4j_uri = "neo4j_uri"
neo4j_username = "neo4j_username"
neo4j_password = "neo4j_password"


prompt = "***Task***" 
prompt += "For the text below extract materials, compositions, properties, applications, methods and create a JSON object in this format."
prompt += "Relationships or Edges can be contains, has_material and has_property, has_application, has_value."
prompt += "Node labels can be contains, material, property, applications, compositions."
prompt += "Nodes should be with ids, names, labels, attributes and  relationships should be source, target, type. Ids need to be numerical values. Json keys need to be nodes and edges."
prompt += "***Format***" 
prompt += "'nodes': [{'id': '','name': '','label':'material','attributes': {}],'edges': [{'source': '','target': '','type': ''}],}"
prompt += "***Text***" 

system_role = "You extract information from documents and return json objects"

model = "gpt-3.5-turbo"