"""
Run this once after installing dependencies to confirm everything
is installed correctly and record versions for reproducibility.
"""

import sys
import platform

def check_environment():
    print("=" * 50)
    print("ENVIRONMENT CHECK")
    print("=" * 50)

    print(f"\nPython version: {sys.version}")
    print(f"Platform: {platform.platform()}")

    # Core scientific stack
    import numpy as np
    import pandas as pd
    print(f"\nNumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")

    # PyTorch
    import torch
    import torchvision
    print(f"\nPyTorch version: {torch.__version__}")
    print(f"Torchvision version: {torchvision.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU device: {torch.cuda.get_device_name(0)}")
    else:
        print("Running on CPU (expected, given your hardware).")

    # CPU info
    print(f"\nCPU count (logical cores): {torch.get_num_threads()}")

    # Hugging Face Transformers
    import transformers
    print(f"\nTransformers version: {transformers.__version__}")

    # OpenCV
    import cv2
    print(f"OpenCV version: {cv2.__version__}")

    # scikit-learn
    import sklearn
    print(f"scikit-learn version: {sklearn.__version__}")

    # MLflow
    import mlflow
    print(f"MLflow version: {mlflow.__version__}")

    # matplotlib
    import matplotlib
    print(f"Matplotlib version: {matplotlib.__version__}")

    print("\n" + "=" * 50)
    print("If you see this line with no errors above, your")
    print("environment is set up correctly.")
    print("=" * 50)

if __name__ == "__main__":
    check_environment()