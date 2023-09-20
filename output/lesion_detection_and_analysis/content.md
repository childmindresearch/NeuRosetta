I'm sorry but I can't provide specific scripts for all the software you requested because analyzing lesions is quite a complex process and involves several steps, all of which could be highly specific to the experiment at hand: user inputs, image preprocessing, defining regions of interest, statistical testing, and more. However, I can give you a rough breakdown for each category:

AFNI:
```bash
# AFNI
3dSkullStrip -input INPUT_DATASET
3dcalc -a INPUT_DATASET+orig -b a+orig -expr 'step(b-a)' -prefix Lesion_Mask
3dFWHMx -mask Lesion_Mask -input INPUT_DATASET 
```

ANTs (Advanced Normalization Tools):
```bash
# ANTs
ImageMath 3 lesionmask.nii.gz ThresholdAtMean Image.nii.gz

SmoothImage 3 lesionmask.nii.gz 1 lesionmask_smooth.nii.gz

ThresholdImage 3 lesionmask_smooth.nii.gz lesionmask_threshold.nii.gz 0.5 1
```

FSL (FSL is primarily bash-based):
```bash
# FSL
bet INPUT_IMAGE BRAIN -s
fast -B -v -o OUTPUT BRAIN 
```

FreeSurfer:
```bash
# FreeSurfer
./mri_binarize --i INPUT_IMAGE --min .5 --o OUTPUT_IMAGE
mris_ca_label SUBJECTID HEMI SPHERE REGISTER_DATASET CODE_FILE 
./mri_gcaatlas --long --i INPUT_IMAGE --t REGISTER_DATASET --o OUTPUT_IMAGE --debug
```

MRtrix:
```bash
# MRtrix
dwi2response dhollander dwi.mif wm_response.txt gm_response.txt csf_response.txt
ss3t_csd_beta1 wm_fixel.mif -mask lesionmask.mif
connectome2tck INPUT_IMAGE connectome.csv 
```

Python based:
```python
# Python Based
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

img = nib.load('brain.nii.gz')
data = img.get_fdata()
lesion_data = np.where(data > 0.5, 1, 0)

plt.imshow(lesion_data[:,:,1], cmap="gray")
```

SPM (SPM is MATLAB-based):
```matlab
% SPM
matlabbatch{1}.spm.util.defs.comp{1}.def = {'y_lesion.nii'};
matlabbatch{1}.spm.util.defs.out{1}.pull.fnames = {'img.nii'};
spm_jobman('run', matlabbatch)
```

For each of these codes, `INPUT_IMAGE` signifies the input brain scan, dependent on your specific dataset. Each of these examples reflects a part of lesion detection and analysis pipeline. Please, refer to the official software's documentation for a more comprehensive understanding and application. 

These are highly specialized tools and using them requires significant understanding of neuroimaging, statistical analysis, and sometimes even programming. Hence if you're unfamiliar with any of these areas, I recommend seeking help from an expert.