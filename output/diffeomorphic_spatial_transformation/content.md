Unfortunately, as a text-based AI developed by OpenAI, I'm unable to run or visually represent scripts. However, I can provide examples of how scripts could look like in each of the software packages to perform Diffeomorphic Spatial Transformations. A diffeomorphic transformation is used in image processing for non-linear registration, particularly in medical imaging. Here are some basic examples:

1. AFNI
For AFNI, there's 3dQwarp which can perform Diffeomorphic transformation:
```bash
3dQwarp -plusminus -pmNAMES Rev For -pblur 0.05 0.05 -blur -1 -1 -source ${SOURCE} -base ${TARGET} -prefix ${OUTPUT}
```

2. ANTs
In Advanced Normalization Tools (ANTs), the script could look something like:
```bash
antsRegistrationSyN.sh -d 3 -f ${FIXED_IMAGE} -m ${MOVING_IMAGE} -o ${OUTPUT} -t s
```

3. FSL
FSL's FNIRT can be used for Diffeomorphic transformations.
```bash
fnirt --ref=${FIXED_IMAGE} --in=${MOVING_IMAGE} --iout=${OUTPUT}
```

4. FreeSurfer
FreeSurfer includes tools like mri_robust_register for such processes:
```bash
mri_robust_register --mov ${MOVING_IMAGE} --dst ${FIXED_IMAGE} --lta ${OUTPUT}
```

5. MRtrix
In MRtrix, you'd have to first get the transformation matrix using a tool like flirt and then apply the warp with warpconvert.
```bash
flirt -in ${MOVING_IMAGE} -ref ${FIXED_IMAGE} -out ${OUTPUT}
warpconvert transformation_matrix.mif output warp full5tt_warped.mif
```

6. Pure Python/SPM
To get a pure Python implementation or one in SPM, one would typically use Nipype, a Python package that provides a uniform interface to existing neuroimaging software. Here is a brief script of this command:
```python
from nipype.interfaces.spm import Normalize12

norm12 = Normalize12()
norm12.inputs.deformation_file = 'y_subj.nii'
norm12.inputs.apply_to_files = 'rc1sub*.nii'
norm12.run() 
```

Please replace all `${VARIABLES}` with the actual paths to your source/target data. Also, ensure you have the right permissions to access and modify the data. These examples deal with lower-level functions in these packages, so always verify the results carefully. If not sure how these commands work, it's best to consult the official documentation or forums for these tools.