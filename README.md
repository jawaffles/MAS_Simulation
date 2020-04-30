Move all files in the gazebo_models folder into ~/.gazebo



Start MultiAgent Simulation :

```
roslaunch MAS mas.launch 
```
------------------------------------------

Control QuadCopter:


Enable Motors

```
rosservice call /quadcopter/enable_motors "enable: true"
```


Send Position Commands to Quadcopter:

```
rostopic pub /quadcopter/command/pose geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'world'
pose:
  position:
    x: 0.0
    y: 0.0
    z: 11.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
``` 
-----

Control Husky (Currently Without Obstacle Avoidance):

Control husky 1:

```
rostopic pub /h1/move_base_simple/goal geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'map'  
pose:
  position:
    x: 1.0
    y: 1.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0" 
```


