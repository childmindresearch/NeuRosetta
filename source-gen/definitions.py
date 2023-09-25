FRAMEWORKS = [
    "AFNI",
    "ANTs",
    "FSL",
    "FreeSurfer",
    "MRtrix",
    "pure Python",
    "SPM (via a MATLAB script)",
    "R",
    "Workbench Command",
]
FRAMEWORKS.sort()

OPERATIONS_DICT = {
    # Image Preprocessing
    "Image Preprocessing": [
        "Spatial Smoothing",
        "Motion Correction",
        "Slice Timing Correction",
        "Image Registration",
        "Intensity Normalization",
        "Skull Stripping",
        "Bias Field Correction",
        "Artifact Detection and Correction",
        "EPI Distortion Correction",
    ],
    
    # Image Transformation
    "Image Transformation": [
        "Rigid Spatial Transformation",
        "Affine Spatial Transformation",
        "Non-linear Spatial Transformation",
        "Diffeomorphic Spatial Transformation",
        "Resampling",
        "Image Concatenation",
        "Image Coregistration",
    ],
    
    # Statistical Analysis
    "Statistical Analysis": [
        "General Linear Model (GLM)",
        "Independent Component Analysis (ICA)",
        "Seed-Based Connectivity Analysis",
        "Region-of-Interest (ROI) Analysis",
        "Multivariate Pattern Analysis (MVPA)",
        "Event-Related Analysis",
        "Mixed-Effects Models",
        "Graph Theory Analysis",
        "Network Analysis",
        "Dynamic Connectivity Analysis",
        "Granger Causality Analysis",
        "Functional Connectivity Density Mapping",
    ],
    
    # Structural Analysis
    "Structural Analysis": [
        "Cortical Surface Reconstruction",
        "Subcortical Structure Segmentation",
        "White Matter Tractography",
        "Volumetric Analysis",
        "Cortical Thickness Measurement",
        "Shape Analysis",
        "Lesion Detection and Analysis",
    ],
    
    # Diffusion MRI Analysis
    "Diffusion MRI Analysis": [
        "Diffusion Tensor Imaging (DTI)",
        "Tractography",
        "Tractometry",
        "Fractional Anisotropy (FA) Mapping",
        "Mean Diffusivity (MD) Mapping",
        "Radial and Axial Diffusivity Mapping",
        "White Matter Fiber Bundle Analysis",
    ],
    
    # fMRI Analysis
    "fMRI Analysis": [
        "Task-Based fMRI Analysis",
        "Resting-State fMRI Analysis",
        "Seed-Based Correlation",
        "Amplitude of Low-Frequency Fluctuations (ALFF)",
        "Regional Homogeneity (ReHo)",
        "Dynamic Functional Connectivity",
        "Brain Parcellation",
    ],
    
    # Visualization and Data Exploration
    "Visualization and Data Exploration": [
        "Volume Visualization",
        "Glass Brain Visualization",
        "Surface Visualization",
    ],
    
    # Quality Control
    "Quality Control": [
        "Image Quality Assessment",
        "Outlier Detection",
        "Motion Outlier Identification",
    ],
    
    # Data Format Conversion
    "Data Format Conversion": [
        "DICOM to NIfTI Conversion",
        "DICOM to MINC Conversion",
        "MINC to NIfTI Conversion",
        "NIfTI to DICOM Conversion",
    ],
}

OPERATIONS = [x for y in OPERATIONS_DICT.values() for x in y]