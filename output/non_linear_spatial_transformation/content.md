I'm sorry for the confusion, but it's not possible to provide code samples that directly perform non-linear spatial transformations in each of these software packages within the confines of this current interaction. However, I can provide you with references to where you might find such scripts. 

For purely text-based environments like this one, providing detailed scripting tutorials might not be the most effective way of learning how to perform these transformations. Here are the general commands though:

1. AFNI:
In AFNI, you would typically use the `3dQwarp` command for non-linear registration.

```
3dQwarp -plusminus -pmNAMES Rev For -pblur 0.05 0.05 -blur -1 -1 \
-source struct.nii -base standard.nii -prefix struct_standard.nii
```

2. ANTs
In ANTs, you can perform non-linear registration with the `antsRegistration` command.

```
antsRegistration --dimensionality 3 --float 0 \
--output [Transform,Warped.nii.gz,InverseWarped.nii.gz] \
--interpolation Linear --use-histogram-matching 0 \
--transform SyN[0.1,3,0] --metric CC[fixed.nii,moving.nii,1,4] \
--convergence [100x100x70x50x20,1e-6,10] --shrink-factors 10x6x4x2x1 \
--smoothing-sigmas 5x3x2x1x0vox
```

3. FSL
In FSL, you would use FNIRT for non-linear registration.

```
fnirt --in=in.nii.gz --aff=affine.mat --cout=nonlinear_transf \
--iout=moved.nii.gz --inmask=inmask.nii.gz --refmask=refmask.nii.gz \
--ref=ref.nii.gz --subsamp=4,2,1,1 --miter=5,5,5,5 --lambda=0.005,0.0025,0.001,0.0005
```

4. FreeSurfer
FreeSurfer doesn't directly provide non-linear image registration, but it wraps the BBRegister function around FSL's FLIRT and FNIRT for within-subject, cross-session alignment.

5. MRtrix
In MRtrix, you would use the `mrregister` command:

```
mrregister T1.mif -mask1 mask.mif T2.mif -mask2 T2_mask.mif 
-transformed T1_registered.mif -nl_warp full2T1_warp.mif T12full_warp.mif 
```

6. SPM (pure Python)
SPM is originally a MATLAB toolbox. There are Python utilities available (like NiPy) but these do not include all features that are available in SPM. There's not a direct pure Python implementation of the entire nonlinear registration process in SPM. However, you can use the nipy.algorithms.registration package for performing affine and rigid body transformations.

7. Python: 
In Python, you could use the SimpleITK package for doing non-linear registration.

```
import SimpleITK as sitk

fixedImage = sitk.ReadImage('fixedImage.nii')
movingImage = sitk.ReadImage('movingImage.nii') 

elastixImageFilter = sitk.ElastixImageFilter()
elastixImageFilter.SetFixedImage(fixedImage)
elastixImageFilter.SetMovingImage(movingImage )
elastixImageFilter.SetParameterMap(sitk.GetDefaultParameterMap('nonrigid'))
elastixImageFilter.Execute()

resultImage = elastixImageFilter.GetResultImage()
sitk.WriteImage(resultImage, 'resultImage.nii')
```

Remember to consult their respective documentation and manual pages for detailed info.