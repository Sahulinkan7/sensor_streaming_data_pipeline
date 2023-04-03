import pandas as pd
import json

class Generic:
    def __init__(self,record:dict):
        
        for key,val in record.items():
            setattr(self,key,val)
            
    @staticmethod
    def dict_to_object(data: dict,ctx):
        print(data,ctx)
        return Generic(record=data)
        
    
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def get_object(cls,file_path):
        chunk_df=pd.read_csv(file_path,chunksize=10)
        for df in chunk_df:
            for data in df.values:
                generic=Generic(dict(zip(df.columns,list(map(str,data)))))
                yield generic
    
    @classmethod
    def get_schema_to_produce_consume_data(cls,file_path):
        columns=next(pd.read_csv(file_path,chunksize=10)).columns
        
        schema=dict()
        schema.update({
            "$id": "http://example.com/myURI.schema.json",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "additionalProperties": False,
            "description": "Sample schema to help you get started.",
            "properties": dict(),
            "title": "SampleRecord",
            "type": "object"
        })
        
        for column in columns:
            schema["properties"].update(
                {
                    f"{column}":{
                        "description":f"generic {column}",
                        "type":"string"
                    }
                }
            )
        
        schema=json.dumps(schema)
        print(schema)
        return schema
    
    def __str__(self):
        return f"{self.__dict__}"
    
def instance_to_dict(instance:Generic,ctx):
    return instance.to_dict()