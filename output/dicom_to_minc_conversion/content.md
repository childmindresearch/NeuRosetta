Here are some basic examples of how you can convert DICOM to MINC in these various programs:

1. AFNI:

AFNI doesn't directly support conversion to MINC, but it can convert DICOM to NIFTI, which can then be converted to MINC using other software.

```
to3d -prefix my_data -session ./SesameStreet -time:tz 64 64 33 3 EchoTime 0 999 dicom_images/*.dcm
3dAFNItoNIFTI -prefix my_data.nii my_data+orig
```
(This assumes AFNI's 'to3d' for DICOM to AFNI, then '3dAFNItoNIFTI' for AFNI to NIFTI)

2. ANTs:

ANTs supports conversion from DICOM to NIFTI, but not directly to MINC.

```
ConvertBetweenFileFormats dicom_images/*.dcm my_data.nii
```
(this assumes 'ConvertBetweenFileFormats' utility for DICOM to NIFTI)
 
3. FSL:

FSL doesn't support DICOM to MINC directly, though it provides the 'dcm2nii' command, which can convert DICOM to NIFTI.

```
dcm2nii -n y dicom_images/*.dcm
```

4. FreeSurfer:

FreeSurfer doesn't support DICOM to MINC conversion, though it provides the 'mri_convert' command, which can convert DICOM to various formats including NIFTI.

```
mri_convert dicom_images/*.dcm my_data.nii
```

5. MRtrix:

MRtrix supports conversion from DICOM to its native MRtrix format (.mif) but not to MINC.

```
mrconvert dicom_images/ my_data.mif
```

6. "pure Python":

For Python, one can use the library pydicom to read DICOM files, and the library nibabel to save in the MINC format.

```python
import pydicom
import nibabel as nib
from nibabel.spatialimages import ImageDataError

def convert_dicom_to_minc(dicom_file, minc_file):
    try:
        dc = pydicom.read_file(dicom_file)
        data = dc.pixel_array
        affine = np.eye(4)
        img = nib.Nifti1Image(data, affine)
        nib.save(img, minc_file)
    except Exception as e:
        print(e)

dicom_file = 'dicom_images/*.dcm'
minc_file = 'my_data.mnc'
convert_dicom_to_minc(dicom_file, minc_file)
```

7. SPM:

SPM doesn't inherently support MINC formats. But, it does provide a 'spm_dicom_convert' function for converting DICOM to NIFTI, which can then be converted to MINC.

```matlab
spm('defaults', 'PET');
spm_jobman('initcfg');

headers = spm_select('FPList', 'dicom_images/', '.*\.dcm');
spm_dicom_convert(headers,'all',[],[],'nifti');
```

Please note that some of these pipelines require intermediate steps because they don't support direct DICOM to MINC conversion.