import os
import matplotlib.pyplot as mps
import numpy as np
import pandas as pd


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len ( self.dataframe )

    def __getitem__(self, item):
        return self.dataframe[item]

    def __repr__(self):
        return "SetOfParliament Memeer : {}".format ( len ( self.dataframe ) )

    def __iter__(self):
        self.iterator_state=0
        return self

    def __next__(self):
        if self.iterator_state >= len(self):
            raise StopIteration
        else:
            result = self[self.iterator_state]
            self.iterator_state+=1
            return result
    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=';')

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        SPM_femmes = data[data.sexe == 'F']
        SPM_hommes = data[data.sexe == 'H']
        counts = [len(SPM_femmes), len(SPM_hommes)]
        np_counts = np.array(counts)
        spm_nb = np_counts.sum()
        proportions = np_counts / spm_nb
        labels = ["female: ({})".format(counts[0]), "male: ({})".format(counts[1])]
        fig, ax = mps.subplots()
        ax.axis('equal')
        ax.pie(
            proportions,
            labels=labels,
            autopct="%1.1f pourcents"
        )
        mps.title("{} ({} MPS)".format(self.name, spm_nb))
        mps.show()



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


def launch_analysis(data_file, by_party=False, info=False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("../data", data_file))
    for mp in sopm:
        print(mp["nom"],mp["emails"])
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

    if info:
        print(sopm)


if __name__ == "__main__":
    launch_analysis('current_mps.csv',)
