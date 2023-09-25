# Task-Based fMRI Analysis

some of these software libraries don't have direct support for task-based fMRI analysis or are considered inappropriate for such tasks. Nevertheless, here are short minimal example scripts for AFNI, FSL, and SPM (via MATLAB). 

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
# First, let's create a model design
3dDeconvolve -input pb00.Tech001.tshift+orig.HEAD \
    -censor motion_Tech001_censor.1D \
    -polort 5 \
    -num_stimts 1 \
    -stim_times 1 'MOVIE_times.1D' 'BLOCK(20,1)'  \
    -stim_label 1 MOVIE \
    -fout -tout \
    -x1D X.xmat.1D \
    -xjpeg X.jpg -nocout -bucket stats.Tech001_REML \
    -errts errts.Tech001.fanaticor+orig.HEAD

# And then run the analysis using AFNI
3dREMLfit -matrix X.xmat.1D \
    -input pb00.Tech001.tshift+orig.HEAD \
    -Rbuck stats.Tech001_REML \
    -Rvar stats.Tech001_REMLvar \
    -fout -tout -verb -Rwherr whitened_errts.Tech001_REML \
```

## <img src="../../icons/fsl.png" height="24px" /> FSL

```bash
# First, let's setup some variables
task_dir="PATH_TO_TASK_DIR"
highres_head="PATH_TO_HIGHRES_HEAD"
highres_brain="PATH_TO_HIGHRES_BRAIN"
run="PATH_TO_RUN"
output="PATH_TO_OUTPUT"

# Now, we create a model design
feat_model $task_dir 

# And then run the analysis
feat $task_dir.fsf
```

## <img src="../../icons/spm.png" height="24px" /> SPM

```matlab
% Initialize SPM
spm('defaults', 'FMRI');

% Specify paths
functional_run = 'PATH_TO_FUNCTIONAL_RUN';
structural_image = 'PATH_TO_STRUCTURAL_IMAGE';

% Specify matlabbatch configuration
matlabbatch{1}.spm.spatial.coreg.estimate.ref = structural_image;
matlabbatch{1}.spm.spatial.coreg.estimate.source = functional_run;
matlabbatch{1}.spm.spatial.coreg.estimate.other = {''};
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.cost_fun = 'nmi';
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.sep = [4 2];
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.tol = [0.02 0.02 0.02 0.001 0.001 0.001 0.01 0.01 0.01 0.001 0.001 0.001];
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.fwhm = [7 7];

% Run the analysis with SPM
spm_jobman('run', matlabbatch);
```

For other libraries like ANTs, FreeSurfer, MRtrix, R, you will need to look into the details of the specific libraries and operations available. Most of these libraries cannot perform fMRI analysis without help from Python packages like Nilearn, PySurfer, or R packages like fslr and antsR. Pure Python implementations like nilearn or PySurfer usually wrap around an existing software like AFNI or FSL.