# Dayana Gonzalez Cruz
# CST-307: Principles of Modeling and Simulation
# WF1100A Dr. Citro
# 11-1-2023
# Project 4: Part 2: EATSolutions.py
# The purpose of this program is to display the solutions obtained in the Part 2 section of this assignment, as displayed in the accompanying document.

# Chosen solution from c = 2t/100(e^(-1t/20)-1/(-1t/20))
# Simplified and rearranged to -20t^-1 (e^(-1t/20)-1) - Solution 1
# Chosen solution from d) e^(1t/20) - Solution 2

# Import math for e and power utilities
# Import matplotlib for plotting, labeling, and displaying

import matplotlib.pyplot as plt
import math

# Initialized arrays to hold keep solution points
pointsSol1 = []
pointsSol2 = [1]

# Define solution 1 

def Sol1(t0):
	for t in range(1000):
		t += 1
		point = ((3 * t)/100) * (-20 * (pow(t, -1)) *(((pow(math.e,((-1 * t/20))))- 1)))
		pointsSol1.append(point)
		

# Define solution 2 
def Sol2(t0):
	for t in range(1000):
		t += 1
		point = pow(math.e, (-1 * t)/20)
		pointsSol2.append(point)
		
# Displays solutions
def display():
	plt.plot(pointsSol1, label = 'Solution 1')
	plt.plot(pointsSol2, label = 'Solution 2')
	plt.legend()
	plt.xlabel('t')
	plt.ylabel('x(t)')
	plt.title('x(t) = e^(At) * C')
	plt.show()

# Display program purpose
print("The purpose of this program is to display the solutions obtained in the Part 2 section of this assignment, as displayed in the accompanying document.")
print("Chosen solution from c = 2t/100(e^(-1t/20)-1/(-1t/20)) -> Simplified and rearranged to -20t^-1 (e^(-1t/20)-1) - Solution 1")
print("Chosen solution from d) e^(1t/20) - Solution 2")

# Calculate solutions and display

Sol1(1)
Sol2(1)
display()