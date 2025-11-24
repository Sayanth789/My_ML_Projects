## Rotation Matrix
Is a special square matrix used to **rotate vectors** in space without  changing their length

It's a fundamental  concept in: 
* COmputer science 💻 👨‍🔬
* Robotics 🤖 👨‍🦲
* Physics 🧑‍🔬
* 3D Animation 👨‍🔧
* Machine Learning (transformations)

 ### What  does a Rotational Matrix does ?
 A rotational matrix **rotates a point or vector** around the the origin by  a certain angle 

 If we have a vector  
**v = [x, y]** and we multiply it by a rotation matrix:

**v_rotated = R · v**

The result is the rotated vector.

## Rotation Matrix in 2D (very common)

To rotate a vector by angle $\theta$:

$$
R(\theta) =
\begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix}
$$

Example: rotate a point (x, y) by $90^\circ$:

$$
R(90^\circ) =
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
$$
## Rotatin Matrix in 3D 
Theea re **three seperate** rotation matrices :

### Rotation around X-axis
$$
R_x(\theta) = 
\begin{pmatrix}
1 & 0 & 0 \\
0 & \cos\theta & -\sin\theta \\
0 & \sin\theta & \cos\theta
\end{pmatrix}
$$

### Rotation around Y-axis
$$
R_y(\theta) = 
\begin{pmatrix}
\cos\theta & 0 & \sin\theta \\
0 & 1 & 0 \\
-\sin\theta & 0 & \cos\theta
\end{pmatrix}
$$

### Rotation around Z-axis
$$
R_z(\theta) = 
\begin{pmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{pmatrix}
$$



# ⭐ Important properties of Rotation Matrices 
Rotation matrices have special mathematical properties 
### They preserve lengths ( no streching) 
### They preserve angles 
### They are orthogonal  
   **$R^T R = I$**
### Determinant = +1

  


