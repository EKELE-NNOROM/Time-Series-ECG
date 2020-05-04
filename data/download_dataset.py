# !wget "https://drive.google.com/uc?id=16MIleqoIr1vYxlGk4GKnGmrsCPuWkkpT"

import os
from subprocess import call

print("Downloading...")

extract_directory = os.path.abspath("ECG5000")

if not os.path.exists(extract_directory):
    os.makedirs(extract_directory)
    os.chdir(extract_directory)
    call(
        'gdown --id 16MIleqoIr1vYxlGk4GKnGmrsCPuWkkpT',
        shell=True
    )
    print("Downloading done.\n")
    print("Extracting")
    call(
        'tar -xf "ECG5000.zip"' ,
        shell=True
    )
    print("Extracting successfully done to {}.".format(extract_directory))
    os.chdir("../..")

else:
    print("Dataset already downloaded. Did not download twice.\n")
    print("Can't extract empty zip file.\n")
    os.chdir("..")
