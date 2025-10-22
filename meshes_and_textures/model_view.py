import pybullet as p
import pybullet_data
import time

# Connect to PyBullet GUI
p.connect(p.GUI)

# Set the search path to PyBullet’s built-in data folder
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the ground plane for reference
plane_id = p.loadURDF("plane.urdf")

# Load your custom URDF file
# Replace this path with your own URDF file path
urdf_path = "base_station.urdf"
model_id = p.loadURDF(urdf_path, basePosition=[0, 0, 0.5])

# Set gravity (optional)
p.setGravity(0, 0, 0)

# Keep the simulation running
while True:
    p.stepSimulation()
    time.sleep(1.0 / 240.0)
