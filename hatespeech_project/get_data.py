
import pandas as pd

def get_data():
    X_train = pd.read_csv("/tmp/azureml_runs/hatespeech_data/X_train.tsv", delimiter="\t", header=None, quotechar='"')
    y_train = pd.read_csv("/tmp/azureml_runs/hatespeech_data/y_train.tsv", delimiter="\t", header=None, quotechar='"')

    return { "X" : X_train.values, "y" : y_train[0].values }
