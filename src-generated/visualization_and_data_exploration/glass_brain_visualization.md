Sorry, brain imaging software is typically specific to each tool, and some of the ones you mentioned have limited functionality for directly creating a 3D glass brain. This is a rather specialized task. However, I can show an example approach for some of them (Python, R, and MATLAB) and refer to the main steps in the others with links to their official documentation:

**1. In pure Python (using `nilearn`):**

This is a Python script that defines a function `plot_glass_brains` and draws glass brain figures from nii image files

```python
import matplotlib.pyplot as plt
from nilearn import plotting, datasets

def plot_glass_brains(nii_files):
    for filepath in nii_files:
        plotting.plot_glass_brain(filepath)

# then you can use the plot_glass_brains function to visualize your nii files
plot_glass_brains(['/path/to/nii/file1', '/path/to/nii/file2'])
```

**2. In R (using `RNifti` and `rgl`):**

An example script in R to read NIFTI files and create a 3D plot:

```R
library(RNifti)
library(rgl)

nii <- readNifti("path/to/your/nifti/file.nii.gz")

isosurface3d(nii, threshold = "auto", alpha = 0.8, smooth = TRUE, windowRect = c(0, 0, 600, 600))
```

**3. In MATLAB (using SPM):**

Below is MATLAB code to plot glass brain. However, it is important to note that SPM has limited functionality for glass brain view, and it might not achieve the desired output.

```MATLAB
spm fmri;
SPM = spm_select(1,'^SPM\.mat$','Select your SPM.mat');
spm_sections(xSPM, struct('swd','.', 'n', 1, 'title', ''));
```

Please refer to the complete documentation or carefully consult a neuroimaging expert to understand these brain imaging tools.
As for the other software, they do not typically exhibit built-in functions to draw a "Glass brain".

**4. AFNI** and **FSL** primarily work as command-line tools for analyzing time series voxel data - where the brain "Glass View" visualization isn't a default offering directly from these tools. Please refer to AFNI's user guide (https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/) and FSL's documentation (https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/).

**5. ANTs** primarily aims to analyze the deformation fields. They do not come with a glass brain viewer. ANTs documentation: https://stnava.github.io/ANTs/

**6. FreeSurfer** is slightly different, as it is primarily used for investigating cortical surface thickness and reconstruction, not for creating brain views like a glass brain. Here is the official place to get more information about this: https://surfer.nmr.mgh.harvard.edu/

**7. Workbench Command** is more suited to surface mapping and related visual analysis but doesn't intrinsically support a "glass brain" visualization. You can check out the full documentation here: 
https://www.humanconnectome.org/software/connectome-workbench

**8. MRtrix**: There are also no specific "glass brain" visualization capabilities in this software. Documentation: https://mrtrix.readthedocs.io/

For a feature like a glass brain visualization, a more generalized or dedicated neuroimaging visualization tool like `nilearn` (in Python), `fsleyes`, `papaya`, or `MRIcroGL` can be more suitable.