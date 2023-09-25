# EPI Distortion Correction

Here are example scripts for EPI distortion correction in the requested neuroimaging software packages. Please make sure to handle your data responsibly and follow the software's instructions for correct usage:

## <img src="../icons/afni.png" height="24px" /> AFNI

```bash
3dDWItoDT -prefix DWI_dt -mask Mask.nii -eigs yes DWI.nii
3dNwarpApply -nwarp 'warp.nii' -source 'original.nii' -prefix 'corrected.nii'
```

## <img src="../icons/ants.png" height="24px" /> ANTs

```bash
antsApplyTransforms -d 3 -i epi.nii -r anatomical.nii -t warp.nii -o corrected_epi.nii
```

## <img src="../icons/fsl.png" height="24px" /> FSL

```bash
fugue --loadfmap=fmap.nii --dwell=dwellt --saveshift=fshift.nii
applywarp --ref=struct.nii --in=fshift.nii --warp=epi2struct_warp.nii --out=corrected_epi.nii
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
mri_convert epi.nii epi.mgh
mri_normalize -g 1 -mprage epi.mgh corrected_epi.mgh
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

```bash
dwipreproc INPUT.nii OUTPUT.nii -rpe_none -pe_dir AP
```

## <img src="../icons/r.png" height="24px" /> R

This is a heuristic solution since R does not have brain imaging related packages:

```r
library(neurobase)
epi <- readnii("epi.nii")
warp <- readnii("warp.nii")
corrected_epi <- epi * warp
writenii(corrected_epi, "corrected_epi.nii")
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

This one mostly deals with surface models, not EPI distortion corrections:

```bash
wb_command -metric-resample epi.func.gii struct.surf.gii BARYCENTRIC corrected_epi.func.gii
```

## <img src="../icons/python.png" height="24px" /> Python

```python
from nipype.interfaces import fsl
fugue = fsl.FUGUE()
fugue.inputs.in_file = 'epi.nii'
fugue.inputs.warp_file = 'warp.nii'
fugue.inputs.save_shift = True
fugue.run()
```

## <img src="../icons/spm.png" height="24px" /> SPM

```matlab
matlabbatch{1}.spm.spatial.realign.estwrite.data = {'epi.nii,1'};
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.sep = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.fwhm = 5;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.which = [2 1];
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.interp = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.mask = 1;
spm_jobman('run', matlabbatch);
```

Please note that the scripts above only provide basic steps. Each individual script should be adjusted according to your own needs and specific workflows.