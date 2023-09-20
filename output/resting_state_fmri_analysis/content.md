Apologies for the misunderstanding, but as a text-based assistant, I can't show scripts directly. However, I can guide you on how to process your Resting-State fMRI (rsfMRI) data using these neuroimaging software packages. Here is a simple guide:

1. AFNI:

```bash
3dDespike -prefix rMPRAGE_despike.nii -NEW rMPRAGE.nii
3dTshift -prefix rMPRAGE_ts.nii -TR 2.5 -tpattern altplus -Fourier rMPRAGE_despike.nii
3dDetrend -prefix rMPRAGE_detrend.nii -polort 5 rMPRAGE_ts.nii
3dBandpass -prefix rMPRAGE_bp.nii -dt 2.5 -band 0.01 0.1 rMPRAGE_detrend.nii
```

2. ANTs:

ANTs doesn't have a dedicated rsfMRI tool. Instead, it is usually used in combination with other tools like AFNI or FSL for better brain extraction, tissue segmentation or registration.

3. FSL:

```bash
fslmaths func.nii.gz -Tmean mean_func.nii.gz
fslmaths func.nii.gz -bptf 25 -1 -add mean_func.nii.gz filtered_func.nii.gz
```

4. FreeSurfer:

FreeSurfer is more used for structural image processing rather than rsfMRI. However, you can use it to obtain surface or volume-based measurements useful for further rsfMRI analysis in other software.

5. MRtrix:

MRtrix doesn't natively support rsfMRI processing. It's designed for diffusion images.

6. SPM (MATLAB-based, not Python)

```matlab
matlabbatch{1}.spm.temporal.st.nslices = 31;
matlabbatch{1}.spm.temporal.st.tr = 2;
matlabbatch{1}.spm.temporal.st.ta = 1.93548387096774;
matlabbatch{1}.spm.temporal.st.so = [1:31];
matlabbatch{1}.spm.temporal.st.refslice = 16;
matlabbatch{1}.spm.temporal.st.v0 = 0;
```

For Python-based analysis you can use tools like "nilearn" or "nipype".

Note: This represents bare-minimum examples, resting-state fMRI preprocessing involves several other steps and considerations depending on the data and experimental design. In general, the pipeline includes steps like Slice-Timing Correction, Motion Correction, Coregistration to structural image, Spatial Normalization, Smoothing, Temporal Filtering, and nuisance regression (motion parameters, WM/CSF signals).