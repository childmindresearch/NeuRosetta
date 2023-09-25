Here are short example scripts for Resting-State fMRI Analysis using different imaging software.

Please note, these are just templates and might need adjustment based on your specific data or research question. 

1. **AFNI**

```python
#!/bin/tcsh
set subj = SUBJECT_ID
set ddir = PATH_TO_DATA_DIRECTORY
afni_proc.py -subj_id $subj -dsets $ddir -blocks tshift align tlrc volreg blur mask regress -copy_anat ANATOMICAL_IMAGE -do_block 'tshift  align tlrc -copy_costs' -tcat_remove_first_trs 0 -volreg_align_to THIRD_VOL -volreg_align_e2a -volreg_tlrc_warp -blur_size 6.0 -regress_anaticor -regress_censor_motion 0.3 -regress_censor_outliers 0.1 -regress_apply_mot_types demean deriv -regress_est_blur_epits -regress_est_blur_errts
```

2. **ANTs**

```bash
motionCorrection <- antsMotionCorr(fixed_image, moving_image)
residuals <- residuals(motionCorrection)
```

3. **FSL**

```bash
#!/bin/bash
set subj=SUBJECT_ID
data_directory=PATH_TO_DATA_DIRECTORY
fsl_motion_outliers -i $data_directory/$subj -o motion_assessment -s output_motion_parameter --fd --thresh=0.9 
```

4. **FreeSurfer**

```bash
recon-all -s subjectname -i pathtoimage.nii.gz -all
bbregister --s subjectname --fmri pathtoimage.nii.gz --init-fsl --bold
mri_vol2vol --mov pathtoimage.nii.gz --targ $SUBJECTS_DIR/subjectname/mri/orig.mgz --interp nearest --o registered.nii.gz --reg $SUBJECTS_DIR/subjectname/bold/004/register.dof6.dat --no-save-reg
```

5. **MRtrix**

```bash
dwifslpreproc input_dwi.mif output_dwi.mif -rpe_none -pe_dir AP -nocleanup -eddy_options " --slm=linear --repol"
```

6. **R**

```R
library(neuroim)
r_mri_data <- read_nii("path_to_nii_file")
summary(r_mri_data)
```

7. **Workbench Command**

```bash
wb_command -cifti-separate 
cifti.dtseries.nii COLUMN -metric CORTEX_LEFT mydata.L.gii -metric CORTEX_RIGHT mydata.R.gii -volume ALL mydata_subcort.nii
```

8. **SPM (via MATLAB)**

```matlab
spm('Defaults','fMRI');
spm_jobman('initcfg');

matlabbatch{1}.spm.temporal.st.scans = {'PATH_TO_YOUR_DATA'}; 
matlabbatch{1}.spm.temporal.st.nslices = NUMBER_OF_SLICES;
matlabbatch{1}.spm.temporal.st.tr = TR;
matlabbatch{1}.spm.temporal.st.ta = TA;
matlabbatch{1}.spm.temporal.st.so = SLICE_ORDER_VECTOR;
matlabbatch{1}.spm.temporal.st.refslice = REFERENCE_SLICE;
matlabbatch{1}.spm.temporal.st.prefix = 'a';

spm_jobman('run',matlabbatch);
```

9. **Pure Python**

```python
import nibabel as nib
from nilearn import image
from nilearn import input_data
from nilearn.connectome import ConnectivityMeasure

# Load a 4D nifti file
path_to_nifti_file ='PATH/TO/FILE.nii'
img = nib.load(path_to_nifti_file)

# Using nilearn's masker to get time series from nifti files
masker = input_data.NiftiLabelsMasker(path_to_atlas_file)
time_series = masker.fit_transform('functional_image.nii.gz')

# Calculate correlation matrix
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]
```

Remember to replace all placeholders like 'SUBJECT_ID', 'PATH_TO_DATA_DIRECTORY', 'ANATOMICAL_IMAGE', 'SUBJECTS_DIR', 'number_of_slices', 'TR', 'TA', etc., with your actual dataset-specific information.