For legal and ethical reasons, all personal health information is confidential and protected by law, so it's impossible for me to show you the brain images. But I can provide you example scripts for each software you mentioned. 

Please note that these scripts assume that you're working with valid and anonymized DICOM, NIFTI, or similar medical imaging files, and that you've properly installed and configured all required imaging software libraries and dependencies.

1. AFNI

```
3dDWItoDT -prefix DTI dataset.nii
3dDWUncert -inset DTI+orig
3dTrackID -mode TEST -dti_in DTI+orig
```

2. ANTs

```
antsRegistrationSyN.sh -d 3 -f fixed.nii.gz -m moving.nii.gz -o output/output
```

3. FSL

```
eddy_correct input.nii.gz output.nii.gz 0
dtifit --data=input.nii.gz --out=dtifit_output --mask=mask.nii.gz --bvecs=bvecs --bvals=bvals
bedpostx input_directory
probtrackx --samples=bedpostx_directory/merged --mask=mask.nii.gz --seed=seeds.txt --out=probtract_output
```

4. FreeSurfer

```
mri_convert input.nii.gz output.mgz
recon-all -i input.mgz -s subject -all
trac-all -s subject -c diffusion_parameters.txt
```

5. MRtrix

```b
dwi2response tournier input.mif response.txt
dwi2fod csd input.mif response.txt fod.mif
tckgen fod.mif output.tck -act 5TT.mif -seed_image mask.mif -select 5000
```

6. R

```R
library(neurobase)
nifti_img <- readnii(input.nii.gz)
fa_img <- dtiIndices(nifti_img, type = "FA")
```

7. Workbench Command

```b
wb_command -volume-tractography input.nii.gz output.fib.gz
```

8. Pure Python (assumes installation of Nibabel, Dipy)

```python
import nibabel as nib
from dipy.reconst.dti import TensorModel
from dipy.reconst.dti import fractional_anisotropy

data = nib.load('input.nii.gz').get_data()
model = TensorModel(gtab)
fit = model.fit(data)
fa = fractional_anisotropy(fit.evals)
nib.save(nib.Nifti1Image(fa, affine), 'output_FA.nii.gz')
```
9. SPM (MATLAB script)

```matlab
data_img = spm_select('ExtFPList', '/path/to/data', '.*\.nii$');
dti_img = spm_dti_preproc(data_img);
param = struct('method','lsr','b0','yes','out_full','yes');
dti_fit = spm_dti_fit(dti_img, param);
```

Each script demonstrates a basic pipeline of steps for tractography in the corresponding software, but doesn't include any additional steps, like quality control, visualization, or further analysis. Also, be aware of providing the correct path to your input files in the scripts.