import math
import matplotlib.pyplot as plt

# Starting position
position = [0, 0]

# Commands: list of vector moves (x, y)
commands = [
    [4, 0],    # Right (East) 4 steps
    [0, 2],    # Up (North) 2 steps
    [-1, 0],   # Left (West) 1 step
    [0, -3]    # Down (South) 3 steps
]

# Track all steps for plotting
path = [position.copy()]

# Apply all vector movements
for move in commands:
    position[0] += move[0]
    position[1] += move[1]
    path.append(position.copy())

# Final Position
print("📍 Final Position Vector:", position)

# Total Displacement (Euclidean Norm)
displacement = math.sqrt(position[0]**2 + position[1]**2)
print("📏 Total Displacement (Norm):", round(displacement, 2))

# Unit vector (Direction)
if displacement != 0:
    unit_vector = [
        round(position[0] / displacement, 3),
        round(position[1] / displacement, 3)
    ]
else:
    unit_vector = [0, 0]

print("🧭 Unit Direction Vector:", unit_vector)

# Plot the path
x_vals = [p[0] for p in path]
y_vals = [p[1] for p in path]

plt.plot(x_vals, y_vals, marker='o', linestyle='--', color='blue')
plt.title("📌 Vector Movement Path")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.text(x_vals[0], y_vals[0], "Start", fontsize=9)
plt.text(x_vals[-1], y_vals[-1], "End", fontsize=9)
plt.axis("equal")
plt.show()
