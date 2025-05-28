# TensorFlow 1.x to 2.x Migration Guide

## Overview
This guide helps you migrate code from TensorFlow 1.x to TensorFlow 2.x, addressing common compatibility issues.

## Key Changes in TensorFlow 2.x

### 1. Eager Execution by Default
- **TensorFlow 1.x**: Graph-based execution with Sessions
- **TensorFlow 2.x**: Eager execution by default (no Sessions needed)

### 2. API Cleanup
- Many deprecated APIs removed
- Simplified API structure
- Better integration with Keras

## Common Migration Issues

### Issue: tf.Session() Not Available

**Error Message**:
```
AttributeError: module 'tensorflow' has no attribute 'Session'
```

**TensorFlow 1.x Code**:
```python
import tensorflow as tf

hello = tf.constant("Hello world")
sess = tf.Session()
print(sess.run(hello))
sess.close()
```

**TensorFlow 2.x Code**:
```python
import tensorflow as tf

hello = tf.constant("Hello world")
print(hello.numpy().decode())
```

### Issue: Placeholders Not Available

**TensorFlow 1.x Code**:
```python
x = tf.placeholder(tf.float32, shape=[None, 784])
y = tf.placeholder(tf.float32, shape=[None, 10])
```

**TensorFlow 2.x Code**:
```python
# Use tf.function for graph execution if needed
@tf.function
def model(x):
    return tf.keras.layers.Dense(10)(x)

# Or use Keras Input layers
inputs = tf.keras.Input(shape=(784,))
outputs = tf.keras.layers.Dense(10)(inputs)
model = tf.keras.Model(inputs, outputs)
```

### Issue: Variable Creation

**TensorFlow 1.x Code**:
```python
W = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([10]))
```

**TensorFlow 2.x Code**:
```python
W = tf.Variable(tf.random.normal([784, 10]))
b = tf.Variable(tf.zeros([10]))
```

### Issue: Training Loops

**TensorFlow 1.x Code**:
```python
optimizer = tf.train.GradientDescentOptimizer(0.01)
train_op = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        _, loss_val = sess.run([train_op, loss], feed_dict={x: batch_x, y: batch_y})
```

**TensorFlow 2.x Code**:
```python
optimizer = tf.keras.optimizers.SGD(0.01)

for i in range(1000):
    with tf.GradientTape() as tape:
        predictions = model(batch_x)
        loss_val = loss_fn(batch_y, predictions)
    
    gradients = tape.gradient(loss_val, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

## Migration Tools

### tf_upgrade_v2 Script
TensorFlow provides an automatic migration tool:

```bash
# Install the upgrade script
pip install tf-upgrade-v2

# Convert a single file
tf_upgrade_v2 --infile old_file.py --outfile new_file.py

# Convert entire directory
tf_upgrade_v2 --intree input_dir --outtree output_dir
```

### Compatibility Mode
For gradual migration, you can use TF 1.x compatibility:

```python
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Now you can use TF 1.x syntax
sess = tf.Session()
# ... rest of TF 1.x code
```

## Best Practices for TensorFlow 2.x

### 1. Use Keras for Model Building
```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

### 2. Use tf.function for Performance
```python
@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x, training=True)
        loss = loss_fn(y, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss
```

### 3. Use tf.data for Input Pipelines
```python
dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
dataset = dataset.batch(32).prefetch(tf.data.AUTOTUNE)
```

## Testing Your Migration

### Before Migration Test
```python
# This will fail in TF 2.x
import tensorflow as tf
sess = tf.Session()
```

### After Migration Test
```python
# This should work in TF 2.x
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("Eager execution enabled:", tf.executing_eagerly())

# Basic operations
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
c = tf.add(a, b)
print("Result:", c.numpy())
```

## Common Gotchas

### 1. Tensor Evaluation
```python
# TF 1.x
result = sess.run(tensor)

# TF 2.x
result = tensor.numpy()  # Only works in eager mode
```

### 2. Variable Initialization
```python
# TF 1.x
sess.run(tf.global_variables_initializer())

# TF 2.x
# Variables are initialized automatically
```

### 3. Control Dependencies
```python
# TF 1.x
with tf.control_dependencies([update_op]):
    train_op = tf.identity(loss)

# TF 2.x
# Usually not needed due to eager execution
# Use tf.function if graph mode is required
```

## Resources

- [Official TensorFlow Migration Guide](https://www.tensorflow.org/guide/migrate)
- [tf_upgrade_v2 Documentation](https://www.tensorflow.org/guide/upgrade)
- [TensorFlow 2.x Effective Guide](https://www.tensorflow.org/guide/effective_tf2)

---

*Last updated: 2025-05-28* 