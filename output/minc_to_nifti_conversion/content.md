Sure, here are some examples of how one would convert MINC to NIfTI file types using different software. 

Please note that the success and correctness of these conversions are highly dependent on the version of the software and the operating system that the user is employing. Also, syntax and instruction manual should be properly referenced for the respective software which you are using.

1. **AFNI**
```bash
3dAFNItoNIFTI -prefix output.nii input.mnc
```

2. **ANTs**
ANTs itself does not support MINC, but both formats are in ITK, so you might use it indirectly. You can convert between different image formats via `ConvertImagePixelType` command. This should work for conversion between MINC and NIFTI if ANTs is compiled with ITK that has MINC format support.

3. **FSL**
```bash
fslchfiletype NIFTI_GZ input.mnc output.nii.gz
```

4. **FreeSurfer**
FreeSurfer also does not natively support MINC to NIfTI conversion. Although, if you have the MINC toolkit installed, you can first convert your MINC file to a format FreeSurfer accepts (like dicom or nifti).

5. **MRtrix**
```bash
mrconvert input.mnc output.nii
```

6. **Pure-Python**
```python
import nibabel as nib

img = nib.load('input.mnc')
nib.save(img, 'output.nii')
```

7. **SPM**
You can use SPM Conversion Utility with the GUI to perform this operation as SPM is a MATLAB based program. There isn't a specific script provided for converting MINC to NIfTI directly in the software. But you can use MATLAB and SPM functions to achieve the conversion (We aren't considering MATLAB a 'pure Python'), but the common purpose of using the software is to analyze the data, not convert it. It's recommended using the specialized functions and software for these conversions.  

For detailed instructions, please refer to the documentation of each of these software libraries.