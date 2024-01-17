[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/data_format_conversion/dicom_to_nifti_conversion.md)
# DICOM to NIfTI Conversion

here are some examples of how you'd convert DICOM images to NIfTI using different libraries and languages. Please make sure to replace the placeholders with your actual file paths, as needed.

## <img src="../icons/afni.png" height="24px" /> AFNI

AFNI provides a program called `to3d` which can be used to convert DICOM files.

```bash
to3d -prefix output.nii -format NIFTI 'dicom_*.dcm'
```

## <img src="../icons/ants.png" height="24px" /> ANTs

ANTs provides a function called `ConvertToNifti`.

```bash
ConvertToNifti input.dcm output.nii
```

## <img src="../icons/fsl.png" height="24px" /> FSL

FSL uses `fslchfiletype` for the format conversion.

```bash
fslchfiletype NIFTI input.dcm output
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

FreeSurfer does not directly support DICOM to NIfTI conversion. However, it can be achieved via the `mri_convert` function.

```bash
mri_convert input.dcm output.nii
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

MRtrix uses `mrconvert` to transform formats.

```bash
mrconvert input.dcm output.nii
```

## <img src="../icons/r.png" height="24px" /> R

In R, you would use the `oro.dicom` and `oro.nifti` libraries. First, you read the DICOM file and then you write it out as NIfTI.

```R
library(oro.dicom)
library(oro.nifti)
dicom_data <- readDICOMFile('input.dcm')
nifti_data <- as.nifti(dicom_data)
writeNIfTI(nifti_data, filename='output.nii')
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

The 'wb_command -cifti-convert' serves the purpose in Workbench.

```bash
wb_command -cifti-convert -to-nifti input.dcm output.nii
```

## <img src="../icons/python.png" height="24px" /> Python

In Python, you can use `pydicom` and `nibabel` libraries to convert DICOM to NIfTI.

```python
import pydicom
import nibabel as nib

data_set = pydicom.dcmread('input.dcm')
data = data_set.pixel_array

new_image = nib.Nifti1Image(data, affine=np.eye(4))
nib.save(new_image, 'output.nii')
```

## <img src="../icons/spm.png" height="24px" /> SPM

In SPM, we use `spm_dicom_convert` function.

```matlab
headers = spm_dicom_headers('input.dcm');
spm_dicom_convert(headers,'all','flat','nii');
```

Please note that these are very basic examples. You may need to adjust these scripts based on your specific needs or features from your DICOM files.