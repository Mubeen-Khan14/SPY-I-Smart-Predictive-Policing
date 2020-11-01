# SPY-I-Smart-Predictive-Policing
The project covers different aspects of crowd analysis such as Crowd Counting, Crowd Density Estimation and the Crowd Activity Recognition i.e suspicious activity detection.
# Suspicious Activity Recognition
# Hardware Requirement
A desktop with 3.4GHz CPU, 8G memory, 32-bit or 64-bit processor, minimum 8-bit graphic adapter and running windows operation system. Basic hardware like monitor, mouse and keyboard are a must for input and output. A CD-ROM or a USB port to install the nessary soft wares. An additional camera will be required for real-time video processing.
# Software Requirement
Python with the version 3.7.x with the following modules installed, opencv, numpy, os, time, fmatch, pickle. Windows operation system. Camera modules installed for importing video file from camera.
# Methodology
Extract usable data by resizing each frame into different scales and uniformly partition each layer to a set of non-overlapping patches. All patches have the same size.
Corresponding regions in 5 continuous frames are stacked together to form a spatial-temporal cube. This pyramid involves local information in fine-scale layers and more global structures in small-resolution ones. With the spatial-temporal cubes, compute 3D gradient features on each of them following [11]. These features in a video sequence are processed separately according to their spatial coordinates. Only features at the same spatial location in the video frames are used together for training and testing. The goal is to find a sparse basis combination set S = {S1,..., SK} with each Si ∈Rp×s containing s dictionary basis vectors, forming a unique combination, where s<<q. Each Si belongs to a closed, convex and bounded set, which ensures column-wise unit Norm to prevent over-fitting. Sparse combination learning has two goals. The first goal – effective representation – is to find K basis combinations, which enjoy a small reconstruction error t.The second goal is to make the total number K of combinations small enough based on redundant surveillance video information.
# Advantages
The hardware requirements are very less as compared to many other algorithms.
