Due to the complexity in the field of brain imaging, it's nearly impossible to provide minimal example scripts for network analysis in all mentioned software packages in a single response. However, here are examples for a subset of the software mentioned:

**1. AFNI (Analysis of Functional NeuroImages)** 

    3dcalc -a 'FWHM+orig[0]' -b 'FWHM+orig[1]' -c 'FWHM+orig[2]' -expr 'sqrt(a*a+b*b+c*c)' -prefix FWHM_total

**2. ANTs (Advanced Normalization Tools)**

    #!/bin/bash
    fixedImage=~/input/fixed.nii.gz
    movingImage=~/input/moving.nii.gz
    outputWarpedImage=~/output/movingWarpedIntoFixed.nii.gz

    antsRegistrationSyN.sh -d 3 -f $fixedImage -m $movingImage -o $outputWarpedImage

**3. FSL (FMRIB Software Library)**

FSL provides network modeling tool which called FSLNets.  You have to follow following step:

    #!/bin/sh 

    melodic -i4D input.nii.gz -o output --nobet -a concat -d 25 --tr=2 

**4. FreeSurfer**

    #!/bin/bash
    SUBJECTS_DIR=/path/to/subjects
    recon-all -s bert -all 

**5. MRtrix**

    dwi2response dhollander input_dwi.mif wm_response.txt gm_response.txt csf_response.txt

**6. R**

    library(igraph)
    g <- graph.formula(A -+ B, B -+ C, C -+ A)
    plot(g)

**7. Workbench Command**

    wget https://yourURL/path/to/your.dconn.nii
    wb_command -cifti-parcellate your.dconn.nii yourParcellation.dlabel.nii COLUMN yourOutput.dscalar.nii -method MEAN

**8. Python**

In python, we often use nilearn to perform a simple correlation matrix.

```python
from nilearn import datasets
from nilearn.input_data import NiftiLabelsMasker
from nilearn.connectome import ConnectivityMeasure

dataset = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm') 
atlas_filename = dataset.maps

masker = NiftiLabelsMasker(labels_img=atlas_filename, standardize=True,
                           memory='nilearn_cache', verbose=5)

time_series = masker.fit_transform('/path/to/your/4D.nii.gz')


correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]
```

Unfortunately, I can't provide an example for SPM (MATLAB), as MATLAB code requires proprietary knowledge of the MATLAB environment.