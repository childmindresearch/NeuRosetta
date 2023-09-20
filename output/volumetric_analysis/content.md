Sure, here are minimal examples for each of them:

1. **AFNI**
```bash
# AFNI Volumetric Analysis
3dcalc -a anat+orig -expr 'step(a)' -prefix anat_bin
3dBrickStat -mask anat_bin+orig -volume anat_bin+orig
```
2. **ANTs**
```bash
# ANTs Volumetric Analysis in Bash
ImageMath 3 volume.nii CountVoxels brainmask.nii
```
3. **FSL**
```bash
# FSL Volumetric Analysis
fslmaths input_image -bin output_image
fslstats output_image -V
```
4. **FreeSurfer**
```bash
# FreeSurfer Volumetric Analysis
mri_mask input.mgh mask.mgh output.mgh
mri_segstats --i output.mgh --seg brainmask.mgh --sum ./summary.stats
```
5. **MRtrix**
```bash
# MRtrix Volumetric Analysis
mrthreshold input.mif mask.mif
mrstats -mask mask.mif -output volume input.mif
```
6. **Python SPM**
```python
# pure PythonSPM Volumetric Analysis
from spm1d.stats import anova1
from spm1d.stats.anova import anova1rm
Y = np.random.randn(30,101)   #random 1D continuum data
A = np.array([0,1,2]*10)      #non-random group membership codes
B = np.array([0,1]*15)        #non-random group membership codes
SUBJ = np.array([0,1,2,3,4,5]*5)  #subject indicators
FF = np.vstack([Y,A,B,SUBJ]).T  
anova1(FF).inference(0.05).plot()  
```

Please adjust them as needed, this is just an illustrative code snippets. Be sure to replace `input_image`, `output_image`, etc. with your actual filenames, and remember that these are basic examples. Real-world usage usually involves much more complex pipelines and additional steps of preprocess and postprocess images.