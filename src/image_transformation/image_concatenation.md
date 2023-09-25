# Image Concatenation

for each of these software, here's a minimal example of image concatenation:

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
3dTcat -prefix concatenated.nii input1.nii input2.nii
```

## <img src="../../icons/ants.png" height="24px" /> ANTs

```bash
ImageMath 3 concatenated.nii m input1.nii input2.nii
```

## <img src="../../icons/fsl.png" height="24px" /> FSL

```bash
fslmerge -t concatenated.nii input1.nii input2.nii
```

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer

FreeSurfer does not directly support image concatenation. However, you can use mris_convert to transform surfaces into volumetric format, then use FSL or AFNI to concatenate.

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix

```bash
mrcat input1.nii input2.nii concatenated.nii -axis 3
```

## <img src="../../icons/r.png" height="24px" /> R

```R
library(oro.nifti)
nii1 = readNIfTI("input1.nii", reorient=FALSE)
nii2 = readNIfTI("input2.nii", reorient=FALSE)
nii_concat = abind(nii1, nii2)
writeNIfTI(nii_concat, "concatenated.nii")
```

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command

Workbench's wb_command tool doesn't natively support 3D NIFTI concatenation you'll likely need to use another tool (like FSL, ANTs, or AFNI) to do the concatenation.

## <img src="../../icons/python.png" height="24px" /> Python

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