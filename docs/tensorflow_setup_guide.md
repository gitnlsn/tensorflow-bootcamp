# TensorFlow Setup Guide

## Overview
This guide provides comprehensive instructions for setting up TensorFlow in your development environment, including troubleshooting common issues.

## System Requirements

### Minimum Requirements
- Python 3.8-3.11 (TensorFlow 2.15+ supports Python 3.9-3.11)
- pip 19.0 or later
- 64-bit system
- At least 4GB RAM (8GB+ recommended)

### GPU Support (Optional)
- NVIDIA GPU with CUDA Compute Capability 3.5 or higher
- CUDA 11.8 (for TensorFlow 2.12+)
- cuDNN 8.6

## Installation Methods

### Method 1: Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv tfdeeplearning

# Activate virtual environment
# On Linux/Mac:
source tfdeeplearning/bin/activate
# On Windows:
tfdeeplearning\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install TensorFlow
pip install tensorflow

# Install additional packages
pip install numpy matplotlib jupyter pandas scikit-learn
```

### Method 2: Using Conda

```bash
# Create conda environment
conda create -n tfdeeplearning python=3.10

# Activate environment
conda activate tfdeeplearning

# Install TensorFlow
conda install tensorflow

# Install additional packages
conda install numpy matplotlib jupyter pandas scikit-learn
```

### Method 3: GPU Support Installation

```bash
# For NVIDIA GPU support
pip install tensorflow[and-cuda]

# Or install CUDA and cuDNN separately, then:
pip install tensorflow-gpu
```

## Verification

Run the installation test script:
```bash
python src/installation-testing.py
```

Expected output should include:
- TensorFlow version information
- Basic tensor operations
- Device information (CPU/GPU)
- Simple neural network test
- Success message

## Common Issues and Solutions

### Issue 1: AttributeError: module 'tensorflow' has no attribute 'Session'

**Problem**: Using TensorFlow 1.x syntax with TensorFlow 2.x

**Solution**: 
- TensorFlow 2.x uses eager execution by default
- Replace `tf.Session()` with direct tensor operations
- Use `tensor.numpy()` to get values instead of `sess.run()`

**Example Fix**:
```python
# TensorFlow 1.x (deprecated)
sess = tf.Session()
result = sess.run(tensor)

# TensorFlow 2.x (correct)
result = tensor.numpy()
```

### Issue 2: CUDA/GPU Warnings

**Symptoms**:
- "Could not find cuda drivers on your machine"
- "Unable to register cuFFT/cuDNN/cuBLAS factory"

**Solutions**:
1. **For CPU-only usage**: These warnings are normal and can be ignored
2. **For GPU usage**: 
   - Install NVIDIA drivers
   - Install CUDA toolkit
   - Install cuDNN
   - Verify with `nvidia-smi`

### Issue 3: Import Errors

**Problem**: `ModuleNotFoundError: No module named 'tensorflow'`

**Solutions**:
1. Ensure virtual environment is activated
2. Install TensorFlow in the correct environment
3. Check Python path: `which python` and `which pip`

### Issue 4: Version Compatibility

**Problem**: Package version conflicts

**Solutions**:
1. Create fresh virtual environment
2. Use specific TensorFlow version: `pip install tensorflow==2.15.0`
3. Check compatibility matrix on TensorFlow website

### Issue 5: Memory Issues

**Symptoms**: 
- Out of memory errors
- System freezing during training

**Solutions**:
1. Reduce batch size
2. Use gradient accumulation
3. Enable memory growth for GPU:
```python
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)
```

## Environment Variables

### Useful TensorFlow Environment Variables

```bash
# Disable oneDNN optimizations (if causing issues)
export TF_ENABLE_ONEDNN_OPTS=0

# Set CUDA visible devices
export CUDA_VISIBLE_DEVICES=0

# Enable/disable GPU memory growth
export TF_FORCE_GPU_ALLOW_GROWTH=true

# Set logging level
export TF_CPP_MIN_LOG_LEVEL=2  # 0=INFO, 1=WARN, 2=ERROR, 3=FATAL
```

## Performance Optimization

### CPU Optimization
```python
# Configure CPU threads
tf.config.threading.set_intra_op_parallelism_threads(4)
tf.config.threading.set_inter_op_parallelism_threads(4)
```

### GPU Optimization
```python
# Enable mixed precision
policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

# Configure GPU memory growth
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
```

## Development Environment Setup

### Jupyter Notebook Setup
```bash
# Install Jupyter
pip install jupyter

# Install TensorFlow kernel
python -m ipykernel install --user --name=tfdeeplearning

# Start Jupyter
jupyter notebook
```

### VS Code Setup
1. Install Python extension
2. Select correct Python interpreter (from virtual environment)
3. Install TensorFlow extension for better IntelliSense

## Testing Your Installation

### Quick Test
```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPU available:", len(tf.config.list_physical_devices('GPU')) > 0)
```

### Comprehensive Test
Run the provided `installation-testing.py` script which tests:
- Basic tensor operations
- Device availability
- Neural network creation
- Model compilation and prediction

## Troubleshooting Commands

```bash
# Check TensorFlow installation
python -c "import tensorflow as tf; print(tf.__version__)"

# Check available devices
python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"

# Check CUDA installation (if applicable)
nvidia-smi
nvcc --version

# Check Python environment
which python
pip list | grep tensorflow
```

## Additional Resources

- [TensorFlow Official Documentation](https://www.tensorflow.org/)
- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [CUDA Installation Guide](https://developer.nvidia.com/cuda-downloads)
- [cuDNN Installation Guide](https://developer.nvidia.com/cudnn)

## Support

If you encounter issues not covered in this guide:
1. Check the TensorFlow GitHub issues
2. Search Stack Overflow with relevant error messages
3. Consult the official TensorFlow documentation
4. Ensure you're using compatible versions of Python, CUDA, and TensorFlow

---

*Last updated: 2025-05-28* 