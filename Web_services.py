#XML schema define and compare with xml with validator to return true or false with schema is matched
# <xs:complexType name="person">
#     <xs:sequence>
#         <xs:element name="Value1" type="xs:string"/>
#         <xs:element name="Value2" type="xs:date"/>
#         <xs:element name="Value3" type="xs:integer"/>
#     </xs:sequence>
# </xs:complexType>
print("#"*10,"XML","#"*10)
import xml.etree.ElementTree as ET
data='''<person>
    <name>Benup</name>
    <phone>+9779861245228</phone>
    <email hide="yes"/>
    <name>Raju</name>
    <phone>+9779861245228</phone>
    <email hide="yes"/>
</person>'''
tree=ET.fromstring(data)
names=tree.findall('name')
for item in names:
    print('Name=',item.text)
print("#"*10,"JSON","#"*10)
import json
data='''{
    "name":"Benup Ghimire",
    "phone":{
        "country":"+977",
        "number":"9861245228"
    }
}'''
info=json.loads(data)
print("Name=",info["name"])
print("Phone=","Country-code:",info["phone"]["country"],"Number:",info["phone"]["number"])
print("#"*10,"JSON List","#"*10)
data2='''[
    {
        "name":"Benup Ghimire",
        "phone":{
            "country":"+977",
            "number":"9861245228"
            }
    },
    {
        "name":"Rajendra Acharya",
            "phone":{
                "country":"+977",
                "number":"9800000000"
            }
    }
]'''
data_values=json.loads(data2)
print("No. of user=",len(data_values))
for data_value in data_values:
    print("Name=",data_value["name"])
    print("Phone=","Country-code:",data_value["phone"]["country"],"Number:",data_value["phone"]["number"])