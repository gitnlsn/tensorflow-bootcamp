import tensorflow as tf
import numpy as np
print("TensorFlow version:", tf.__version__)
print("Keras version:", tf.keras.__version__)
print("Python version:", tf.version.VERSION)

print("\n=== Basic TensorFlow Operations ===")
hello = tf.constant("Hello, TensorFlow!")
print("Constant tensor:", hello.numpy().decode())

a = tf.constant([1, 2, 3, 4, 5])
b = tf.constant([2, 3, 4, 5, 6])
c = tf.add(a, b)
print("Addition result:", c.numpy())

print("\n=== GPU/CPU Device Information ===")
print("Available devices:")
for device in tf.config.list_physical_devices():
    print(f"  {device}")

print("GPU available:", tf.config.list_physical_devices('GPU'))
print("Built with CUDA:", tf.test.is_built_with_cuda())

print("\n=== Simple Neural Network Test ===")
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

X_test = np.random.random((5, 4))
y_test = np.random.randint(0, 3, (5,))

print("Model prediction shape:", model.predict(X_test, verbose=0).shape)
print("✅ TensorFlow installation is working correctly!")