# Quick Start Guide

## Running the Application

### Method 1: Double-click (Windows)
Simply double-click `main.py` if Python is set up as default program for .py files

### Method 2: Command Line
```bash
python main.py
```

## How to Use

1. **Click "Generate New Maze"** 
   - This creates a random maze using DFS algorithm
   - The maze is always solvable

2. **Select an Algorithm**
   - **BFS**: Breadth-First Search - Guarantees shortest path
   - **DFS**: Depth-First Search - Finds any path (may not be shortest)
   - **A***: A-Star - Intelligent search using heuristic (usually fastest)

3. **Click "Solve Maze"**
   - Watch the solution appear in blue
   - See path length and solving time

4. **Customize Start/End Points** (NEW!)
   - Click **"Set Start"** button
   - Click on any path (light gray) cell to place the start point
   - Click **"Set End"** button
   - Click on any path cell to place the end point
   - Click **"Reset Points"** to restore default positions
   - Solve the maze with your custom endpoints!

5. **Compare Algorithms**
   - Generate one maze
   - Try all three algorithms on the same maze
   - Compare path lengths and solving times!

## What You're Seeing

- 🟢 **Green Square**: Start position (top-left area)
- 🔴 **Red Square**: End position (bottom-right area)
- ⬛ **Dark Gray**: Walls
- ⬜ **Light Gray**: Open paths
- 🔵 **Blue Line**: Solution path found by algorithm

## Tips

- BFS and A* always find the shortest path
- DFS might find a longer path but uses less memory
- A* is usually fastest because it uses intelligent searching
- Try generating multiple mazes to see different patterns!

## Troubleshooting

**Problem**: "No module named tkinter"
**Solution**: 
- Windows/Mac: tkinter comes with Python, reinstall Python
- Linux: `sudo apt-get install python3-tk`

**Problem**: Window doesn't appear
**Solution**: Make sure you're not running in a headless environment (need display)

## Understanding the Algorithms

### Maze Generation (Recursive Backtracking)
- Starts with grid full of walls
- Carves paths using depth-first search
- Creates a "perfect maze" (one solution between any two points)

### BFS (Breadth-First Search)
- Explores maze level by level
- Uses a Queue data structure
- Always finds shortest path

### DFS (Depth-First Search)
- Explores as far as possible before backtracking
- Uses a Stack data structure
- Finds a path, but not necessarily shortest

### A* (A-Star)
- Smart search using distance estimation
- Uses a MinHeap (priority queue)
- Finds shortest path efficiently

Enjoy exploring algorithms! 🚀

