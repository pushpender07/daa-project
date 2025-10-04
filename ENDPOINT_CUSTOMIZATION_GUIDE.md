# Endpoint Customization Feature Guide

## 🎯 New Feature: Customizable Start & End Points

You can now place the start and end points anywhere on the maze! This allows you to:
- Create custom challenges
- Test different path scenarios
- Explore how algorithms behave with different endpoints
- Compare path efficiency from various positions

---

## 📖 How to Use

### Step-by-Step Instructions

#### **1. Generate a Maze**
First, click the **"Generate New Maze"** button to create a maze.

#### **2. Set Custom Start Point**
1. Click the **"Set Start"** button (green button)
2. Your cursor will change to a crosshair ➕
3. Click on any **path cell** (light gray square) where you want the start point
4. The green start marker will move to that location
5. You'll see a confirmation message with the coordinates

#### **3. Set Custom End Point**
1. Click the **"Set End"** button (red button)
2. Your cursor will change to a crosshair ➕
3. Click on any **path cell** (light gray square) where you want the end point
4. The red end marker will move to that location
5. You'll see a confirmation message with the coordinates

#### **4. Solve with Custom Endpoints**
1. Select your preferred algorithm (BFS, DFS, or A*)
2. Click **"Solve Maze"**
3. Watch the algorithm find the path between your custom points!

#### **5. Reset to Default** (Optional)
- Click **"Reset Points"** to restore the original start (top-left) and end (bottom-right) positions

---

## ⚠️ Important Notes

### What You Can Do ✅
- Place start/end on **any path cell** (light gray areas)
- Place them anywhere in the maze - close together or far apart
- Move them as many times as you want
- Solve the same maze multiple times with different endpoints

### What You Cannot Do ❌
- **Cannot place on walls** (dark gray cells) - you'll get an error message
- Cannot place outside the maze boundaries
- The algorithms only work on valid path cells

---

## 🎮 Creative Ways to Use This Feature

### 1. **Challenge Mode**
- Place start and end very close together
- Compare if BFS/DFS/A* all find the same short path

### 2. **Distance Test**
- Place endpoints at opposite corners
- See which algorithm is fastest for long distances
- A* usually wins due to its heuristic!

### 3. **Dead-End Exploration**
- Place an endpoint in a dead-end area
- Watch how algorithms backtrack

### 4. **Path Comparison**
- Solve with one endpoint configuration
- Note the path length
- Move an endpoint slightly
- Solve again and compare!

### 5. **Educational Demonstration**
Perfect for teaching:
- Show students how BFS always finds the shortest path
- Demonstrate how DFS might take a longer route
- Illustrate A*'s intelligent searching

---

## 🎨 Visual Indicators

During customization, watch for these cues:

| Element | Meaning |
|---------|---------|
| 🎯 **Crosshair Cursor** | You're in "Set Start" or "Set End" mode |
| 🖱️ **Arrow Cursor** | Normal mode (not setting endpoints) |
| 🟢 **Green Square** | Current start position |
| 🔴 **Red Square** | Current end position |
| ⬜ **Light Gray** | Valid path cells (you can click these!) |
| ⬛ **Dark Gray** | Walls (cannot place endpoints here) |

---

## 🐛 Troubleshooting

**Problem**: "Cannot place on a WALL!"
- **Solution**: Click only on light gray (path) cells, not dark gray (walls)

**Problem**: Nothing happens when I click
- **Solution**: Make sure you clicked "Set Start" or "Set End" button first

**Problem**: I want to undo my endpoint change
- **Solution**: Click "Reset Points" to go back to defaults, or click the same button again to choose a different spot

**Problem**: Algorithm says "No path found"
- **Solution**: The endpoints you chose might be in disconnected areas. Try different positions or reset to defaults.

---

## 💡 Tips & Tricks

1. **Experiment Freely**: There's no penalty for trying different positions!

2. **Algorithm Comparison**: Set custom endpoints, then try all three algorithms on the same configuration to compare performance.

3. **Understanding Heuristics**: Place endpoints where A*'s Manhattan distance heuristic can shine - you'll see it explores fewer cells than BFS!

4. **Teaching Tool**: Great for demonstrating pathfinding concepts:
   - Show that BFS/A* always find optimal paths
   - Show that DFS path length varies
   - Demonstrate algorithm efficiency differences

5. **Path Length Analysis**: 
   - Diagonal placements (far apart) = longer paths
   - Adjacent placements = very short paths
   - Compare path lengths across algorithms

---

## 🚀 Example Use Cases

### Example 1: Short Path Test
```
1. Generate maze
2. Set Start at position (5, 5)
3. Set End at position (5, 7) - just 2 cells away
4. Solve with BFS - likely finds direct path
5. Solve with DFS - might take roundabout route!
```

### Example 2: Algorithm Race
```
1. Generate maze
2. Set Start at top-right corner
3. Set End at bottom-left corner
4. Time each algorithm:
   - BFS: Usually 3-5ms
   - DFS: Usually 2-4ms  
   - A*: Usually 1-3ms (winner!)
```

### Example 3: Educational Demo
```
Teacher: "Let's see if BFS really finds the shortest path!"
1. Generate maze
2. Set custom endpoints in middle of maze
3. Solve with BFS - note path length
4. Solve with DFS - compare path length
5. Students see BFS path ≤ DFS path always!
```

---

## 📊 What This Feature Demonstrates

From a DSA perspective, this feature showcases:

1. **Algorithm Flexibility**: Same algorithm works with any valid endpoints
2. **Graph Theory**: Start/end are just graph nodes - position doesn't matter
3. **Correctness**: Algorithms find valid paths regardless of endpoint positions
4. **Performance**: Compare algorithm efficiency across different scenarios

---

## 🎓 Learning Value

This interactive feature helps understand:
- How pathfinding algorithms adapt to different scenarios
- Why BFS/A* are optimal (always shortest path, regardless of endpoints)
- Why DFS is not optimal (path varies with endpoints)
- Real-world applications (GPS recalculates route when you move!)

---

Enjoy exploring different maze configurations! 🎉

**Pro Tip**: Generate one maze, then set 5 different endpoint pairs and solve each with all 3 algorithms = 15 different paths to compare! 📈

