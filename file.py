
import os
import pydicom

fileName = "test.dcm"
ds = pydicom.dcmread(fileName)

print(ds)

