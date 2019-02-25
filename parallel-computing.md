# Parallel computing standards and frameworks 

We are using a little bit of openmp.

We don't have access to the iPhone CPUS in a crossplatform manner. The only way is to use metal or shaders. 
We are not ready yet with the implementation in order to use shaders. 

CUDA is not an option. We only use it for ZED CAM in Windows 

Tech stack

|                 | Khronos Group | ltseez | Apple| 
| ---             |  ---          | ---    | ---  |
| higher<br>level | OpenVX        | OpenCV |      |
|                 | OpenCL        |        |       |     
| lower<br>level  | Vulkan        |        | Metal|

