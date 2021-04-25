#! /usr/bin/env python3
# coding: utf-8
import analysis.parite_csv as c_an
import analysis.parite_xml as x_an
import argparse
import logging as lg
import re as regularexp



# import MPS

def parse_arguments():
    parser = argparse.ArgumentParser ()
    parser.add_argument ( "-e", "--extension", help="type of file to analyse. CSV or XML" )
    parser.add_argument("-p","--byparty",help="displays a graph of each..")
    parser.add_argument ( "-d", "--datafile", help="file to analyse" )
    parser.add_argument ( "-i", "--info", help="""information about the file""" )
    return parser.parse_args()


if __name__ == "__main__":
    lg.basicConfig(level=lg.INFO)
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You should indicate a file!')
        my_exp = regularexp.search ( r'^.+\.(\D{3})$', datafile )
        if my_exp is None:
            raise Warning ( "You should indicate a file with a .xxx extension" )
    except Warning as e:
        lg.warning ( e )
    else:
        extension=my_exp.group(1)
        if extension == 'xml':
            x_an.launch_analysis ( 'syseron.xml' )
        elif extension == 'csv':
            c_an.launch_analysis ( datafile, args.byparty, args.info )
    finally:
        lg.info ( '##### Analysis is over ####' )


