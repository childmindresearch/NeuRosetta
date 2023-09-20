I'm sorry for the confusion, but writing scripts for all mentioned software packages would be extensive. Instead, I'll illustrate simplified examples for a couple of those packages. However, please take note that these scripts may not run 'as-is' and could need adjustments according to your data and specific use case.

1. FSL (FMRIB Software Library)
   ```bash
   # ReHo analysis is not directly supported in FSL. However, you can use FSL tools for some steps.
   # fslmaths is used for spatial smoothing. You may need additional scripts or software for a complete ReHo analysis.
   
   fslmaths input -kernel gauss 2.35482 -fmean output_smoothed
   ```

2. Pure Python with NiBabel and sklearn (doesn't support ReHo directly, but these libraries can handle neuroimaging data)
    ```python
    import numpy as np
    from skimage.measure import label
    from nibabel import load, save, Nifti1Image
    from sklearn.metrics import pairwise_distances
    
    # Load a nifti file
    img = load('input.nii.gz')
    data = img.get_fdata()

    # Define neighborhoods
    neighborhood = np.ones((3, 3, 3))
    labels = label(data, neighborhood)

    # Compute the regional homogeneity
    regional_homogeneity = np.zeros_like(data)
    for region in np.unique(labels):
        if region == 0:
            continue
        regional_indices = np.where(labels == region)
        regional_data = data[regional_indices]
        regional_homogeneity[regional_indices] = 1 - pairwise_distances(regional_data).mean()

   # Save the output
   img_to_save = Nifti1Image(regional_homogeneity, img.affine, img.header)
   save(img_to_save, 'output.nii.gz')
   ```

Please note that due to different emphasis and objectives of each of these software tools, not every one of them can perform ReHo analysis directly. For instance, AFNI doesn't directly support ReHo but it has a 3dReHo script to calculate the KCC-ReHo. ANTs, FreeSurfer, and MRtrix3 do not directly have ReHo analysis as per my knowledge.

When dealing with a specific type of analysis like Regional Homogeneity (ReHo), tools like REST (Resting-State fMRI Data Analysis Toolkit) or DPABI, which are more targeted towards resting-state data analysis, might be more appropriate than general-purpose neuroimaging software.