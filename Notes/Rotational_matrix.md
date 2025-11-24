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

 If we have a vactor 
  V = [x , y] and if we multiply it by a rotation matrix
  
  v_rotated = R . v 
  the result is the rotated vector 
  
  ## Rotation Matrix in 2D (very common) 
   To rotate a vector by angle $\theta$:
   R($\theta$) = 
          $$ A = \begin{rmatrix}
          cos$theta$ & -sin$theta$  \\
          sin$theta$ & cos$theta$
          \end{rmatrix}
          $$
   Example : rotate a point (x, y) by 90$degree$:
       R(90$degree$) = $$ B = \begin{r2matrix}
          0 & -1 \\
          1 & 0 
          /end{r2matrix}
          $$
