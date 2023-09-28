[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/data_format_conversion/minc_to_nifti_conversion.md)
# MINC to NIfTI Conversion

## <img src="../icons/afni.png" height="24px" /> AFNI
```
#!/bin/bash
3dAFNItoNIFTI -prefix output.nii input.mnc
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```
#!/bin/bash
ANTS 3 -m MSR[output.nii,input.mnc,1,32,fixed.nii] -o input.nii
```

## <img src="../icons/fsl.png" height="24px" /> FSL
``` 
#!/bin/bash
fslchfiletype NIFTI input.mnc output.nii
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
``` 
#!/bin/bash
mri_convert input.mnc output.nii
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
``` 
#!/bin/bash
mrconvert input.mnc output.nii -datatype float32
```

## <img src="../icons/r.png" height="24px" /> R
```
library(oro.nifti)

# load MINC file
mnc <- readMNC("input.mnc")

# convert to NIfTI
nii <- as(mnc, "nifti")

# save NIfTI file
writeNIfTI(nii, "output.nii")
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
``` 
#!/bin/bash
wb_command -cifti-convert -from-nifti input.mnc output.nii
```

Pure Python (requires nibabel, numpy)
```python
import nibabel as nib
import numpy as np

# Load MINC file
mnc = nib.load('input.mnc')

# Save as NIfTI
nib.save(nib.Nifti1Image(np.asanyarray(mnc.dataobj), mnc.affine), 'output.nii')
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
spm('defaults', 'FMRI');
spm_jobman('initcfg');

matlabbatch{1}.spm.util.minc.data = {'input.mnc'};
matlabbatch{1}.spm.util.minc.output = {'output.nii'};
matlabbatch{1}.spm.util.minc.dtype = 4;

spm_jobman('run', matlabbatch);
```