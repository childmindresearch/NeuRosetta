Sure, below are the minimal example scripts you need for each.

## AFNI

```csh
#! /bin/tcsh

afni_proc.py -subj_id 'subj1' \
-bash \
-blocks tshift align tlrc volreg blur mask scale regress \
-copy_anat 'anatomy/anat.nii' \
-dsets 'rest/rest.nii' \
-tcat_remove_first_trs 3 \
-align_opts_aea -cost lpc+ZZ -giant_move -check_flip \
-align_epi_anat.py -dset1 'anatomy/anat.nii' -dset2 'rest/rest.nii' \
```

## ANTs
```bash
#!/bin/bash

antsRegistrationSyN.sh -d 3 \
-f structural.nii -m restingstate.nii \
-o outputname \
```

## FSL

```bash
#!/bin/bash

flirt -in struct_image.nii -ref target_image.nii -omat struct2target.mat -out struct2target.nii.gz \
```

## FreeSurfer

```bash
#!/bin/tcsh

mri_coreg --s subject --mov functional.nii --reg register.dat
```

## MRtrix

```bash
#!/bin/bash

flirt -in T1_image.nii -ref DTI_image.nii -dof 12 -omat T12DTI.mat
transformconvert T12DTI.mat T1_image.nii DTI_image.nii flirt_import T12DTI.txt
```

## pure PythonSPM

```python
import spm1d
spm1d.norm.main('structural.nii', 'normalized.nii', template='template.nii')
```

Please note that in practice, these commands' parameters, like names of the input files and any optional flags, would likely need to be customized to your data and experiment. Make sure to refer to each package's comprehensive documentation to fully understand and utilize its capabilities.