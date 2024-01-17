[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/data_format_conversion/nifti_to_dicom_conversion.md)
# NIfTI to DICOM Conversion

some of the requested imaging tools do not support direct conversion from NIfTI to DICOM. As such, I can only provide examples for those that support this operation. Here are the examples:

## <img src="../icons/afni.png" height="24px" /> AFNI

```bash
3dresample -prefix outfile.dcm -input infile.nii -orient RAI
```

## <img src="../icons/ants.png" height="24px" /> ANTs
ANTs doesn't support direct conversion from NIfTI to DICOM. You might need additional tools like dcm2niix or equivalent.

## <img src="../icons/fsl.png" height="24px" /> FSL
FSL doesn't support conversion from NIfTI to DICOM directly. You need additional tools like dcm2niix or equivalent.

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
mri_convert --out_type dicom infile.nii outfile.dcm
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
MRtrix does not support NIfTI to DICOM conversion.

## <img src="../icons/r.png" height="24px" /> R
R does not support NIfTI to DICOM conversion without external packages like oro.nifti or divest.

```R
library('oro.dicom')
niftiFile <- oro.nifti::readNIfTI('infile.nii', reorient = FALSE)
dicomOut<- oro.dicom::writeDICOM(niftiFile,'outfile.dcm')
```

## <img src="../icons/spm.png" height="24px" /> SPM

```matlab
hdr = load_nii_hdr('infile.nii');
img = load_nii_img(hdr);
dicomwrite(img, 'outfile.dcm')
```

## <img src="../icons/python.png" height="24px" /> Python

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

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
Workbench Command does not support NIfTI to DICOM conversion.