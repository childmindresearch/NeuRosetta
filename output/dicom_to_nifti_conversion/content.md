Sure, I can provide short examples with basic commands for DICOM to NIfTI conversion using various brain imaging software tools. It's important to note that the file and directory names should be adjusted to match your actual file paths.

Remember to check each software's documentation for a more detailed explanation on how to use their functions and adjust parameters.

1. **AFNI**

```
#!/bin/tcsh
Dimon -write_images -file_type AFNI -outfile_prefix dset \
 -infile_prefix glob('*.dcm') -dicom_org
```

2. **ANTs**
   
ANTs does not natively support DICOM to NIfTI conversion. You might opt for another tool for this conversion then bring the NIfTI file into ANTs.

3. **FSL**

```
#!/bin/bash
dcm2nii -n y -g y -o /output/dir /input/DICOM/dir
```

4. **FreeSurfer**

```
#!/bin/tcsh
mri_convert DICOM_directory/image.dcm output.nii
```

5. **MRtrix**

```
#!/bin/bash
mrconvert /input/DICOM/directory output.nii
```

6. **Pure Python**

You can use `pydicom` and `nibabel` in Python for this purpose.

```python
from pydicom import dcmread
import nibabel as nib

dcm = dcmread('input.dcm')
data = dcm.pixel_array

new_image = nib.Nifti1Image(data, affine=np.eye(4))
nib.save(new_image, 'output.nii')
```

7. **SPM**

SPM requires MATLAB and doesn't support command-line only usage. But here is an example MATLAB script using SPM's functions:

```MATLAB
spm('Defaults','fMRI');
spm_jobman('initcfg');
matlabbatch{1}.spm.util.dicom.data = '<insert_paths_here>'; % DICOM files 
matlabbatch{1}.spm.util.dicom.root = 'flat';
matlabbatch{1}.spm.util.dicom.outdir = '<insert_output_directory_here>'; % output directory
matlabbatch{1}.spm.util.dicom.convopts.format = 'nii';
matlabbatch{1}.spm.util.dicom.convopts.icedims = 0;
spm('run', matlabbatch);
```
You should replace the placeholders with your actual DICOM paths and desired output directory. This will save the converted images in NIfTI format in the specified output directory. The format 'nii' specifies NIfTI format.