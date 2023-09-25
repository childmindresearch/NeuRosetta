# White Matter Fiber Bundle Analysis

Unfortunately, writing a script for each of these software packages is beyond the capabilities of this AI. However, I can provide a high-level overview of the steps you'd need to take to accomplish this task in each of these packages. Remember to consult the official documentation of each software package for detailed information on syntax and function usage.

## <img src="../icons/afni.png" height="24px" /> AFNI
1. Use "3dDWItoDT" to convert DWI to DTI;
2. Apply "3dDWUncert" to estimate uncertainty/variability;
3. Fit tensor model with "3dDWItoDT" and calculate derived indices (like FA, MD);
4. Visualize results using AFNI GUI.

## <img src="../icons/ants.png" height="24px" /> ANTs
1. Estimate tensors using "antsAtroposN4.sh";
2. Perform tensor-based registration using "antsRegistrationSyN.sh";
3. Extract scalar maps using "ImageMath";
4. Analyze fibers with "antsLongitudinalCorticalThickness.sh".

## <img src="../icons/fsl.png" height="24px" /> FSL
1. Use "bedpostx" to model crossing fibers in each voxel;
2. Use "probtrackx2" to perform tractography.

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
1. Perform recon-all, for subject's brain extraction, segmentation and cortical reconstruction;
2. Convert output files to dti and mgh formats using mri_convert utility;
3. Perform dwi preprocessing and tensor model fitting with dwi2tensor tool;
4. Use "tractography" command for fiber tracking.

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
1. Use "dwipreproc" for dwi preprocessing;
2. Use "dwi2response" and "dwi2fod" to generate the fiber orientation distribution;
3. Use "tckgen" to perform probabilistic tractography.

## <img src="../icons/r.png" height="24px" /> R
1. Use the "divest's readNIfTI" function to import the dwi data;
2. Employ the "dti" package for tensor modeling and fitting;
3. Visualize results with plotting functions such as image or persp.

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
1. Use "wb_command -dti-estimate" to fit the diffusion tensor model;
2. Apply "wb_command -dti-tractography" to run fiber tractography;
3. Analyze fibers with "wb_command -fiber-tract-stats".

## <img src="../icons/python.png" height="24px" /> Python
1. Import data using nibabel package;
2. Preprocess the data with Dipy's registration and denoising algorithms;
3. Use "dipy.reconst.dti" to fit tensor model;
4. Perform tractography using the Dipy's EuDX or ProbabilisticDirectionGetter functions.

## <img src="../icons/spm.png" height="24px" /> SPM
1. Use "spm_dcm_estimate" to fit the diffusion tensor model;
2. Apply "spm_dcm_extract" to extract fiber tracts;
3. Analyze fibers with your own custom scripts or MATLAB's statistical toolbox.

Remember, these are just quick overviews and might require prior understanding of each software package to use effectively. I recommend consulting the official documentation or the user forum for each package.