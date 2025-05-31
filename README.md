# Pacman Search AI Project 👾

This project implements classic search algorithms (DFS, BFS, UCS, A*) in the Pacman game environment, as part of an AI course.

## 🚀 Getting Started
1. Extract the project zip.
2. Run the game:
   ```bash
   python pacman.py
   ```
3. See help options:
   ```bash
   python pacman.py -h
   ```

## 🧠 Implemented Algorithms

- **DFS** (Depth-First Search):
  ```bash
  python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch
  ```

- **BFS** (Breadth-First Search):
  ```bash
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  ```

- **UCS** (Uniform Cost Search):
  ```bash
  python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
  ```

- **A\*** (with Manhattan heuristic):
  ```bash
  python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  ```

## 🧩 Corners Problem

- BFS:
  ```bash
  python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
  ```

- A\* with custom heuristic:
  ```bash
  python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
  ```

## ✅ Autograder Tests
```bash
python autograder.py -q q1  # DFS
python autograder.py -q q2  # BFS
python autograder.py -q q3  # UCS
python autograder.py -q q4  # A*
python autograder.py -q q5  # Corners Problem
```

## 📌 Notes
- Use data structures from `util.py` (e.g., Stack, Queue, PriorityQueue).
- Implement **graph search**, not tree search.
- Heuristics must be efficient and not rely on the full GameState.

---

**Author:** [Your Name]  
AI Course Project – 2025
