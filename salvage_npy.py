# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:45:17 2021

@author: Clayton
"""
import struct
import numpy as np

def salvage_npy(filename):
    with open(filename, "rb") as file:
        magic_string = b'\x93NUMPY' # should = first 6 bytes of file
        if file.read(6) != magic_string:
            raise 'Not a .npy file!'
        major_version = file.read(1) # unused
        minor_version = file.read(1) # unused
        header_len = struct.unpack('H'*1, file.read(2))[0] # returns short little edian corresponding to rest of header len
        array_format = eval(file.read(header_len)) # get dictionary of array format info
    offset = 10+header_len # offset to where the data starts
    return np.fromfile(filename,dtype=array_format['descr'],offset=offset) # read data, do no reformatting