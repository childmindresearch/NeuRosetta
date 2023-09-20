### AFNI
```bash
3dAllineate -base base_image.nii -input input_image.nii -prefix out.nii -1Dfile out.aff12.1D -twopass -cost ls -zclip -fineblur 3 -source_automask
```

### ANTs
```bash
antsRegistration --dimensionality 3 --float 0 --output [out, warp.nii.gz] --interpolation Linear --use-histogram-matching 0 --initial-moving-transform [base_image.nii, input_image.nii, 1] --transform Rigid[0.1] --metric MI[base_image.nii,input_image.nii,1,32, Regular, 0.25] --convergence [1000x500x250x0,1e-8,12] --shrink-factors 8x4x2x1 --smoothing-sigmas 3x2x1x0vox
```

### FSL
```bash
flirt -in input_image.nii -ref base_image.nii -out out.nii -omat out.mat -cost corratio -dof 6 -searchrx -180 180 -searchry -180 180 -searchrz -180 180
```

### FreeSurfer
```bash
bbregister --s subject --mov input_image.nii --init-coreg --out registered.nii.gz --lta out.lta
```

### MRtrix
```bash
mrregister base_image.nii input_image.nii -type rigid -mask1 mask.nii -nl_warp out.nii warp.nii.gz
```

### SPM using pure Python
```python
from nipype.interfaces.spm import Normalize12

norm12 = Normalize12()
norm12.inputs.deformation_file = "y_t1.nii"
norm12.inputs.apply_to_files = 'functional.nii'
norm12.inputs.jobtype = 'write'
res = norm12.run() 
```

Please note that the above examples are simplified to illustrate rigid transformations in each tool. The exact commands and scripts may need to be adjusted based on your specific imaging data and the desired transformation parameters.
