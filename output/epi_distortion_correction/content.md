Sorry for misunderstanding, but it's impossible to create such scripts without defining and downloading specific data. However, I can give you an overview of how you would perform EPI Distortion Correction using these programs.

## AFNI
```bash
3dDWItoDT -echo_ed 1 dwi.nii.gz dwi_dt.nii.gz
3dSkullStrip -input dwi_dt.nii.gz -output brain.nii.gz
3dUnifize -input brain.nii.gz -output brain_unif.nii.gz
3dQwarp -plusminus -pmNAMES Rev_For -pblur 0.05 0.05 -blur -1 -1 \
-source brain_unif.nii.gz -base dwi_dt.nii.gz \
-prefix epi_unwarped.nii.gz
```
This script does a simple distortion correction using the 3dDWItoDT command.

## ANTs
```bash
antsApplyTransforms -d 3 -i distorted.nii.gz -r reference.nii.gz \
-o warped.nii.gz -n Linear -t [epi_reg_ANTs_0GenericAffine.mat, 1]
```
This script applies a transformation to a distorted image using a precomputed affine matrix.

## FSL
```bash
topup --imain=b0_b0rev --datain=acq_parameters.txt --config=b02b0.cnf --out=topup_results
applytopup --imain=dwi --inindex=1 --datain=acq_parameters.txt --topup=topup_results --out=dwi_corrected
```
In FSL, 'topup' computes the susceptibility-induced off-resonance field and 'applytopup' applies the field to correct the distortion.

## FreeSurfer
```bash
mri_nu_correct.mni --i orig.mgz --o nu.mgz
mri_normalize -g 1 nu.mgz norm.mgz
```
In FreeSurfer, `mri_nu_correct.mni` corrects intensity normalization and `mri_normalize` performs skull stripping.

## MRtrix
```bash
dwipreproc -rpe_pair -pe_dir AP dwi.mif dwi_corrected.mif -se_epi b0_pair.mif
```
In MRtrix, `dwipreproc` command performs EPI correction, using the `-rpe_pair` option to specify the reverse phase-encode pair.

## SPM (Matlab)
```matlab
matlabbatch{1}.spm.spatial.realign.estwrite.data = {'Distorted.nii,1'};
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.sep = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.which = [2 1];
spm_jobman('run', matlabbatch);
```
This matlab script uses the SPM function 'realign.estwrite' to correct the distortion.

Note: I'm using hypothetical filenames for the images, you'll need to replace these with the actual names of your images.