| **Layer** | **Type**           | **Maps** | **Size**     | **Kernel-Size** | **Stride** | **Activation** |
|-----------|---------------------|----------|--------------|------------------|------------|-----------------|
| Out       | Fully Connected     | -        | 10           | -                | -          | RBF             |
| F6        | Fully Connected     | -        | 84           | -                | -          | tanh            |
| C5        | Convolution         | 120      | 1 × 1        | 5 × 5            | 1          | tanh            |
| S4        | Avg Pooling         | 16       | 5 × 5        | 2 × 2            | 2          | tanh            |
| C3        | Convolution         | 16       | 10 × 10      | 5 × 5            | 1          | tanh            |
| S2        | Avg Pooling         | 6        | 14 × 14      | 2 × 2            | 2          | tanh            |
| C1        | Convolution         | 6        | 28 × 28      | 5 × 5            | 1          | tanh            |
| IN        | Input               | 1        | 32 × 32      | -                | -          | -               |


### **This is the Architecture of the LeNet5** 🕸️  5️⃣
