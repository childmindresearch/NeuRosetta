Sure, while I cannot run these scripts for you, I can certainly provide an example of how they might be structured. Here are example scripts for the different brain imaging software packages you mentioned:

1. **AFNI**

```
#!/bin/tcsh
3dSkullStrip -input T1.nii -prefix brain_mask.nii
3dresample -master T1.nii  -prefix brain_mask_resampled.nii
```

2. **ANTs**

```
#Resampling
antsApplyTransforms -d 3 -i brain.nii.gz -r brain.nii.gz  -o brain_resampled.nii.gz -n NearestNeighbor
```

3. **FSL**

```
# skull stripping 
bet T1.nii T1_brain.nii
```

4. **FreeSurfer**

```
#!/bin/tcsh
recon-all -i T1.nii -subjid subject1 -all
```

5. **MRtrix**

```
# mask generation
dwi2mask dwi.mif mask.mif
```

6. **R**

```
# Assuming you've already loaded your data into variable "brain"
library(neurobase)
brain_mask <- mask(brain, type = "otu")
```

7. **Workbench Command**

```
# Generate a mask with wb_command 
wb_command -volume-math "(x > 0) ? 1 : 0" brain_mask.nii -var x T1.nii
```

8. **Python (via nibabel)**

```python
import nibabel as nib

# Load data
img = nib.load('T1.nii.gz')

# Image resampling
resampled_img = nib.Nifti1Image(img.dataobj, img.affine.dot(np.diag([1, 2, 3, 1])))
nib.save(resampled_img, 'brain.nii.gz')
```

9. **SPM (via a MATLAB script)**

```MATLAB
spm('Defaults','fMRI');
spm_jobman('initcfg');
clear matlabbatch;

matlabbatch{1}.spm.spatial.preproc.channel.vols = {'T1.nii,1'};
matlabbatch{1}.spm.spatial.preproc.channel.boundary = 1;
matlabbatch{1}.spm.spatial.preproc.channel.biasreg = 0.001;
matlabbatch{1}.spm.spatial.preproc.channel.biasfwhm = 60;
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 1];

spm_jobman('run',matlabbatch);
clear matlabbatch;
```

Please adjust these scripts to fit your dataset. You must replace 'T1.nii' or 'dwi.mif', 'brain.nii.gz', etc. with your actual input file name.

Just keep in mind that these scripts merely outline the most basic function of each software package, and real use cases could require much more complex scripts.

Also, the FreeSurfer and AFNI scripts are written in tcsh instead of bash which is more common today. You could run these command scripts in bash on most systems.