[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/diffusion_mri_analysis/mean_diffusivity_md_mapping.md)
# Mean Diffusivity (MD) Mapping

in providing example scripts, it's worth noting that brain imaging analysis tools are usually standalone software applications. It's very complex to find a minimal script that can map Mean Diffusivity (MD) for each of the mentioned APIs and command line interfaces, as they all have their own workflows for this task. However, here are some general descriptions of the workflow in different tools:

## <img src="../icons/afni.png" height="24px" /> AFNI
```Bash
# DTI requires pre-processing before we can compute Mean Diffusivity 
afni_proc.py -dsets DTI_data.nii.gz -copy_anat ANAT_data.nii.gz -dti_tr 2.5 -regress_stim_times stim_times*
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```Bash
# In ANTs, the Mean Diffusivity can be estimated if the Diffusion Tensor Image (DTI) is given
ComputeDTIParameters -d DTI_data.nii.gz -m MD
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```Bash
# DTIFIT is generally used for creating MD maps in FSL
dtifit --data=DTI_data.nii.gz --mask=brain_mask.nii.gz --bvecs=bvecs --bvals=bvals --out=dti
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```Bash
# FreeSurfer doesn't directly compute Mean Diffusivity, but it can be processed if the DTI is given
mri_convert DTI_data.nii.gz mri/out.mgz
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```Bash
# In MRtrix, the Mean Diffusivity can also be calculated if the DTI has been estimated first
dwi2tensor DTI_data.nii.gz - | tensor2metric - -mean diffusivity.nii.gz
```

## <img src="../icons/r.png" height="24px" /> R
```R
# R requires additional packages to perform MD analysis such as dti
library(dti)
data <- readDWIdata("DTI_data.nii.gz")
b0 <- data$bvals==0
MD <- mean(data$ADC[!t0,])
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```Bash
# The Workbench Command doesn't directly compute Mean Diffusivity. However, it can visualize MD maps if they have been created with another tool.
wb_command -cifti-smoothing dti_MD.dscalar.nii 6 6 COLUMN dti_MD_sm6.dscalar.nii
```

## <img src="../icons/spm.png" height="24px" /> SPM
```MATLAB
% SPM doesn't directly compute Mean Diffusivity, but it can be performed if the DTI is processed
spm('defaults','fmri')
spm_jobman('initcfg')
matlabbatch{1}.spm.tools.dti.dtifit.dtidata{1} = 'DTI_data.nii.gz';
matlabbatch{1}.spm.tools.dti.dtifit.outbasename = 'DTI';
spm_jobman('run',matlabbatch);
MD = spm_read_vols(spm_vol('DTI_MD.nii.gz'));
```

## <img src="../icons/python.png" height="24px" /> Python
```Python
# Python needs packages such as nibabel and dipy for Mean Diffusivity computation
import nibabel as nib
import numpy as np
from dipy.reconst.dti import fractional_anisotropy, color_fa, lower_triangular

img = nib.load('DTI_data.nii.gz')
data = img.get_fdata()
md = np.mean(data, axis=-1)
```