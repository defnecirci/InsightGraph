import json
import os
import openai

with open('nm_abstract.json', 'r') as file:
    input_data = json.load(file)


openai.api_key = "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"
key = list(input_data.keys())[1]
print(key)

text = input_data[key]
prompt = " For the text below extract materials (Material), compositions (Composition), properties (Property), applications (Application), methods (Method) and create a JSON objectin a format                  {nodes:[{id:1,name:SiO2 nanoparticles,label:Material,attributes:{diameter:15 nm,copolymer:grafted block copolymer}},{id:2,name:polyhexylmethacrylate(PHMA),label:Material,attributes:{block:rubbery,molecular weight:20-80 kg/mol}},{id:3,name:polyglycidylmethacrylate(PGMA),label:Material,attributes:{block:matrix compatible,outer block thickness:30 nm}},{id:4,name:epoxy,label:Material,attributes:{}},{id:5,name:ductility,label:Property,attributes:{improvement:maximum 60%}},{id:6,name:fracture toughness,label:Property,attributes:{improvement:maximum 300%}},{id:7,name:fatigue crack growth resistance,label:Property,attributes:{}},{id:8,name:modulus,label:Property,attributes:{loadings:less than 2 vol% of silica core}},{id:9,name:plastic void growth,label:Property,attributes:{}},{id:10,name:shear banding,label:Property,attributes:{}},{id:11,name:fracture energy,label:Property,attributes:{}},{id:12,name:nanocomposites,label:Application,attributes:{}},{id:13,name:grafting,label:Method,attributes:{}},{id:14,name:systematic study,label:Method,attributes:{}}],edges:[{source:2,target:1,type:composition},{source:3,target:4,type:composition},{source:1,target:5,type:properties},{source:1,target:6,type:properties},{source:4,target:5,type:properties},{source:4,target:6,type:properties},{source:4,target:7,type:properties},{source:1,target:8,type:properties},{source:4,target:8,type:properties},{source:1,target:9,type:properties},{source:1,target:10,type:properties},{source:1,target:11,type:properties},{source:12,target:1,type:uses},{source:13,target:1,type:method},{source:14,target:1,type:method}]}"

prompt = prompt + text
response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You extract information from documents and return json objects"},
        {"role": "user", "content": prompt},
        ]
        )
out_final= response["choices"][0]["message"]["content"]


print (out_final)

try:
    json_string = out_final
    json_object = json.loads(json_string)
except:
    json_string = out_final.split('```')[1].split('```')[0]
    json_object = json.loads(json_string)

json_object = json.loads(json_string)
with open('run6_output_' + key + '.json', 'w') as file:
    json.dump(json_object, file)

