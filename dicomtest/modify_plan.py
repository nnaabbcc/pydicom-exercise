import pydicom
import os

filePath = "C:/zhaoyl/Backup/01.DICOM/04.DICOM_Files/07.Multi-ISO-Center/2 iso plan/RP1.2.752.243.1.1.20190128151700217.4000.28177.dcm"

ds = pydicom.dcmread(filePath)

for i, beam in enumerate(ds.IonBeamSequence):
    ## Change the Machine Name
    beam.TreatmentMachineName = "GTR2-PBS"
    ## Change the Snout ID
    for j, snout in enumerate(beam.SnoutSequence):
        snout.SnoutID = "snout40"

# Get Save As File Name
folder = os.path.dirname(filePath)
fileName = os.path.basename(filePath)
fileName, ext = os.path.splitext(fileName)
fileName = fileName + "_modified" + ext
saveFileName = os.path.join(folder, fileName)

## Save to DICOM file
ds.save_as(saveFileName)
