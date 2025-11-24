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
