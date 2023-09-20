I'm sorry for the misunderstanding, but it's not possible for me to generate scripts for those software without prior information or data. The code would vary based on the types of images you're working with, the specific functionality you want to incorporate, and the analysis you're conducting. However, I can provide you with a general direction of how you can carry out Dynamic Functional Connectivity in each of those software. Yet, remember that these are just outlines and not actual functional scripts:

1) AFNI 

AFNI has a specific function dedicated to Dynamic Functional Connectivity known as "3dReHo". It would typically look like this:

```bash
3dReHo -prefix ReHo -inset my_func.nii.gz -nneigh Neighboringhood_size -automask
```

2) ANTs

ANTs (Advanced Normalization Tools) does not have a direct built-in function to calculate dynamic functional connectivity, but it provides flexible registration algorithms to perform image registration, normalization, and segmentation that can be used in conjunction with other software packages.

3) FSL

In FSL, you can calculate Dynamic Functional Connectivity through seed-based analysis, dual regression, or Independent Component Analysis (ICA). Here is sample code to start an ICA:

```bash
melodic -i filtered_func_data -o outdir --nobet --bgthreshold=10 --tr=2.2 --mmthresh=0.5 --Oall
```

4) FreeSurfer

FreeSurfer's primary functions are brain surface reconstruction and structural analysis. It does not have direct built-in functions for dynamic functional connectivity.

5) MRtrix

Similar to ANTs and FreeSurfer, MRtrix does not have direct built-in functions for dynamic functional connectivity. Its strength lies in pre-processing and analysis of diffusion MRI data.

6) Python (like nilearn)

Using Python package like Nilearn, you can perform Dynamic Functional Connectivity:

```python
from nilearn.input_data import NiftiLabelsMasker
masker = NiftiLabelsMasker(labels_img='Atlas_filename.nii.gz', standardize=True)
time_series = masker.fit_transform('fmri_filename.nii.gz')
```

7) SPM

In SPM, you can use functions such as spm_fmri_spm_ui to setup your model, spm_spm to estimate it, and then use the resulting beta images in a subsequent Dynamic Functional Connectivity analysis:

```matlab
SPM = spm_fmri_spm_ui(SPM);
SPM = spm_spm(SPM);
```

Again, remember these are just generalized examples. The actual implementation could differ depending on your specific objectives and datasets.