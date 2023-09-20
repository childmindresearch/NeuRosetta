The toolkits you mentioned offer complex functionalities and their usage can vary based on the user-end requirements. Here are some minimal examples for brain visualization in Python-friendly environments. However, just to note, MRtrix and FreeSurfer don't have an explicit "glass brain" functionality, but they can certainly visualize brain images. Following scripts assume that you have preprocessed brain image data ready to be fed.

1. AFNI (Python's afni-python module)

```python
from afni_python import afni_util as au
import matplotlib.pyplot as plt

# Where 'brain.nii' is your brain image file name
dset = au.read_anat('brain.nii')

# Display a middle axial slice
plt.imshow(dset.anat[..., dset.anat.shape[2]//2], cmap='gray')

# Then use your strategy to achieve "glass brain" view
```

2. ANTs (Python's ANTsPy module)

```python
import ants

# Where 'brain.nii.gz' is your brain image file name
img = ants.image_read('brain.nii.gz')

# Visualize
ants.plot(img)
```

3. FSL (Python's nilearn module)

```python
from nilearn import datasets, plotting

# where 'example.nii' is your image
img='example.nii'

plotting.plot_glass_brain(img, colorbar=True)
plotting.show()
```

4. FreeSurfer (Python's nibabel and nilearn modules)

```python
import nibabel as nib
from nilearn import plotting

# Where 'brain.mgz' is your brain image file name
brain_img = nib.load('brain.mgz')
plotting.plot_glass_brain(brain_img, threshold=3))
plotting.show()
```

5. MRtrix (Python's MRtrix3 module)

```python
import mrtrix3

# Where 'dwi.mif' is your brain image file name
img = mrtrix3.image.open('dwi.mif')

# Display image
print(img)
```

6. PythonSPM (Python's nilearn module)

```python
from nilearn import datasets, plotting

# Where 'spmT_0001.nii' is the SPM statistical map
img='spmT_0001.nii'

# Visualize
plotting.plot_glass_brain(img, threshold=0)
plotting.show()
```
Remember, these are directly for reading and visualizing, not full solutions to getting a glass brain visual from raw MRI data. Plus, apart from ANTsPy, nilearn, nibabel and MRtrix3 for Python aren't directly linked to the command-line tools (AFNI, ANTs, FSL, FreeSurfer, MRtrix). So, the script doesn't signify using those tools directly but their corresponding Python libraries.