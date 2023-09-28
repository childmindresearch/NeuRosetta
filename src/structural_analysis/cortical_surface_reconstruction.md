[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/structural_analysis/cortical_surface_reconstruction.md)
# Cortical Surface Reconstruction

while I cannot run these scripts for you, I can certainly provide an example of how they might be structured. Here are example scripts for the different brain imaging software packages you mentioned:

## <img src="../icons/afni.png" height="24px" /> AFNI

```
#!/bin/tcsh
3dSkullStrip -input T1.nii -prefix brain_mask.nii
3dresample -master T1.nii  -prefix brain_mask_resampled.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs

```
#Resampling
antsApplyTransforms -d 3 -i brain.nii.gz -r brain.nii.gz  -o brain_resampled.nii.gz -n NearestNeighbor
```

## <img src="../icons/fsl.png" height="24px" /> FSL

```
# skull stripping 
bet T1.nii T1_brain.nii
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

```
#!/bin/tcsh
recon-all -i T1.nii -subjid subject1 -all
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

```
# mask generation
dwi2mask dwi.mif mask.mif
```

## <img src="../icons/r.png" height="24px" /> R

```
# Assuming you've already loaded your data into variable "brain"
library(neurobase)
brain_mask <- mask(brain, type = "otu")
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

```
# Generate a mask with wb_command 
wb_command -volume-math "(x > 0) ? 1 : 0" brain_mask.nii -var x T1.nii
```

## <img src="../icons/python.png" height="24px" /> Python

```python
import nibabel as nib

# Load data
img = nib.load('T1.nii.gz')

# Image resampling
resampled_img = nib.Nifti1Image(img.dataobj, img.affine.dot(np.diag([1, 2, 3, 1])))
nib.save(resampled_img, 'brain.nii.gz')
```

## <img src="../icons/spm.png" height="24px" /> SPM

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