While I can provide sample code snippets, keep in mind that brain imaging analysis is complex and requires a deep understanding of the underlying analysis tools as well as the specific datasets. Always consult credible and trustworthy documentation or consult an expert when working with these algorithms.

1. AFNI:

```
# ALFF in AFNI
3dFourier -highpass 0.01 -lowpass 0.08 -prefix REST_filtered.nii REST.nii
3dcalc -a REST_filtered.nii -expr 'sqr(a)' -prefix REST_filtered_sqr.nii
3dFourier -retrend -lowpass 0.08 -prefix REST_filtered_sqr_ALFF.nii REST_filtered_sqr.nii
```

2. ANTs:

ANTs itself does not provide an ALFF calculation functionality.

3. FSL:

```
# ALFF in FSL
fslmaths REST -Tmean mean_REST
fslmaths REST -bptf 33.33 -1 -add mean_REST filtered_REST
fslmaths filtered_REST -sqr filtered_REST_sqr
fslmaths filtered_REST_sqr -bptf 33.33 -1 ALFF_REST
```

4. FreeSurfer:

FreeSurfer does not directly support ALFF calculation.

5. MRtrix:

MRtrix does not directly support ALFF calculation.

6. Using R:

R does not directly support ALFF calculation, but packages such as 'neuRosim' can be used to stimulate brain imaging data.

7. Workbench Command:

The Workbench Command does not directly support ALFF calculation.

8. Pure Python:

```
# ALFF in Python
import numpy as np
from nilearn import image

tseries_img = image.load_img('rest.nii.gz')
tseries = image.img_to_array(tseries_img)
tseries = np.square(tseries)
tseries_img = image.new_img_like(tseries_img, tseries)
tseries_img = image.math_img("img * np.sin(0.01*np.pi*2) * np.sin(0.08*np.pi*2)", img=tseries_img)
tseries_img.to_filename('alff.nii.gz')
```

9. SPM (via a MATLAB script):

```
% ALFF in SPM
matlabbatch{1}.spm.tools.alff.inputdata = {'/path/to/functional/data.nii'};
matlabbatch{1}.spm.tools.alff.bandlow = 0.01;
matlabbatch{1}.spm.tools.alff.bandhigh = 0.08;
matlabbatch{1}.spm.tools.alff.brainmask = {'/path/to/masked/brain.nii'};
matlabbatch{1}.spm.tools.alff.nonbrainmask = {''};
spm('defaults', 'PET');
spm_jobman('run', matlabbatch);
```

Please note: These code snippets should only be used as a rough guide and may require heavy modification for any real use case.