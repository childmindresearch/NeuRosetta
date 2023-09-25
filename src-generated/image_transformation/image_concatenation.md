Sure, for each of these software, here's a minimal example of image concatenation:

AFNI

```bash
3dTcat -prefix concatenated.nii input1.nii input2.nii
```

ANTs

```bash
ImageMath 3 concatenated.nii m input1.nii input2.nii
```

FSL

```bash
fslmerge -t concatenated.nii input1.nii input2.nii
```

FreeSurfer

FreeSurfer does not directly support image concatenation. However, you can use mris_convert to transform surfaces into volumetric format, then use FSL or AFNI to concatenate.

MRtrix

```bash
mrcat input1.nii input2.nii concatenated.nii -axis 3
```

R

```R
library(oro.nifti)
nii1 = readNIfTI("input1.nii", reorient=FALSE)
nii2 = readNIfTI("input2.nii", reorient=FALSE)
nii_concat = abind(nii1, nii2)
writeNIfTI(nii_concat, "concatenated.nii")
```

Workbench Command (HCP)

Workbench's wb_command tool doesn't natively support 3D NIFTI concatenation you'll likely need to use another tool (like FSL, ANTs, or AFNI) to do the concatenation.

Python

```python
import nibabel as nib
nii1 = nib.load('input1.nii')
nii2 = nib.load('input2.nii')
nii_concat = nib.concat_images([nii1, nii2])
nib.save(nii_concat, 'concatenated.nii')
```

SPM(MATLAB)

```matlab
V1 = spm_vol('input1.nii');
V2 = spm_vol('input2.nii');
V_concat = cat(1, V1, V2);
V_concat.fname = 'concatenated.nii';
spm_write_vol(V_concat, spm_read_vols(V_concat));
```