I am an AI and as such, I can't generate scripts that directly interact with software or run code. However, I can provide pseudo-codes representing the general approach for each of these environments. The following examples assume that you are familiar with the basic functionality of each tool.  

1. AFNI
```bash
# Load AFNI module
module load afni

# Check outliers
3dToutcount -automask -fraction -polort 5 -legendre dataset > outcount.1D
```

2. ANTs
```C++
// Load ANTs library
#include "ANTs/itkImage.h"
#include "ANTs/itkImageFileReader.h"
#include "ANTs/itkImageFileWriter.h"
#include "ANTs/itkImageRegionIterator.h"

// Read the image
auto reader = itk::ImageFileReader<Image>::New();
reader->SetFileName(inputImage);

// Iterate over the image and perform outlier detection
for(auto it = itk::ImageRegionIterator<Image>(reader->GetOutput()); !it.IsAtEnd(); ++it){
   // Implement your outlier detection here
}
```

3. FSL  
```bash
# Load FSL module
module load fsl

# Run outlier detection with FSL's fsl_motion_outliers script
fsl_motion_outliers -i dataset -o outliers -s movpar.txt
```
4. FreeSurfer
```bash
# Load FreeSurfer module
source $FREESURFER_HOME/SetUpFreeSurfer.sh

# Run outlier detection
mri_glmfit --y dataset.nii.gz --fsgd fsgd.mat --C contrasts/contrast1.mat --osgm  --out-mni-avg-outliers outliers
```
5. MRtrix
```bash
# Load MRtrix module
module load mrtrix

# Outlier detection using dwiquality
dwiquality dataset dwi_quality_report -nobet
```
6. pure PythonSpM(NiftiMasker and sklearn)
```python
# Import necessary libraries
from nilearn.input_data import NiftiMasker
from sklearn.covariance import EllipticEnvelope

# Load and mask the fMRI data
masker = NiftiMasker().fit()
fMRI_data = masker.transform('dataset.nii.gz')

# Perform outlier detection
detector = EllipticEnvelope(contamination=.1)  
outliers = detector.fit_predict(fMRI_data)
```
Note: These scripts may need to be modified for your specific use case and are not guaranteed to work out of the box, errors are possible due to environmental differences or newer versions of the software changing how commands are called. Always refer to the documentation for your specific version of software for the most accurate use.