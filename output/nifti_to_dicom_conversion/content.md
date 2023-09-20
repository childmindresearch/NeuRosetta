I'm sorry for the confusion, but some of the software packages mentioned (AFNI, FreeSurfer, FSL, and SPM) do not directly support NIfTI to DICOM conversion. These software typically work the other way around, converting DICOM to NIfTI for easier manipulation in Python or other languages.

The purpose of these platforms is to facilitate the analysis of brain imaging data, which is typically done in NIfTI format. As such, the conversion from DICOM to NIfTI is more common as a pre-processing step.

That being said, here are some examples of how you might convert files using ANTs and pure Python (with the help of external packages), and an alternative solution through dcm2niix tool:

**ANTs**

ANTs does not directly support DICOM to NIFTI but it does provide an interface with the dcm2niix tool which can do so. Here's a minimal example:

```bash
dcm2niix -z y -f %p -o output_folder input_folder/*.dcm
```

**Pure Python (nibabel + pydicom)**

```python
import pydicom
import nibabel as nib
import numpy as np

# Load DICOM and construct NIfTI
ds = pydicom.dcmread('input.dcm')
data = ds.pixel_array
affine = np.eye(4)
img = nib.Nifti1Image(data, affine)

# Save as NIfTI
nib.save(img, 'output.nii')
```

**dcm2niix**

dcm2niix is a designed to convert neuroimaging data from the DICOM format to the NIfTI format. This tool is a part of other larger neuroimaging data processing libraries.

Here's a minimal example of how to use it:

```bash
dcm2niix -z y -f %p -o output_folder input_folder/*.dcm
```
Please ensure to replace the 'input_folder' with the path to your directory holding DICOM files, and 'output_folder' with the path where you want NIFTI files to be saved.
The "-z y" option is for compressing the output NIfTI file, and "-f %p" will name the output NIFTI file same as original DICOM file.

You'll also need to ensure that the dcm2niix tool and the DICOM and NIfTI files are appropriately installed and located for these commands to work.