import openai
import os
import pathlib as pl
import re


openai.api_key = os.environ["OAI_API_KEY"]
openai.organization = os.environ["OAI_ORG"]

FRAMEWORKS = [
    "AFNI",
    "ANTs",
    "FSL",
    "FreeSurfer",
    "MRtrix",
    "pure Python"
    "SPM",
]

OPERATIONS = [
    # Image Preprocessing
    "Spatial Smoothing",
    "Motion Correction",
    "Slice Timing Correction",
    "Image Registration",
    "Intensity Normalization",
    "Skull Stripping",
    "Bias Field Correction",
    "Artifact Detection and Correction",
    "EPI Distortion Correction",
    
    # Image Transformation
    "Rigid Spatial Transformation",
    "Affine Spatial Transformation",
    "Non-linear Spatial Transformation",
    "Diffeomorphic Spatial Transformation",
    "Resampling",
    "Image Concatenation",
    "Image Coregistration",
    
    # Statistical Analysis
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
    
    # Structural Analysis
    "Cortical Surface Reconstruction",
    "Subcortical Structure Segmentation",
    "White Matter Tractography",
    "Volumetric Analysis",
    "Cortical Thickness Measurement",
    "Shape Analysis",
    "Lesion Detection and Analysis",
    
    # Diffusion MRI Analysis
    "Diffusion Tensor Imaging (DTI)",
    "Tractography",
    "Tractometry",
    "Fractional Anisotropy (FA) Mapping",
    "Mean Diffusivity (MD) Mapping",
    "Radial and Axial Diffusivity Mapping",
    "White Matter Fiber Bundle Analysis",
    
    # fMRI Analysis
    "Task-Based fMRI Analysis",
    "Resting-State fMRI Analysis",
    "Seed-Based Correlation",
    "Amplitude of Low-Frequency Fluctuations (ALFF)",
    "Regional Homogeneity (ReHo)",
    "Dynamic Functional Connectivity",
    "Brain Parcellation",
    
    # Visualization and Data Exploration
    "Volume Visualization",
    "Glass Brain Visualization",
    "Surface Visualization",
    
    # Quality Control
    "Image Quality Assessment",
    "Outlier Detection",
    "Motion Outlier Identification",
    
    # Data Format Conversion
    "DICOM to NIfTI Conversion",
    "DICOM to MINC Conversion",
    "MINC to NIfTI Conversion",
    "NIfTI to DICOM Conversion",
]

operation = OPERATIONS[0]
framework = FRAMEWORKS[0]

def get_prompt(operation):
    output = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
                {"role": "system", "content": "You are a helpful assistant in brain imaging."},
                {"role": "user", "content": f"Show a short minimal example script that does {operation} in each of {', '.join(enquote(i) for i in FRAMEWORKS)} with a heading for each of them. Do not include instructions about installing software or downloading data."},
            ]
    )
    return output

def fsafe(s):
    return re.sub(r"[^a-zA-Z0-9]+", "_", s)

def enquote(s):
    return f'"{s}"'

# save output to file
OUT_DIR = pl.Path("output")
OUT_DIR.mkdir(exist_ok=True)


for operation_idx, operation in enumerate(OPERATIONS):
    out_file = OUT_DIR / fsafe(operation).lower() / "content.md"
    out_file.parent.mkdir(exist_ok=True, parents=True)
    
    if not out_file.exists():
        print(f"Generating {operation}... ({operation_idx+1}/{len(OPERATIONS)})")
        output = get_prompt(operation)
        with open(out_file, "w") as f:
            f.write(output.choices[0].message.content)
    else:
        print(f"Skipping {operation}...")

    with open(out_file.parent / "operation.txt", "w") as f:
        f.write(operation)
