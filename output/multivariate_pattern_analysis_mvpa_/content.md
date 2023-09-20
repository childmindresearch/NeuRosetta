Here are small code snippets illustrating basic workflows in various neuroimaging frameworks:

1. **AFNI**
```
# MVPA using 3dsvm in AFNI
3dsvm -mask brainMask+orig. -trainvol data+orig. \
-trainlabels labels.1D -model myModel
```

2. **ANTs (Advanced Normalization Tools)**
```
# Scripting in ANTs doesn't easily support MVPA
# Here is how to create an average image, normally a step in MVPA
AverageImages 3 output.nii.gz 1 input1.nii.gz input2.nii.gz
```

3. **FSL (FMRIB Software Library)**
```bash
# FSL MVPA example using featquery
# Assuming a feat analysis has already been run
featquery 1 'input.feat' 1 stats/cope1 'my_mvpa_output'
```

4. **FreeSurfer**
```bash
# FreeSurfer preferred tool is mri_glmfit for similar analyses
mri_glmfit --y input.mgh --fsgd design.fsgd --C contrast1.mtx
```

5. **MRtrix**
```bash
# No built-in MVPA in MRtrix
# But you can do simple tensor fitting
dwi2tensor dwi.mif -mask mask.mif dt.mif
```

6. **Python (nilearn package)**

```python
from nilearn.input_data import NiftiMasker
from sklearn import svm
from nilearn.image import load_img

# Load behavioral information
behavioral = pd.read_csv('behavioral_data.csv')
# Load mask and create NiftiMasker object
masker = NiftiMasker(mask_img='mask.nii.gz', standardize=True)
# Load fmri data and apply mask
fmri_data = masker.fit_transform('fmri_data.nii.gz')

# Create SVM classifier
svc = svm.SVC(kernel='linear')
# Fit classifier to data
svc.fit(fmri_data, behavioral.target)

# This is a very simplified example, but hopefully it gives an idea
# of how a general Python-based MVPA pipeline might look.
```

Note: All above examples are highly simplified and might not work on your specific problem out of the box. Pre-processing steps for MVPA often include spatial smoothing, time slice correction, alignment, normalization, bandpass filtering, and creation of a mask. 

As always when using third-party packages, please familiarize yourself with the specifics of each function and adjust parameters as needed.