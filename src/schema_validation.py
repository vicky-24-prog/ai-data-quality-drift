import pandas as pd


import yaml
def load_schema(schema_path):
    with open(schema_path,"r") as file:
        schema=yaml.safe_load(file)
    return schema
def validate_schema(df,schema):
    errors=[]

    for column, rules in schema.items():
        if rules["required"] and column not in df.columns:
            errors.append(f"Missing required column: {column}")
        elif column in df.columns:
            if str(df[column].dtype) != rules["type"]:
                errors.append(
                    f"Wrong type for column {column}: expected {rules['type']}, got {str(df[column].dtype)}"
                )
    return errors

if __name__ == "__main__":
    df=pd.read_csv("../data/application_train.csv")
    schema=load_schema("../config/schema.yaml")

    validation_errors=validate_schema(df,schema)
    
    if validation_errors:
        print("schema validation Failed")
        for error in validation_errors:
            print(error)
    else:
        print("Schema validation Passed")


