[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/statistical_analysis/functional_connectivity_density_mapping.md)
# Functional Connectivity Density Mapping

I'm sorry for any confusion, but as a text-based model AI developed by OpenAI, I'm unable to execute code or provide scripts for each of the different neuroimaging software tools you mentioned. However, I can certainly explain a general approach to perform Functional Connectivity Density Mapping using these tools. Let's go through each one.

## <img src="../icons/afni.png" height="24px" /> AFNI
AFNI does not have a specific function dedicated to Functional Connectivity Density Mapping (FCDM). General functional connectivity can be conducted using 3dTcorr1D or 3dTcorrMap.

## <img src="../icons/ants.png" height="24px" /> ANTs
ANTs mainly focuses on anatomical image registration and segmentation, it does not have a specific function for FCDM.

## <img src="../icons/fsl.png" height="24px" /> FSL
```
# Generate a mask for the brain
bet2 subject_image.nii subject_brain.nii

# Perform functional connectivity density mapping
fsl_glm -i subjectA.nii.gz -d matrix -o fcdm.nii.gz
```
The `fsl_glm` command can be used to perform general linear modelling, which is useful for FCDM. You may need to construct your design matrix to represent the correlations between regions of interest.

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
There's no specific method in FreeSurfer for FCDM. FreeSurfer is best used for cortical thickness and surface-based processing.

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
MRtrix is more tuned for diffusion MRI analyses, and does not have straightforward functions for FCDM.

## <img src="../icons/r.png" height="24px" /> R
For the R programming language, you would need to make use of existing neuroimaging packages, such as the `neurobase` package, and write custom code to perform FCDM.

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
It mainly focuses on surface-based data visualization. FCDM task would be better accomplished through other software.

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
% Load the SPM.mat file
load('SPM.mat')

% Load the into voxel space
V = spm_vol('Functional.nii');

% Apply the SPM model to the data
Y = spm_get_data(V,XYZ);

% Perform FCDM
conn = corrcoef(Y);

% Save the result
save('fcdm.mat', 'conn')
```
In this sample script, we've loaded a SPM.mat file, which is assumed to contain the necessary voxel space and design matrix for FCDM. 

Again, please note that these are not direct scripts for Functional Connectivity Density Mapping, but rather pointing you to the relevant functions which you may need to use in each software to then compute FCDM. Crafting these scripts for your need would indeed be a very task-oriented procedure that you would have to tailor to the needs of your data.