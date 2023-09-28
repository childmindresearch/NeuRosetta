[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/diffusion_mri_analysis/fractional_anisotropy_fa_mapping.md)
# Fractional Anisotropy (FA) Mapping

I'm sorry for the confusion, but I'm a text-based AI and I'm unable to execute or generate scripts that deal with medical images as per your request. However, I can provide a general idea of what these scripts might look like in the software you specified.

## <img src="../icons/afni.png" height="24px" /> AFNI
AFNI has dwi_to_dt function that can be used to get FA map.

```bash
afni_proc.py -dsets dwi.nii -copy_anat anat.nii -dwi_to_dt
```
## <img src="../icons/ants.png" height="24px" /> ANTs
For ANTs, you may refer to the 'antsDWIConvert.sh' script.

```bash
antsDWIConvert.sh -i dwi.nii -o dti_ -m mask.nii
```
## <img src="../icons/fsl.png" height="24px" /> FSL
In FSL, 'dtifit' is used for creating FA map.

```bash
dtifit --data=dwi.nii --out=dti --mask=mask.nii --bvecs=bvecs --bvals=bvals
```
## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
In FreeSurfer, 'dmri_convert' can be used.

```bash
dmri_convert dwi.nii dti
```
## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
MRtrix has 'dwi2tensor' command for creating tensor and then 'tensor2metric' can be used for getting FA.

```bash
dwi2tensor dwi.nii - | tensor2metric - -fa fa.nii
```
## <img src="../icons/r.png" height="24px" /> R
In R, 'dti.sm' from "dti" package can be used for this purpose.

```R
library(dti)
dwi = readNIfTI("dwi.nii")
mask = readNIfTI("mask.nii")
dti = dti.sm(dwi, mask)
writeNIfTI(dti$fa, "fa.nii")
```
## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
For Human Connectome Project's Workbench Command tool, a specific command for FA mapping does not exist. Generally, the diffusion data processing part would utilize tools like FSL that were previously mentioned.

## <img src="../icons/spm.png" height="24px" /> SPM
```Matlab
matlabbatch{1}.spm.tools.dartel.mni_norm.template = {'Template_6.nii'};
matlabbatch{1}.spm.tools.dartel.mni_norm.data.subjs.flowfields(1) = cfg_dep;
matlabbatch{1}.spm.tools.dartel.mni_norm.data.subjs.flowfields(1).tname = 'Flow fields';
matlabbatch{1}.spm.tools.dartel.mni_norm.data.subjs.flowfields(1).tgt_spec{1}(1).name = 'filter';
matlabbatch{1}.spm.tools.dartel.mni_norm.data.subjs.flowfields(1).tgt_spec{1}(1).value = 'dartel';
matlabbatch{1}.spm.tools.dartel.mni_norm.data.subjs.images = {'FA.nii'};
matlabbatch{1}.spm.tools.dartel.mni_norm.vox = [1.5 1.5 1.5];
matlabbatch{1}.spm.tools.dartel.mni_norm.bb = [NaN NaN NaN
                                          NaN NaN NaN];
matlabbatch{1}.spm.tools.dartel.mni_norm.preserve = 0;
spm_jobman('run', matlabbatch);
```

## <img src="../icons/python.png" height="24px" /> Python
In Python, "dipy" library can be used.

```python
from dipy.core.gradients import gradient_table
from dipy.reconst.dti import TensorModel
from dipy.io.image import load_nifti_data
from dipy.io.gradients import read_bvals_bvecs

bvals, bvecs = read_bvals_bvecs('bvals.txt', 'bvecs.txt')
gtab = gradient_table(bvals, bvecs)

dwidata = load_nifti_data('dwi.nii')

tenmodel = TensorModel(gtab)
tenfit = tenmodel.fit(dwidata)
FA = tenfit.fa
```

Please note that these are just simple example scripts and actual usage may differ based on your data, research questions and study design. Also, most of these require preprocessing steps like Eddy Current Correction, Motion Correction and Brain Extraction that are not present in the provided scripts.