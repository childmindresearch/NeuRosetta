AFNI
```
#!/bin/bash
3dAFNItoNIFTI -prefix output.nii input.mnc
```

ANTs
```
#!/bin/bash
ANTS 3 -m MSR[output.nii,input.mnc,1,32,fixed.nii] -o input.nii
```

FSL
``` 
#!/bin/bash
fslchfiletype NIFTI input.mnc output.nii
```

FreeSurfer
``` 
#!/bin/bash
mri_convert input.mnc output.nii
```

MRtrix
``` 
#!/bin/bash
mrconvert input.mnc output.nii -datatype float32
```

R
```
library(oro.nifti)

# load MINC file
mnc <- readMNC("input.mnc")

# convert to NIfTI
nii <- as(mnc, "nifti")

# save NIfTI file
writeNIfTI(nii, "output.nii")
```

Workbench Command
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

SPM (via a MATLAB script)
```matlab
spm('defaults', 'FMRI');
spm_jobman('initcfg');

matlabbatch{1}.spm.util.minc.data = {'input.mnc'};
matlabbatch{1}.spm.util.minc.output = {'output.nii'};
matlabbatch{1}.spm.util.minc.dtype = 4;

spm_jobman('run', matlabbatch);
```