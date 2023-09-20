Sure, here's a minimal script to perform spatial smoothing with AFNI.

```bash
#!/bin/bash

# specify the input and output filenames
input_file="RestingState.nii"
output_file="RestingState_Smooth.nii"

# Set the smoothing kernel size in mm
FWHM=5

# Run 3dBlurToFWHM to perform the smoothing
3dBlurToFWHM -FWHM $FWHM -input $input_file -prefix $output_file
```

Please make sure to replace `"RestingState.nii"` and `"RestingState_Smooth.nii"` with your actual nifti file names. The `FWHM=5` is the full-width-half-max of the Gaussian blur kernel (set it to what you want). This script assumes that you have AFNI correctly installed and available in your command line environment.