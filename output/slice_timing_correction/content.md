Sure, here are some minimal examples using each software package. Please note that these are very basic examples and potentially not tuned for your specific requirements. You might need to mention your absolute input and output file paths instead of placeholders (`<...>`).

### 1. AFNI
```bash
3dTshift -prefix <output_file> -tpattern altplus <input_file>
```

### 2. ANTs
ANTs doesn't have a built-in function specifically for slice timing correction but it can be done using a combination of other tools.

### 3. FSL
```bash
slicetimer -i <input_file> -o <output_file> -r <repetition_time_in_seconds> --odd
```

### 4. FreeSurfer
FreeSurfer doesn't have a tool specifically for slice time correction.

### 5. MRtrix
MRtrix doesn't have an explicit tool for slice timing correction. 

### 6. SPM (in Matlab)
```matlab
matlabbatch{1}.spm.temporal.st.scans{1} = '<input_file>';
matlabbatch{1}.spm.temporal.st.nslices = <number_of_slices>;
matlabbatch{1}.spm.temporal.st.tr = <repetition_time_in_seconds>;
matlabbatch{1}.spm.temporal.st.ta = <repetition_time_in_seconds> - (<repetition_time_in_seconds>/<number_of_slices>);
matlabbatch{1}.spm.temporal.st.so = [1:<number_of_slices>];
matlabbatch{1}.spm.temporal.st.refslice = 1;
matlabbatch{1}.spm.temporal.st.prefix = 'a';
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```

### 7. Pure Python
For pure Python implementations, `nipy` library can be used.
```python
import nipy.algorithms.slicetiming as slicetiming
from nipy.modalities.fmri import design_matrix
import nipy.algorithms.resampling as rs

slice_order = list(range(1, <number_of_slices> + 1))
tr = <repetition_time_in_seconds>
resampler = slicetiming.TimeSliceResampler(slice_order, tr)

in_file = '<input_file>'
img = nipy.load_image(in_file)
resampled_img = resampler.resample(img)

out_file = '<output_file>'
nipy.save_image(resampled_img, out_file)
```

Please note that these code snippets must be customized to your specific use case, and they all assume you have already installed the relevant packages and have imported any necessary dependencies. For Python code, you also need to replace `<input_file>`, `<output_file>`, `<number_of_slices>` and `<repetition_time_in_seconds>` with the actual reference. For shell commands, replace these placeholders including the angle brackets.