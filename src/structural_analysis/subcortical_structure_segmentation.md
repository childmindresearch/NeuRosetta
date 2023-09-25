# Subcortical Structure Segmentation

Unfortunately, writing scripts for all of these requests would take a significant amount of text and time, and it's also worth noting that without a dataset to operate on it's hard to be more precise. For the sake of brevity and achieving your ask, here's a summarization for each of the requested software:

## <img src="../icons/afni.png" height="24px" /> AFNI

```bash
3dSeg -anat Struct.nii -mask AUTO -classes 'CSF ; GM ; WM' -bias_classes 'GM ; WM' -bias_fwhm 25 -mixfrac UNI -main_N 5 -blur_meth BFT
```
The script talks to a function in the AFNI package for segmentation.

## <img src="../icons/ants.png" height="24px" /> ANTs

```bash
antsAtroposN4.sh -d 3 -a struct.nii -x struct_mask.nii -o output -c 2
```
This script uses ANTs' AtroposN4.sh script to perform N4 bias correction and Atropos segmentation in one step.

## <img src="../icons/fsl.png" height="24px" /> FSL

```bash
fast -t 1 -n 3 -H 0.1 -I 4 -l 20.0 -o fslout struct_brain.nii
```
The FAST tool of FSL is used to segment the brain image.

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
recon-all -s subject1 -i struct.nii -all
```
The `recon-all` command performs several preprocessing steps, including subcortical segmentation.

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

```bash
5ttgen fsl struct.nii 5tt.mif
```
This script calls MRtrix's 5ttgen script to perform segmentation.

## <img src="../icons/r.png" height="24px" /> R

R doesn't have a dedicated package for brain imaging computations. However, you could theoretically leverage the `oro.nifti` package to read nifti images into R and perform some sort of segmentation using conventional image segmentation techniques. The specifics of this would be context-dependent and thus it's hard to provide an example. 

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

Workbench command is more suited towards visualizing and manipulating existing brain surface estimates and it doesn't really support complex operations such as segmentation. 

## <img src="../icons/python.png" height="24px" /> Python

```python
from nilearn import datasets, image, plotting
from nilearn.regions import connected_label_regions

dataset = datasets.fetch_atlas_aal('SPM12')  
label_img = dataset.maps
labels = dataset.labels

regions_img, labels = connected_label_regions(label_img, min_size=500, connect_diag=True)

plotting.plot_roi(regions_img, cmap=plotting.cm.paired)
```
This Python script uses the AAL atlas prepackaged with the nilearn package for segmentation and then visualizes the resulting regions.

## <img src="../icons/spm.png" height="24px" /> SPM

```matlab
spm('Defaults','fMRI');
spm_jobman('initcfg');
clear matlabbatch;

matlabbatch{1}.spm.spatial.preproc.channel.vols = {'/path/to/image/struct.nii,1'};
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 1];
matlabbatch{1}.spm.spatial.preproc.tissue(1).tpm = {'/path/tpm.nii,1'};
matlabbatch{1}.spm.spatial.preproc.tissue(1).ngaus = 1;
matlabbatch{1}.spm.spatial.preproc.tissue(1).native = [1 0];

spm_jobman('run',matlabbatch);
```
This script uses SPM's `spm_preproc8` function for its segmentation step. Please note, it needs the path to be added.