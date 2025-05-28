# TensorFlow Deep Learning Bootcamp

A comprehensive TensorFlow bootcamp project with updated setup instructions and migration guides for modern TensorFlow versions.

## 📋 Overview

This repository contains materials and setup instructions for a TensorFlow deep learning bootcamp. Originally designed for TensorFlow 1.3, it now includes comprehensive migration guides and setup instructions for TensorFlow 2.x.

## 🚀 Quick Start

### Prerequisites

- Python 3.8-3.11 (TensorFlow 2.15+ supports Python 3.9-3.11)
- pip 19.0 or later
- 64-bit system
- At least 4GB RAM (8GB+ recommended)

### Option 1: Automated Setup (Recommended)

Run the setup script to create a virtual environment with all dependencies:

```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

To activate the environment:
```bash
source tfdeeplearning/bin/activate
```

### Option 2: Manual Installation

#### Using Virtual Environment
```bash
# Create virtual environment
python -m venv tfdeeplearning

# Activate virtual environment
source tfdeeplearning/bin/activate  # Linux/Mac
# tfdeeplearning\Scripts\activate   # Windows

# Upgrade pip
pip install --upgrade pip

# Install TensorFlow and dependencies
pip install tensorflow numpy matplotlib jupyter pandas scikit-learn
```

#### Using Conda
```bash
# Create conda environment
conda create -n tfdeeplearning python=3.10

# Activate environment
conda activate tfdeeplearning

# Install packages
conda install tensorflow numpy matplotlib jupyter pandas scikit-learn
```

## ✅ Verify Installation

Run the installation test:
```bash
python src/installation-testing.py
```

Expected output should include:
- TensorFlow version information
- Basic tensor operations
- Device information (CPU/GPU)
- Simple neural network test
- Success message

## 📚 Documentation

### Setup Guides
- **[TensorFlow Setup Guide](docs/tensorflow_setup_guide.md)** - Comprehensive installation instructions, troubleshooting, and optimization tips
- **[Migration Guide](docs/tensorflow_migration_guide.md)** - Complete guide for migrating from TensorFlow 1.x to 2.x

### Additional Resources
- **[Installation Logs](docs/installation.txt)** - Detailed conda environment creation logs
- **[Testing Guide](docs/installation-testing.txt)** - Installation verification procedures

## 🔄 Migration from TensorFlow 1.x

If you're working with older TensorFlow 1.x code, use our migration guide:

### Key Changes in TensorFlow 2.x
- **Eager execution by default** (no more Sessions)
- **Simplified APIs** with better Keras integration
- **tf.function** for performance optimization
- **Cleaner variable and model management**

### Quick Migration Example
```python
# TensorFlow 1.x (deprecated)
import tensorflow as tf
sess = tf.Session()
result = sess.run(tensor)

# TensorFlow 2.x (current)
import tensorflow as tf
result = tensor.numpy()
```

For complete migration instructions, see [`docs/tensorflow_migration_guide.md`](docs/tensorflow_migration_guide.md).

## 🛠 Troubleshooting

### Common Issues

**GPU Warnings**: CUDA/GPU warnings are normal for CPU-only installations and can be ignored.

**Import Errors**: Ensure your virtual environment is activated and TensorFlow is installed correctly.

**Memory Issues**: Reduce batch sizes or enable GPU memory growth:
```python
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)
```

For detailed troubleshooting, see the [setup guide](docs/tensorflow_setup_guide.md#common-issues-and-solutions).

## 🔧 Development Setup

### Jupyter Notebook
```bash
# Install Jupyter (if not already installed)
pip install jupyter

# Start Jupyter
jupyter notebook
```

### Environment Variables
```bash
# Disable oneDNN optimizations (if causing issues)
export TF_ENABLE_ONEDNN_OPTS=0

# Set logging level
export TF_CPP_MIN_LOG_LEVEL=2  # Suppress INFO/WARNING messages
```

## 📁 Project Structure

```
.
├── README.md                    # This file
├── docs/                        # Documentation
│   ├── tensorflow_setup_guide.md      # Detailed setup instructions
│   ├── tensorflow_migration_guide.md  # TF 1.x to 2.x migration
│   ├── installation.txt               # Installation logs
│   └── installation-testing.txt       # Testing procedures
├── src/                         # Source code
│   └── installation-testing.py        # Installation verification script
├── setup_venv.sh               # Automated environment setup
└── run-python-venv.sh          # Environment activation helper
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with the verification script
5. Submit a pull request

## 📄 License

This project is part of a TensorFlow bootcamp educational material.

## 🆘 Support

If you encounter issues:

1. Check the [troubleshooting section](docs/tensorflow_setup_guide.md#common-issues-and-solutions) in the setup guide
2. Verify your installation with `python src/installation-testing.py`
3. Review the [migration guide](docs/tensorflow_migration_guide.md) if working with older code
4. Open an issue with detailed error messages and system information