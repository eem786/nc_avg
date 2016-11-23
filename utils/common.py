#!/usr/bin/env python
import os
import sys
import re
import netCDF4 as nc

def get_variable_names(file, dims=None):

    dataset = nc.Dataset(file, "r")
    variables = dataset.variables
    if dims:
        variables = [ varname for varname in variables if len(dataset.variables[varname].dimensions) == dims ]
    dataset.close()
    return variables



