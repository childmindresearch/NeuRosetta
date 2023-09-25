# Bias Field Correction

Unfortunately, it would be impractical to provide a full script for each software package as they are all quite involved and have their own interfaces and ways of working. However, here is a snippet of each example script that pertains to performing Bias Field Correction:

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
3dUnifize -prefix out.nii.gz -input in.nii.gz
```
The function `3dUnifize` performs bias field correction in AFNI.

## <img src="../../icons/ants.png" height="24px" /> ANTs

```bash
N4BiasFieldCorrection -d 3 -i input.nii.gz -o output.nii.gz
```
The command `N4BiasFieldCorrection` performs bias field correction in ANTs.

## <img src="../../icons/fsl.png" height="24px" /> FSL

```bash
fast -B -b bias -i in.nii.gz -o out
```
The function `fast` with `-B` instruction performs bias field correction in FSL.

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
mri_nu_correct.mni --i input.mgz --o output.mgz --distance 25 --proto-iters 1000
```
The command `mri_nu_correct.mni` performs bias field correction in FreeSurfer.

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix

```bash
mtnormalise in_fod.mif in_wmfod_norm.mif in_csf.mif in_csf_norm.mif -mask in_mask.mif
```
The command `mtnormalise` performs Bias Field Correction in MRtrix.

## <img src="../../icons/r.png" height="24px" /> R

Brain imaging in R is usually done with the help of specialized packages. The mmand package can be used for bias field correction.

```R
library(mmand)
img <- mmand::imread("input.tif")
correction <- mmand::bias.correct(img)
```

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command

The Workbench Command doesn't directly offer a bias field correction command.

## <img src="../../icons/python.png" height="24px" /> Python
```python
from nipype.interfaces.ants import N4BiasFieldCorrection
correct = N4BiasFieldCorrection()
correct.inputs.input_image = 'T1.nii.gz'
correct.inputs.output_image = 'T1_corrected.nii.gz'
correct.run() 
```
The `N4BiasFieldCorrection` interface from the nipype library can be used for bias field correction in pure python.

## <img src="../../icons/spm.png" height="24px" /> SPM

```m
matlabbatch{1}.spm.spatial.preproc.channel.vols = {'input.nii,1'};
matlabbatch{1}.spm.spatial.preproc.channel.biasreg = 0.001;
matlabbatch{1}.spm.spatial.preproc.channel.biasfwhm = 60;
matlabbatch{1}.spm.spatial.preproc.channel.write = [1 1];
spm('defaults', 'PET');
spm_jobman('run', matlabbatch);
```
This MATLAB script uses the SPM library to run the bias field correction. The `spm.spatial.preproc.channel` functions are used for this task.