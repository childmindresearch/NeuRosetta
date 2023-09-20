Given the complexity of neuroimaging analysis pipelines and the nature of coding, it's not possible to provide scripts exactly as you requested. But I can guide you through a brief simplified version of how analysis can look in such packages.

# 1) AFNI (Analysis of Functional NeuroImages)
```bash
# Preprocess
afni_proc.py -subj_id sub-01 -blocks tshift align tlrc volreg blur mask scale regress -out_dir sub-01.results

# Run the first level analysis
3dDeconvolve -input pb03.sub-01.r01.blur+tlrc -1Dfile dfile.r01.1D -mask mask_group+tlrc -polort A -num_stimts 3 -stim_times 1 'stim_times_01.1D' 'BLOCK(12,1)' -stim_label 1 'Task1' -stim_times 2 'stim_times_02.1D' 'BLOCK(12,1)' -stim_label 2 'Task2' -stim_times 3 'stim_times_03.1D' 'BLOCK(12,1)' -stim_label 3 'Task3' -gltsym 'SYM: Task2 -Task1' -fout -tout -errts errts.sub-01.r01.fanaticor+tlrc -bucket stats.sub-01.r01_REML -cbucket cstats.sub-01.r01_REML -jobs 2 -xjpeg X.sub-01.r01
```

# 2) ANTs (Advanced Normalization Tools)
```bash
# Normalization
antsRegistrationSyN.sh -d 3 -f sub-01_T1w.nii.gz -m sub-01_func.nii.gz -o output

# Smoothing (as it often follows normalization)
SmoothImage 3 sub-01_func_pt1.nii.gz 1 sub-01_func_pt1_smooth.nii.gz 1
```

# 3) FSL (FMRIB Software Library)
```bash
# FEAT GLM setup
feat design.fsf

# Applying the GLM
feat design.feat
```

# 4) FreeSurfer
```bash
# Preprocess
recon-all -subjid sub-01 -i sub-01_T1w.nii.gz -all -clean

# First level surface analysis
mri_glmfit --y sub-01_func.mgz --fsgd design.fsgd --C contrast.mtx --glmdir glmresults
```

# 5) MRtrix (Magnetic Resonance Imaging in Python)
```bash
# Preprocess
dwipreproc sub-01_dwi sub-01_dwi_prep.mif

# First level analysis
dwi2tensor dwi.mif tensor.mif -mask mask.mif
```

# 6) Python with Nipype (for SPM)
```python
from nipype.interfaces.spm import Level1Design, EstimateModel, EstimateContrast

# Set up design matrix
design = Level1Design()
design.inputs.timing_units = 'secs'
design.inputs.interscan_interval = 2.5
# ... set other design variables here
design.run()

# Estimate model
est_model = EstimateModel()
est_model.inputs.estimation_method = {'Classical': 1}
# ... set other model variables here
est_model.run()

# Estimate contrast
con_est = EstimateContrast()
# ... set up contrast variables here
con_est.run()
```

Please, note that these example codes are extremely simplified and it's almost certain that they won't run correctly without modification and other supplement operations. Each neuroimaging package has comprehensive and detailed tutorials and manuals that provide a full walkthrough of various types of analyses.