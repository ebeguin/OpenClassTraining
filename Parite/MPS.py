import os

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as mps
import numpy as np


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        # à venir, patience !
        # Deputes femmes
        data = self.dataframe
        SPM_femmes = data[data.sexe == "F"]
        SPM_hommes = data[data.sexe == "M"]
        counts = [len(SPM_femmes), len(SPM_hommes)]
        np_counts = np.array(counts)
        spm_nb = np_counts.sum()
        proportions = np_counts / spm_nb
        labels = ["female: ({})".format(counts[0]), "male: ({})".format(counts[1])]
        fig, ax = mps.subplots()
        ax.axis("equals")
        ax.pie(
            proportions,
            labels=labels,
            autopct="%1.1f pourcents"
        )
        plt.title("{} ({} MPS)".format(self.name, spm_nb))


    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party=False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("data", data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()
