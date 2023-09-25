Sorry, but some of the requested imaging tools do not support direct conversion from NIfTI to DICOM. As such, I can only provide examples for those that support this operation. Here are the examples:

1. **AFNI**

```bash
3dresample -prefix outfile.dcm -input infile.nii -orient RAI
```

2. **ANTs**
ANTs doesn't support direct conversion from NIfTI to DICOM. You might need additional tools like dcm2niix or equivalent.

3. **FSL**
FSL doesn't support conversion from NIfTI to DICOM directly. You need additional tools like dcm2niix or equivalent.

4. **FreeSurfer**

```bash
mri_convert --out_type dicom infile.nii outfile.dcm
```

5. **MRtrix**
MRtrix does not support NIfTI to DICOM conversion.

6. **R**
R does not support NIfTI to DICOM conversion without external packages like oro.nifti or divest.

```R
library('oro.dicom')
niftiFile <- oro.nifti::readNIfTI('infile.nii', reorient = FALSE)
dicomOut<- oro.dicom::writeDICOM(niftiFile,'outfile.dcm')
```

7. **SPM (via a MATLAB script)**

```matlab
hdr = load_nii_hdr('infile.nii');
img = load_nii_img(hdr);
dicomwrite(img, 'outfile.dcm')
```

8. **Python**

Using Pydicom and Nibabel libraries in Python:

```python
import pydicom
import nibabel as nib

# load nifti file
nifti = nib.load('infile.nii')

# cast data to int16 type
data = nifti.get_fdata().astype('int16')

# create dicom
output = pydicom.Dataset()
output.PixelData = data.tostring()

# save as dicom
output.save_as('outfile.dcm')
```

9. **Workbench Command**
Workbench Command does not support NIfTI to DICOM conversion.