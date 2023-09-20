AFNI
```bash
# Load AFNI modules
module load afni

# Define your dataset
3dNetCorr -inset 'your_dataset' -ts_out

```

ANTs
```python
# Load ANTs
import ants

# Load your image
image = ants.image_read('your_dataset.nii.gz')

# Compute correlation
correlation_matrix = ants.image_similarity(image, image, metric_type='correlation')
```

FSL
```bash
# Load FSL
. ${FSLDIR}/etc/fslconf/fsl.sh

# Multivariate exploratory linear optimized decomposition into independent components
melodic -i 'your_dataset' -o 'output_directory' --nobet --bgthreshold=10 --mmthresh=0.5 --Oall
```

FreeSurfer
```bash
# Load FreeSurfer 
source $FREESURFER_HOME/SetUpFreeSurfer.sh

# Surface-based smoothing
mris_fwhm --s subjectname --hemi lh --smooth-only --i lh.thickness --fwhm 10 --o lh.thickness.fwhm10.mgh
```

MRtrix
```bash
# Load MRtrix
module load mrtrix

# Compute the fibre orientation distributions
dwi2fod csd dwi.mif response.txt FOD.mif -mask mask.mif
```

pure Python (Nilearn)
```python
# Load Nilearn
from nilearn import image, input_data, connectome

# Define your time series
time_series = image.load_img('your_dataset.nii.gz')

# Define your mask
masker = input_data.NiftiLabelsMasker('atlas.nii.gz')

# Extract time series
time_series = masker.fit_transform(time_series)

# Calculate correlation matrix
correlation_matrix = connectome.ConnectivityMeasure(kind='correlation')
correlation_matrix.fit_transform([time_series])
```

SPM
```matlab
% Load SPM
addpath /path/to/spm12;

% Specify data
data = spm_select('FPList', '/path/to/your/data', '^*\.nii$');

% Specify parameters
matlabbatch{1}.spm.stats.fmri_spec.sess.scans = cellstr(data);
matlabbatch{1}.spm.stats.fmri_spec.sess.cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});

% Estimate parameters
spm_jobman('run', matlabbatch);
```

Please substitute all occurrences of 'your_dataset', 'output_directory', 'atlas.nii.gz', '/path/to/your/data' and '/path/to/spm12' with actual paths to your data and software.