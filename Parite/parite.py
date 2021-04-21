#! /usr/bin/env python3
# coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an
import argparse
import MPS

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--extension",help="type of file to analyse. CSV or XML")
    parser.add_argument("-d", "--datafile", help="file to analyse")
    return parser.parse_args()

def main():
    c_an.launch_analysis('current_mps.csv')
    x_an.launch_analysis('syseron.xml')

if __name__ == "__main__":
        args=parse_arguments()
        datafile = args.datafile
        if args.extension == 'xml':
            x_an.launch_analysis(datafile)
        elif args.extension == 'csv':
            #c_an.launch_analysis(datafile)
            MPS.launch_analysis(datafile)


        #main()