Here are some basic scripts for network analysis in each of the requested brain imaging software:

**1. AFNI**

AFNI is primarily a tool for analyzing and visualizing functional brain imaging datasets. It doesn't have a specific network analysis command but it can preprocess data for network analysis. Here's an example of its usage:

```bash
# preprocessing - remove first 5 volumes
3dTcat -prefix r_func.nii.gz func.nii.gz'[5..$]'

# smooth the data
3dmerge -1blur_fwhm 4.0 -doall -prefix s_r_func.nii.gz r_func.nii.gz
```

**2. FSL**

FSL also doesn't provide direct network analysis, but you can use the "probtrackx2" tool to track fiber pathways:

```bash
# Probabilistic tractography
probtrackx2 --samples=BedpostX/merged --mask=BedpostX/nodif_brain_mask --seed=my_roi --stop=my_roi --out=My_Tracts
```

**3. FreeSurfer**

Brain network analysis is currently not directly available with FreeSurfer. However, you can leverage FreeSurfer for preprocessing.

**4. ANTs**

ANTs does not have a single script for doing network analysis, it's a toolbox for performing advanced image registration.

**5. MRtrix**

MRtrix also offers more specific functionalities like fiber tractography:

```bash
# Generate 5TT image
5ttgen fsl T1.mif 5TT.mif

# Generate response file
dwi2response tournier dwi.mif response.txt

# Perform CSD
dwi2fod csd dwi.mif response.txt FOD.mif

# Perform tractography
tckgen FOD.mif 100M.tck -act 5TT.mif -backtrack -crop_at_gmwmi -seed_dynamic FOD.mif -maxlength 250
```

**6. Python SPM (Nilearn, nipy, nibabel)**

Python doesn't have a direct equivalent to SPM, but libraries like scipy, nilearn can be used for similar analysis:

```python
# Import libraries
from nilearn import datasets, input_data, connectome

# Load a 5 subject subset
adhd_dataset = datasets.fetch_adhd(n_subjects=5)

# Extract signals on a parcellation defined by labels
masker = input_data.NiftiLabelsMasker(labels_img='Power.nii.gz', standardize=True,
                                       memory='nilearn_cache', verbose=5)

# Calculate correlation matrices
correlation_measure = connectome.ConnectivityMeasure(kind='correlation')
correlation_matrices = correlation_measure.fit_transform([masker.transform(subject) 
                                                         for subject in adhd_dataset.func])
```

Please note that all brain imaging software support an extensive range of functionality and the code provided here merely touches the surface of what these software provide.