cmake_minimum_required(VERSION 3.8)
project(my_robot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# =========================================================
# Dependencies
# =========================================================
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# =========================================================
# Install folders
# =========================================================
install(
  DIRECTORY urdf meshes launch
  DESTINATION share/${PROJECT_NAME}
)

# =========================================================
# Install Python scripts
# =========================================================
install(
  PROGRAMS
    scripts/joint_feedback_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# =========================================================
# Testing
# =========================================================
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)

  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
