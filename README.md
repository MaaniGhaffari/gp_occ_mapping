## Gaussian Processes continuous occupancy mapping and exploration
This is a ROS package for 2D Gaussian Processes (GPs) continuous occupancy mapping and exploration based on:

1- M. Ghaffari Jadidi, J. Valls Miro, G. Dissanayake, Mutual Information-based Exploration on Continuous Occupancy Maps, in IEEE/RSJ International Conference on Intelligent Robots and Systems, 2015, pp. 6086-6092.

2- M. Ghaffari Jadidi, J. Valls Miro, R. Valencia, J. Andrade-Cetto, Exploration on Continuous Gaussian Process Frontier Maps, in IEEE International Conference on Robotics and Automation, 2014, pp. 6077-6082.


### Dependencies
The package is written in Python and depends on numpy, scipy, and matplotlib (optional).

For GPs calculation the open source library, pyGPs is used:

- http://www-ai.cs.uni-dortmund.de/weblab/static/api_docs/pyGPs/index.html

The package requires laser scans and corresponding robot poses in LaserScan and PoseStamped message types, respectively.
