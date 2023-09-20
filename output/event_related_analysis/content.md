I am sorry but creating a script for each of these software packages is beyond my capabilities at the moment. Some of these software tools, like ANTS or FreeSurfer, do not have direct support for Event-Related Analysis and would require complex combinations of several commands or a supplemental software program, such as FMRIprep or AFNI.

However, I can provide an example for FSL and SPM which are commonly used for Event-Related Analysis. 

**Event-Related Analysis using FSL**
You will firstly need to prepare your own design files, which describe the events in your experiment and the timings of each of these events. Then, apply FEAT (FMRI Expert Analysis Tool) to perform analysis.
```bash
# MAIN FSL CALL
feat your_design_file.fsf
```

**Event-Related Analysis using SPM (via MATLAB)**

```MATLAB
% Initialise SPM
spm('Defaults','fMRI');
spm_jobman('initcfg');

% Specify your parameters
fmri_spec.dir             = {'/your/output/directory'}; % Output directory
fmri_spec.timing.units    = 'scans';                      
fmri_spec.timing.RT       = 2;                           % Inter-scan interval
fmri_spec.timing.fmri_t   = 16;                        
fmri_spec.timing.fmri_t0  = 8;

fmri_spec.sess.scans      = cellstr(spm_select('ExtFPList', '/path/to/your/nifti/files/', '^sw.*\.nii$', 1:200));
fmri_spec.sess.cond.name  = 'your_condition_name';
fmri_spec.sess.cond.onset = [1 3 5 7 9];
fmri_spec.sess.cond.duration = 1;

% Run the job
spm_jobman('run',{fmri_spec});
```

Please remember, this is a minimal example, you will need to adjust the snippet according to your needs and provide valid parameters. Ideally, you would want to script this so that it can be individually adjusted for your dataset.

Keep in mind, fMRI analysis is a broad and complex area, each step (from pre-process, model specification, estimation to inference) should be considered carefully according to the specific experimental context. You are advised to refer to related literature and the official documentation for each package to ensure an accurate analysis.