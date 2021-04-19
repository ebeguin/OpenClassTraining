import os
import logging as lg

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
    path_to_file = os.path.join(directory, "data", data_file) # with this path, we go inside the folder `data` and get the file.
    lg.basicConfig(level=lg.DEBUG)
    try:
        with open(path_to_file,"r") as f:
            preview = f.readline()
            lg.debug( 'Yeah! We managed to read the file. Here is a preview: {}'.format ( preview ) )
    except FileNotFoundError as e :
        lg.critical("erreur d'ouvertures : {}".format(e.filename))


if __name__ == "__main__":
    launch_analysis('current_mps.csv')
