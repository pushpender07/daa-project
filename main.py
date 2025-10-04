from data_structures import Stack, Queue, MinHeap
import tkinter as tk
from tkinter import ttk
import time


class Maze:
    """
    Maze class that handles maze generation and solving using various algorithms.
    The maze is represented as a 2D grid where:
    - 1 represents a wall
    - 0 represents a path
    """
    
    def __init__(self, rows, cols):
        """
        Initialize maze with given dimensions.
        Time Complexity: O(rows * cols)
        """
        self.rows = rows
        self.cols = cols
        # Initialize maze with all walls
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)]
        self.start = (1, 1)
        self.end = (rows - 2, cols - 2)
        
    def generate_maze(self):
        """
        Generate maze using Recursive Backtracking algorithm with DFS.
        
        Algorithm:
        1. Start with a grid full of walls
        2. Choose a random starting cell, mark it as path
        3. While there are unvisited cells:
            - If current cell has unvisited neighbors:
                * Choose random unvisited neighbor
                * Remove wall between current and chosen cell
                * Push current cell to stack
                * Make chosen cell current
            - Else:
                * Pop cell from stack and make it current
        
        Time Complexity: O(rows * cols) - visits each cell once
        Space Complexity: O(rows * cols) - for the stack in worst case
        """
        # Start from (1, 1)
        start_row, start_col = 1, 1
        self.grid[start_row][start_col] = 0
        
        stack = Stack()
        stack.push((start_row, start_col))
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        visited[start_row][start_col] = True
        
        # Directions: up, right, down, left
        directions = [(-2, 0), (0, 2), (2, 0), (0, -2)]
        
        while not stack.is_empty():
            current_row, current_col = stack.peek()
            
            # Find unvisited neighbors
            neighbors = []
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                if (0 < new_row < self.rows - 1 and 
                    0 < new_col < self.cols - 1 and 
                    not visited[new_row][new_col]):
                    neighbors.append((new_row, new_col, dr, dc))
            
            if neighbors:
                # Choose random neighbor using simple randomization
                import time
                random_index = int((time.time() * 1000000) % len(neighbors))
                new_row, new_col, dr, dc = neighbors[random_index]
                
                # Remove wall between current and neighbor
                wall_row = current_row + dr // 2
                wall_col = current_col + dc // 2
                self.grid[wall_row][wall_col] = 0
                self.grid[new_row][new_col] = 0
                
                visited[new_row][new_col] = True
                stack.push((new_row, new_col))
            else:
                stack.pop()
        
        # Ensure start and end are clear
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.end[0]][self.end[1]] = 0
    
    def solve_bfs(self):
        """
        Solve maze using Breadth-First Search (BFS) with Queue.
        BFS guarantees shortest path in unweighted graph.
        
        Algorithm:
        1. Create queue and add start position
        2. While queue is not empty:
            - Dequeue current position
            - If current is end, reconstruct path
            - For each neighbor:
                * If not visited and is path, enqueue and mark visited
        
        Time Complexity: O(rows * cols) - visits each cell at most once
        Space Complexity: O(rows * cols) - for queue and visited array
        
        Returns:
            list: Path from start to end, or empty list if no path
        """
        queue = Queue()
        queue.enqueue(self.start)
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        parent = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        visited[self.start[0]][self.start[1]] = True
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while not queue.is_empty():
            current_row, current_col = queue.dequeue()
            
            # Check if we reached the end
            if (current_row, current_col) == self.end:
                return self._reconstruct_path(parent)
            
            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                
                if (0 <= new_row < self.rows and 
                    0 <= new_col < self.cols and
                    not visited[new_row][new_col] and 
                    self.grid[new_row][new_col] == 0):
                    
                    visited[new_row][new_col] = True
                    parent[new_row][new_col] = (current_row, current_col)
                    queue.enqueue((new_row, new_col))
        
        return []  # No path found
    
    def solve_dfs(self):
        """
        Solve maze using Depth-First Search (DFS) with Stack.
        DFS does not guarantee shortest path but uses less memory.
        
        Algorithm:
        1. Create stack and push start position
        2. While stack is not empty:
            - Pop current position
            - If current is end, reconstruct path
            - For each neighbor:
                * If not visited and is path, push and mark visited
        
        Time Complexity: O(rows * cols) - visits each cell at most once
        Space Complexity: O(rows * cols) - for stack and visited array
        
        Returns:
            list: A path from start to end, or empty list if no path
        """
        stack = Stack()
        stack.push(self.start)
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        parent = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        visited[self.start[0]][self.start[1]] = True
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while not stack.is_empty():
            current_row, current_col = stack.pop()
            
            # Check if we reached the end
            if (current_row, current_col) == self.end:
                return self._reconstruct_path(parent)
            
            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                
                if (0 <= new_row < self.rows and 
                    0 <= new_col < self.cols and
                    not visited[new_row][new_col] and 
                    self.grid[new_row][new_col] == 0):
                    
                    visited[new_row][new_col] = True
                    parent[new_row][new_col] = (current_row, current_col)
                    stack.push((new_row, new_col))
        
        return []  # No path found
    
    def solve_astar(self):
        """
        Solve maze using A* algorithm with MinHeap priority queue.
        A* uses heuristic (Manhattan distance) to find optimal path efficiently.
        
        Algorithm:
        1. Create min heap with (f_score, position) where f = g + h
        2. g_score: actual distance from start
        3. h_score: heuristic (Manhattan distance to end)
        4. While heap is not empty:
            - Pop position with lowest f_score
            - If current is end, reconstruct path
            - For each neighbor, update scores if better path found
        
        Time Complexity: O(rows * cols * log(rows * cols)) - heap operations
        Space Complexity: O(rows * cols) - for heap and score arrays
        
        Returns:
            list: Optimal path from start to end, or empty list if no path
        """
        def heuristic(pos1, pos2):
            """Manhattan distance heuristic"""
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        
        # Priority queue: (f_score, position)
        heap = MinHeap()
        heap.push((0, self.start))
        
        # g_score: cost from start to this position
        g_score = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]
        g_score[self.start[0]][self.start[1]] = 0
        
        # f_score: g_score + heuristic
        f_score = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]
        f_score[self.start[0]][self.start[1]] = heuristic(self.start, self.end)
        
        parent = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while not heap.is_empty():
            _, current = heap.pop()
            current_row, current_col = current
            
            if visited[current_row][current_col]:
                continue
            
            visited[current_row][current_col] = True
            
            # Check if we reached the end
            if current == self.end:
                return self._reconstruct_path(parent)
            
            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                neighbor = (new_row, new_col)
                
                if (0 <= new_row < self.rows and 
                    0 <= new_col < self.cols and
                    not visited[new_row][new_col] and 
                    self.grid[new_row][new_col] == 0):
                    
                    tentative_g_score = g_score[current_row][current_col] + 1
                    
                    if tentative_g_score < g_score[new_row][new_col]:
                        parent[new_row][new_col] = current
                        g_score[new_row][new_col] = tentative_g_score
                        f_score[new_row][new_col] = tentative_g_score + heuristic(neighbor, self.end)
                        heap.push((f_score[new_row][new_col], neighbor))
        
        return []  # No path found
    
    def _reconstruct_path(self, parent):
        """
        Reconstruct path from parent array.
        Time Complexity: O(path_length)
        """
        path = []
        current = self.end
        
        while current is not None:
            path.append(current)
            current = parent[current[0]][current[1]]
        
        path.reverse()
        return path


