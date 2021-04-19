import pandas as pd
import os

class SetOfParliamentMembers:
    def __init__(self,name):
        self.name=name

    def data_from_csv (self, csv_file):
        sel.dataframe=pd.read_csv(csv_file,sep=";")

    def data_from_dataframe (self, dataframe):
        self.dataframe = dataframe

    def display_chart:
        #TODO DISPLAY CHART
        pass

    import os
    import pandas as pd

    class SetOfParliamentMembers:
        def __init__(self, name):
            self.name = name

        def data_from_csv(self, csv_file):
            self.dataframe = pd.read_csv ( csv_file, sep=";" )

        def data_from_dataframe(self, dataframe):
            self.dataframe = dataframe

        def display_chart(self):
            # à venir, patience !
            pass

        def split_by_political_party(self):
            result = {}
            data = self.dataframe

            all_parties = data["parti_ratt_financier"].dropna ().unique ()

            for party in all_parties:
                data_subset = data[data.parti_ratt_financier == party]
                subset = SetOfParliamentMembers ( 'MPs from party "{}"'.format ( party ) )
                subset.data_from_dataframe ( data_subset )
                result[party] = subset

            return result

    def launch_analysis(data_file, by_party=False):
        sopm = SetOfParliamentMembers ( "All MPs" )
        sopm.data_from_csv ( os.path.join ( "data", data_file ) )
        sopm.display_chart ()

        if by_party:
            for party, s in sopm.split_by_political_party ().items ():
                s.display_chart ()