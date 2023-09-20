Here are the sample example scripts for each of the requested image processing tools. 

Note: In these examples, 'fixedImage.nii' and 'movingImage.nii' are placeholders for your actual filenames.

1. **AFNI**

```shell
3dAllineate -base fixedImage.nii -input movingImage.nii -prefix registered.nii -1Dfile out.1D
```
2. **ANTs**

```shell
antsRegistration --dimensionality 3 --float 0 --output [registered, warp.nii, inverseWarp.nii] --interpolation Linear --use-histogram-matching 0 --initial-moving-transform [fixedImage.nii, movingImage.nii, 1] --transform Rigid[0.1]
```
3. **FSL**

```shell
flirt -in movingImage.nii -ref fixedImage.nii -out registered.nii -omat out.mat
```
4. **FreeSurfer**

```shell
bbregister --s <subject_id> --mov movingImage.nii --init-fsl --bold --out registered.dat
```
5. **MRtrix**

```shell
mrregister fixedImage.nii movingImage.nii -type rigid -rigid_transform out.txt -nl_warp outNLWarp.nii
```
6. **SPM in Python (using nipype lib)**

```python
from nipype.interfaces.spm import NewSegment, Coregister
coreg = Coregister()
coreg.inputs.target = 'fixedImage.nii'
coreg.inputs.source = 'movingImage.nii'
res = coreg.run()
```
This SPM example utilises the 'nipype' interface for SPM in python as SPM doesn't directly support python. Please modity the placeholders `<subject_id>`, `fixedImage.nii`, `movingImage.nii` to your needs.