class MazeGUI:
    """
    GUI for maze visualization using tkinter.
    Displays maze generation and solving process with animations.
    """
    
    def __init__(self, root):
        """Initialize GUI components"""
        self.root = root
        self.root.title("Maze Generator & Solver - DSA Project")
        self.root.geometry("900x750")
        
        # Maze parameters
        self.cell_size = 15
        self.rows = 31  # Odd number for better maze generation
        self.cols = 41
        self.maze = None
        
        # Colors
        self.color_wall = "#2C3E50"
        self.color_path = "#ECF0F1"
        self.color_start = "#27AE60"
        self.color_end = "#E74C3C"
        self.color_solution = "#3498DB"
        self.color_hover = "#F39C12"
        
        # Customization mode
        self.custom_mode = None  # 'start' or 'end'
        self.current_solution = None
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create all GUI widgets"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="Maze Generator & Solver",
            font=("Arial", 20, "bold"),
            bg="#34495E",
            fg="white",
            pady=10
        )
        title_label.pack(fill=tk.X)
        
        # Control panel
        control_frame = tk.Frame(self.root, bg="#ECF0F1", pady=10)
        control_frame.pack(fill=tk.X)
        
        # Generate button
        tk.Button(
            control_frame,
            text="Generate New Maze",
            command=self.generate_maze,
            bg="#27AE60",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=5
        ).pack(side=tk.LEFT, padx=10)
        
        # Algorithm selection
        tk.Label(
            control_frame,
            text="Algorithm:",
            font=("Arial", 12),
            bg="#ECF0F1"
        ).pack(side=tk.LEFT, padx=5)
        
        self.algorithm_var = tk.StringVar(value="BFS")
        algorithms = ["BFS", "DFS", "A*"]
        algorithm_menu = ttk.Combobox(
            control_frame,
            textvariable=self.algorithm_var,
            values=algorithms,
            state="readonly",
            width=10,
            font=("Arial", 11)
        )
        algorithm_menu.pack(side=tk.LEFT, padx=5)
        
        # Solve button
        tk.Button(
            control_frame,
            text="Solve Maze",
            command=self.solve_maze,
            bg="#3498DB",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=5
        ).pack(side=tk.LEFT, padx=10)
        
        # Separator
        tk.Frame(control_frame, width=2, bg="#95A5A6").pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Customize endpoints
        tk.Label(
            control_frame,
            text="Customize:",
            font=("Arial", 12),
            bg="#ECF0F1"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame,
            text="Set Start",
            command=self.set_start_mode,
            bg="#27AE60",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame,
            text="Set End",
            command=self.set_end_mode,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame,
            text="Reset Points",
            command=self.reset_endpoints,
            bg="#95A5A6",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        # Info label
        self.info_label = tk.Label(
            self.root,
            text="Click 'Generate New Maze' to start!",
            font=("Arial", 11),
            bg="#ECF0F1",
            pady=5
        )
        self.info_label.pack(fill=tk.X)
        
        # Canvas for maze
        canvas_frame = tk.Frame(self.root, bg="#BDC3C7")
        canvas_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
        
        self.canvas = tk.Canvas(
            canvas_frame,
            width=self.cols * self.cell_size,
            height=self.rows * self.cell_size,
            bg="white",
            cursor="arrow"
        )
        self.canvas.pack()
        
        # Bind click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Legend
        legend_frame = tk.Frame(self.root, bg="#ECF0F1", pady=10)
        legend_frame.pack(fill=tk.X)
        
        legends = [
            ("Start", self.color_start),
            ("End", self.color_end),
            ("Wall", self.color_wall),
            ("Path", self.color_path),
            ("Solution", self.color_solution)
        ]
        
        for text, color in legends:
            frame = tk.Frame(legend_frame, bg="#ECF0F1")
            frame.pack(side=tk.LEFT, padx=15)
            
            tk.Canvas(
                frame,
                width=20,
                height=20,
                bg=color,
                highlightthickness=1,
                highlightbackground="black"
            ).pack(side=tk.LEFT, padx=5)
            
            tk.Label(
                frame,
                text=text,
                font=("Arial", 10),
                bg="#ECF0F1"
            ).pack(side=tk.LEFT)
    
    def generate_maze(self):
        """Generate new maze and display it"""
        self.info_label.config(text="Generating maze using DFS with Stack...")
        self.root.update()
        
        self.maze = Maze(self.rows, self.cols)
        self.maze.generate_maze()
        
        self.draw_maze()
        self.info_label.config(
            text=f"Maze generated! Select algorithm and click 'Solve Maze'. Size: {self.rows}x{self.cols}"
        )
    
    def draw_maze(self, path=None):
        """Draw the maze on canvas"""
        self.canvas.delete("all")
        
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Determine color
                if (row, col) == self.maze.start:
                    color = self.color_start
                elif (row, col) == self.maze.end:
                    color = self.color_end
                elif path and (row, col) in path:
                    color = self.color_solution
                elif self.maze.grid[row][col] == 1:
                    color = self.color_wall
                else:
                    color = self.color_path
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=""
                )
        
        self.root.update()
    
    def solve_maze(self):
        """Solve maze using selected algorithm"""
        if self.maze is None:
            self.info_label.config(text="Please generate a maze first!")
            return
        
        algorithm = self.algorithm_var.get()
        self.info_label.config(text=f"Solving maze using {algorithm}...")
        self.root.update()
        
        start_time = time.time()
        
        if algorithm == "BFS":
            path = self.maze.solve_bfs()
        elif algorithm == "DFS":
            path = self.maze.solve_dfs()
        else:  # A*
            path = self.maze.solve_astar()
        
        end_time = time.time()
        solve_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        if path:
            self.current_solution = path
            self.draw_maze(path)
            self.info_label.config(
                text=f"{algorithm} found path! Length: {len(path)} cells, Time: {solve_time:.2f}ms"
            )
        else:
            self.current_solution = None
            self.info_label.config(text=f"No path found using {algorithm}!")
    
    def set_start_mode(self):
        """Enable mode to set custom start point"""
        if self.maze is None:
            self.info_label.config(text="Please generate a maze first!")
            return
        
        self.custom_mode = 'start'
        self.canvas.config(cursor="crosshair")
        self.info_label.config(text="Click on a PATH cell (light gray) to set START point")
    
    def set_end_mode(self):
        """Enable mode to set custom end point"""
        if self.maze is None:
            self.info_label.config(text="Please generate a maze first!")
            return
        
        self.custom_mode = 'end'
        self.canvas.config(cursor="crosshair")
        self.info_label.config(text="Click on a PATH cell (light gray) to set END point")
    
    def reset_endpoints(self):
        """Reset start and end points to default positions"""
        if self.maze is None:
            self.info_label.config(text="Please generate a maze first!")
            return
        
        self.maze.start = (1, 1)
        self.maze.end = (self.rows - 2, self.cols - 2)
        self.custom_mode = None
        self.canvas.config(cursor="arrow")
        self.current_solution = None
        self.draw_maze()
        self.info_label.config(text="Endpoints reset to default positions!")
    
    def on_canvas_click(self, event):
        """Handle click on canvas to set custom start/end points"""
        if self.maze is None or self.custom_mode is None:
            return
        
        # Convert click coordinates to grid position
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        # Validate position is within bounds
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        
        # Check if clicked cell is a path (not a wall)
        if self.maze.grid[row][col] == 1:
            self.info_label.config(text="Cannot place on a WALL! Click on a path cell (light gray)")
            return
        
        # Set the appropriate endpoint
        if self.custom_mode == 'start':
            self.maze.start = (row, col)
            self.info_label.config(text=f"Start point set to ({row}, {col})! Click 'Solve Maze' to find path")
        else:  # 'end'
            self.maze.end = (row, col)
            self.info_label.config(text=f"End point set to ({row}, {col})! Click 'Solve Maze' to find path")
        
        # Exit custom mode and redraw
        self.custom_mode = None
        self.canvas.config(cursor="arrow")
        self.current_solution = None
        self.draw_maze()


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = MazeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

