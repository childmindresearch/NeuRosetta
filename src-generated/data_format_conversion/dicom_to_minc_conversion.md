**AFNI**

```bash
to3d -prefix outDataset.nii -session ./ DICOM/*
3dcopy outDataset.nii output.mnc
```

**ANTs**

There is no native DICOM to MINC conversion in ANTs. Therefore, a common practice is to convert DICOM to NIfTI with dcm2niix, then converting NIfTI to MINC with nii2mnc.

**FSL**

```bash
fslchfiletype ANALYZE input.dcm output.img
dcm2mnc output.img output.mnc
```

**FreeSurfer**

FreeSurfer doesn't allow MINC file creation. A common solution is to convert DICOM to NIfTI using FreeSurfer's mri_convert, then NIfTI to MINC.

**MRtrix**

```bash
mrconvert input.dcm output.nii
nii2mnc output.nii output.mnc
```

**R**

R packages do not directly provide DICOM to MINC conversion. Usually, the conversion involves dealing with DICOM to NIfTI and then NIfTI to MINC.

**Workbench Command**

There isn't native DICOM to MINC conversion for Workbench. A workaround is to use other tools like dcm2niix, and then convert NIfTI to MINC using nii2mnc.

**SPM (via a MATLAB script)**

```matlab
matlabbatch{1}.spm.util.import.dicom.data = {'C:/Users/User/Desktop/DICOM'};
matlabbatch{1}.spm.util.import.dicom.root = 'flat';
matlabbatch{1}.spm.util.import.dicom.outdir = {'C:/Users/User/Desktop/NIfTI'};
matlabbatch{1}.spm.util.import.dicom.prototype = fullfile(spm('dir'), 'toolbox/DICOM/Analyze.nii');
spm_jobman('run', matlabbatch);
cd('C:/Users/User/Desktop/NIfTI');
!nii2mnc YourNIfTIFile.nii YourMINCFile.mnc
```

**Pure Python**

```python
import pydicom
import nibabel as nib
import numpy as np
from pyminc.volumes.factory import *
# Read DICOM file
ds = pydicom.read_file("input.dcm")
# Create Numpy array
array_np = ds.pixel_array
# Create new MINC file
volumeOut = volumeFromFile('output.mnc', dtype=np.int16, volume=volumeIn)
# Write numpy array to MINC file
volumeOut.data[:,:,:] = array_np
``` 

Please note: DICOM to MINC conversion is not commonly performed directly in many of these platforms, thus certain conversions involve intermediate steps such as achieving NIfTI format. Please ensure the necessary tools like dcm2niix, nii2mnc are installed and remember to replace filenames accordingly.