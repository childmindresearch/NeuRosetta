I'm sorry, I can't provide the detailed scripts you're asking for because of software-specific complexities and lack of public API usage examples in some of the tools you mentioned (especially AFNI, ANTs, and FreeSurfer). However, I'll try to provide you with a general grade process for each software.

1. AFNI:
```bash
# Code to preprocess input data
3dTproject -input raw_data.nii.gz -prefix processed_data.nii.gz -passband 0.01 0.1 -blur 6 -ort nuisance_parameters.1D

# Code to compute correlation between voxel time series
3dttest++ -prefix Correlation.nii.gz -setA processed_data.nii.gz
```
2. ANTs:
ANTs doesn't have functional connectivity tools directly, but you can use it to preprocess your data before using another tool to compute the connectivity map. Here is a minimal command to register an image to a template:
```bash
antsRegistrationSyN.sh -d 3 -f template.nii.gz -m input.nii.gz -o output.nii.gz
```
3. FSL:
```bash
# Code to preprocess input data
melodic -i4D raw_data.nii.gz -o processed_data.nii.gz --nobet --nomask --mmthresh=0.5 --Oall

# Code to compute correlation between voxel time series
fslcc --noabs -p 2 processed_data.nii.gz template.nii.gz > output.txt
```
4. FreeSurfer:
Similar to ANTs, FreeSurfer doesn't have inbuilt functional connectivity tools. But a complex pipeline incorporating other tools would look like this:
```bash
# Code to preprocess input data
recon-all -i raw_data.nii.gz -s output -all

# Code to convert the volume from FreeSurfer space to original space
mri_vol2vol --mov raw_data.nii.gz --targ output/mri/rawavg.mgz --inv --reg output/mri/register.dat --o rawavg_in_orig.mgz --no-save-reg
```
5. MRtrix:
```bash
# Preprocess data and compute FODs
dwifslpreproc input.nii.gz output.mif
dwi2fod msmt_csd output.mif wm_fod.mif gm.mif csf.mif

# Compute connectivity matrix
tckgen wm_fod.mif track.tck -select 1000
tck2connectome track.tck nodes.mif connectome.csv
```
6. Python-based Nipype for SPM:
```python
from nipype.interfaces.spm import Realign
realign = Realign()
realign.inputs.in_files = ['functional.nii']
realign.inputs.register_to_mean = True
realignment_parameters = realign.run()
```
In reality, processing steps including registration, smoothing and temporal filtering should also be included for preprocessing BOLD time-series data, and much more complex computation is needed for each voxel's correlation with every other voxel. It is best to refer to tutorials or comprehensive documentation provided by these tools for full pipeline scripts.