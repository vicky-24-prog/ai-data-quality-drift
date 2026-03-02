import pandas as pd
def load_reference_data(path):
    """
    Load historical refrence data
    """
    df=pd.read_csv(path)
    return df

if __name__=="__main__":
    data_path="./data/application_train.csv"
    df=load_reference_data(data_path)
    print("data loaded successfully")
    print("Shape:",df.shape)