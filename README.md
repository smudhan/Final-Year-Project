# Multi-Purpose Robotic Arm With Automatic Tool Changing and Digital Twin

## 📌 Project Overview
This repository contains the source code, hardware descriptions, and simulation configurations for a **Multi-Purpose Robotic Arm featuring an Automatic Tool-Changing (ATC) system**.

## ✨ Key Features
*   **Automatic Tool-Changing (ATC) System:** A versatile end-effector mechanism allowing the arm to swap tools dynamically without human intervention, maximizing multi-purpose utility.
*   **Real-Time Digital Twin:** A high-fidelity virtual representation of the physical robotic arm built with URDF and simulated in ROS (RViz/Gazebo). The physical and virtual models mirror each other in real-time.
*   **Low-Cost Architecture:** Designed with affordability in mind, replacing expensive proprietary controllers with accessible microcontrollers and serial communication interfaces.
*   **ROS Integration:** Fully built on the ROS framework, ensuring modularity, scalability, and compatibility with a vast ecosystem of robotics libraries.
*   **Real-Time Joint Feedback:** Continuous monitoring and updating of joint states utilizing dedicated joint feedback nodes.

---
## 📂 Project Structure (ROS Workspace)

<img width="794" height="594" alt="image" src="https://github.com/user-attachments/assets/9bd48023-863c-4c93-9bda-ee386256e74c" />

---
## ⚙️ System Architecture

### 1. Digital Twin & Visualization (`my_robot_description`)
The physical characteristics of the robot—including its links, joints, inertial properties, and collision meshes—are defined in `robot.urdf`. STL files (`armlink1urdf.stl`, `baseplateurdf.stl`, etc.) are mapped to these links to provide a visually accurate Digital Twin. `display.launch.py` spins up the robot state publisher and RViz for visualization.

### 2. Hardware Interface (`serial_communication`)
Since the project focuses on a low-cost approach, the physical arm is controlled via microcontrollers. The `serial_node.py` script establishes a robust serial communication pipeline, sending target joint angles to the hardware and receiving real-time encoder feedback.

### 3. State Synchronization (`joint_feedback_node.py`)
To ensure the Digital Twin is a true "twin", the `joint_feedback_node.py` processes the incoming hardware data and broadcasts it to the ROS `/joint_states` topic. This ensures the 3D simulation mirrors the physical arm with near-zero latency.


<img width="479" height="492" alt="Screenshot from 2026-05-17 19-39-33" src="https://github.com/user-attachments/assets/21900638-97ac-487d-a38c-4e0f0af8b7bc" />

---

## 🔧 Automatic Tool-Changing (ATC) System

A major component of this multi-purpose robotic arm is the custom **Automatic Tool-Changing (ATC)** system. 
*   **Mechanical Design:** The ATC is mechanically designed to act as a versatile end-effector mechanism, allowing the robotic arm to seamlessly attach and detach different tools based on the specific task at hand. 
*   **Dynamic Swapping:** This mechanism enables dynamic tool swapping without requiring human intervention, maximizing the multi-purpose utility of this low-cost arm

---
## 🚀 Installation & Setup*   **Digital Twin Integration:** The tool-changing actions and states are fully integrated into the real-time ROS-based Digital Twin, ensuring that whenever a physical tool is swapped, the virtual model updates to reflect the new configuration immediately. 


### Prerequisites
*   **Ubuntu 20.04 / 22.04** (Recommended)
*   **ROS 2 (Humble)**


---

## 🕹️ Usage Guide

### 1. Launching the Digital Twin (Simulation Only)
To view the robotic arm in RViz without connecting the physical hardware, run:
```bash
ros2 launch my_robot_description display.launch.py
```
*(Use `roslaunch my_robot_description display.launch` for ROS 1)*

### 2. Starting Serial Communication
Connect your robotic arm to the computer via USB/Serial, then start the serial communication node:
```bash
ros2 run serial_communication serial_node
```

### 3. Running the Full System (Hardware + Digital Twin)
1. Start the serial node to establish a connection with the arm.
2. Launch the `joint_feedback_node.py` to begin syncing data.
3. Launch the `display.launch.py` to visualize the mirrored movements in real-time.
