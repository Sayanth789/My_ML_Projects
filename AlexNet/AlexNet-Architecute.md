| **Layer** | **Type**           | **Maps** | **Size**     | **Kernel-Size** | **Stride**    | **Padding**| **Activation**   |
|-----------|---------------------|----------|--------------|------------------|-------------|-------------|-----------------|
| Out       | Fully Connected     | -        | 1000         | -                | -           |            | Softmax          |
| F10       | Fully Connected     | -        | 4096         | -                | -           |            | ReLU             |
| F9        | Fully Connected     | -        |   4096       | -                | -           |            | ReLU             |
| S8        | Max Pooling         | 256      | 6 × 6b       | 3 × 3            | 2           |  valid     | -                |
| C7        | Convolution         | 256      | 13 × 13      | 3 × 3            | 1           |  same      | ReLU             |
| C6        | Convolution         | 384      | 13 × 13      | 3 × 3            | 1           |  same      | ReLU             |
| C5        | Convolution         | 384      | 13 × 13      | 3 × 3            | 1           |  same      | ReLU             |
| S4        | Max-Pooling         | 256      | 13 × 13      | 3 x 3            | 2           |  valid     | -                |
| C3        | Convolution         | 256      | 27 x 27      | 5 x 5            | 1           |  same      | ReLU             |
| S2        | Max-Pooling         | 96       | 27 x 27      | 3 x 3            | 2           |  valid     | -                |
| C1        | Convolution         | 96       | 55 x 55      | 11 x 11          | 4           |  valid     | ReLU             |
In          | Input               | 3 (RGB)  | 227 x 227    | -                | _           |  -         | -                |


TODO: Add the Notes ....😕 😴
