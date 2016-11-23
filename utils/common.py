#!/usr/bin/env python
import os
import sys
import re
import xarray

def get_variable_names(args):

    dataset = xarray.open_dataset(args.input, decode_times=False)
    all_variables = dataset.variables
    dataset.close()
    if args.variables:
        variables = args.variables.split(",")
        missing_variables = [ varname for varname in variables if varname not in all_variables ]
        if missing_variables:
            sys.stderr.write("ERROR: Missing {} from the input file\n".format(",".join(missing_variables)))
            sys.exit(1)
        return variables
    return all_variables


