import os
import pandas as pd


def read_network(network_path: str):
    data = pd.read_csv(network_path, delim_whitespace=True)
    data = data[["UniProtName_A","UniProtName_B"]]
    return data


def combine_networks(networks_path: str):
    files = os.listdir(networks_path)
    combined_network = pd.DataFrame(columns=["UniProtName_A", "UniProtName_B"])
    for file in files:
        data = read_network(networks_path + file)
        combined_network = pd.concat([combined_network, data])
        combined_network = combined_network.drop_duplicates()
    combined_network.to_csv("combined_network_header.txt", index=False, sep="\t")
    combined_network.to_csv("combined_network.txt", index=False, header=False, sep="\t")


current_path = os.getcwd()
networks_path = current_path + "\\Networks\\"

combine_networks(networks_path)
