[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/image_transformation/non_linear_spatial_transformation.md)
# Non-linear Spatial Transformation

While I can provide high-level pseudo code snippets for some of the platforms mentioned, it's essential to understand that some tools may not support non-linear spatial transformations directly (like R, Workbench Command, and pure Python). Here are examples of using each tool:

## <img src="../icons/afni.png" height="24px" /> AFNI

```
3dQwarp -source subject.nii -base template.nii -prefix warped_subject.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs

```
antsRegistration -d 3 -r [ template.nii, subject.nii, 1 ] \
-m mattes[ template.nii, subject.nii, 1, 32, regular, 0.1 ] \
-t syn[0.1,3,0] -c [50x20x5,1e-6,10] -s 4x2x1vox -f 6x4x2 -l 1 \
-o [subject_to_template_,warped_subject.nii]
```

## <img src="../icons/fsl.png" height="24px" /> FSL

```bash
fnirt --in=subject --aff=sub_to_temp.mat --cout=nonlinear_trans --iout=warped_subject --jout=jac --config=T1_2_MNI152_2mm  --ref=MNI152_T1_2mm --refmask=MNI152_T1_2mm_brain_mask_dil --warpres=10,10,10
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
mri_robust_register --mov subject.nii.gz --dst template.nii.gz --mapmov registered.nii.gz --cost mi
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

MRtrix3 does not perform non-linear registration in isolation. It does, however, allow interfacing with ANTS registration. For direct MRtrix-based image registration, only linear transformations are currently supported. 

## <img src="../icons/r.png" height="24px" /> R

R does not support non-linear spatial transformations by itself. However, ANTsR (https://github.com/stnava/ANTsR) interface can be used.

```R
library(ANTsR)
fixedImage <- antsImageRead( template.nii.gz , 3 )
movingImage <- antsImageRead( T1.nii.gz , 3 )
mytx <- antsRegistration( fixedImage, movingImage , 'SyN' )
warpedImage <- antsApplyTransforms( fixedImage, movingImage, mytx$forwardTransforms )
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

Workbench commands primarily operate on surface-based data. Non-linear volume registration can be performed using other software packages such as FSL, ANTs, or AFNI.

## <img src="../icons/python.png" height="24px" /> Python

Similar to R, pure Python requires interfaces to other software systems to perform non-linear registration. Following is an example with Nipype module which interfaces with ANTs:

```python
from nipype.interfaces.ants import Registration
reg = Registration()
reg.inputs.fixed_image = 'fixed1.nii'
reg.inputs.moving_image = 'moving1.nii'
reg.inputs.transforms = ['SyN']
reg.inputs.transform_parameters = [(0.25, 3.0, 0.0)]
reg.inputs.number_of_iterations = [[100, 50, 20]]
reg.inputs.dimension = 3
reg.inputs.write_composite_transform = True
reg.inputs.output_transform_prefix = 'output_'
reg.inputs.initialize_transforms_per_stage = False
reg.cmdline
reg.run()
```

## <img src="../icons/spm.png" height="24px" /> SPM

```matlab
matlabbatch{1}.spm.spatial.normalise.estwrite.subj.vol = {'subject.nii,1'};
matlabbatch{1}.spm.spatial.normalise.estwrite.subj.resample = {'subject.nii,1'};
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.biasreg = 0.0001;
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.biasfwhm = 60;
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.tpm = {'TPM.nii,1'};
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.affreg = 'mni';
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.reg = [0 0.001 0.5 0.05 0.2];
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.fwhm = 0;
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.samp = 3;
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.bb = [-78 -112 -70
                                                              78 76 85];
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.vox = [2 2 2];
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.interp = 4;
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.prefix = 'w';
spm_jobman('run',matlabbatch);
```

These are generic pipeline codes and should be adjusted to your specific case concerning image dimension, registration type, interpolation method, etc. Please refer to the official documentation of the mentioned sotware packages for more details.