import math
import time
import tkinter as tk


WIDTH, HEIGHT = 1920, 1080
SEGMENT_LENGTH = 100
SPINS_PER_SECOND = (1, 0, 0.1, 0)
FRAME_DELAY_MS = 1

root = tk.Tk()
root.title("Spinning joints")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="darkgray", highlightthickness=0)
canvas.pack()

anchor = (0.1, HEIGHT / 3)
previous_joints = None
start_time = time.perf_counter()


def animate():
	global previous_joints

	elapsed = time.perf_counter() - start_time
	angles = [elapsed * spins * 2 * math.pi for spins in SPINS_PER_SECOND]

	# Four equal links put the three hinges at 1/4, 1/2, and 3/4 of the line.
	link_angles = (0.0, angles[0], angles[0] + angles[1], sum(angles))
	points = [anchor]
	x, y = anchor
	for angle in link_angles:
		x += SEGMENT_LENGTH * math.cos(angle)
		y += SEGMENT_LENGTH * math.sin(angle)
		points.append((x, y))

	joints = points[1:2]
	if previous_joints is not None:
		for old, new in zip(previous_joints, joints):
			canvas.create_line(*old, *new, fill="white", width=1)

	for start, end in zip(points, points[1:]):
		canvas.create_line(*start, *end, fill="white", width=2)
	for jx, jy in joints:
		canvas.create_oval(jx - 5, jy - 5, jx + 5, jy + 5, fill="white", outline="white")

	previous_joints = joints
	root.after(FRAME_DELAY_MS, animate)


animate()
root.mainloop()
