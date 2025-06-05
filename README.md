# 🎬 Six Degrees of Separation - Actor Connection Finder

This project is a Python-based AI application that finds the **shortest connection path** between two actors based on the movies they've appeared in. It's inspired by the game **"Six Degrees of Kevin Bacon"**, where the goal is to show how any actor is linked to Kevin Bacon through no more than six film collaborations.

## 📌 Project Overview

Using structured data from IMDb-style CSV files, the program builds a graph of actors and movies. It then employs **Breadth-First Search (BFS)** to determine the shortest sequence of shared movie appearances between any two actors.

## 🧠 Key Features

- Loads and parses actor and movie data from CSV files.
- Resolves ambiguities when multiple actors share the same name.
- Finds the shortest connection path between any two actors.
- Prints a human-readable chain of movies connecting them.
- Includes two BFS implementations (standard and alternative).
- Handles edge cases like:
  - Same actor selected as source and target.
  - No path found between the actors.

## 📁 Dataset

The `small/` directory contains three essential CSV files:

| File         | Description                          |
|--------------|--------------------------------------|
| `people.csv` | Actor details: ID, Name, Birth Year  |
| `movies.csv` | Movie details: ID, Title, Year       |
| `stars.csv`  | Relationships: Actor ID ↔ Movie ID   |

Example:
```
people.csv: 102,Kevin Bacon,1958  
movies.csv: 104257,A Few Good Men,1992  
stars.csv: 102,104257
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/tehreemcodes/Six-Degrees-of-Separation.git
cd Six-Degrees-of-Separation
```

### 2. Add Dataset Files

Place your `people.csv`, `movies.csv`, and `stars.csv` files inside the root directory or in a folder named `small/` as needed.

### 3. Run the Program

```bash
degrees.py
```

Follow the prompts:

```
Enter source actor's name: Jennifer Lawrence  
Enter target actor's name: Tom Hanks
```

Example output:

```
Jennifer Lawrence to Tom Hanks — 2 degrees of separation:

Jennifer Lawrence → X-Men: First Class → Kevin Bacon  
Kevin Bacon → Apollo 13 → Tom Hanks
```

## 🔍 Search Strategy

### Why Breadth-First Search (BFS)?

We use BFS to explore the graph of actors and movies because:

- The graph is **unweighted**: All connections are considered equal.
- BFS always finds the **shortest path** (minimum number of edges).
- It's optimal and complete for unweighted graphs.

Two BFS-based implementations are included:
- `shortest_path`: Efficiently tracks parent nodes and reconstructs the path.
- `shortest_path_alternative`: Stores paths directly during traversal.

## 🛠️ File Structure

```
├── people.csv  
├── movies.csv  
├── stars.csv  
├── degrees.py  
└── README.md
```

## 📄 Example Use Cases

- **Actor Networking**: Find indirect collaborations between stars.  
- **Data Analysis**: Explore the connectedness of actors.  
- **Games & Trivia**: Recreate the “Six Degrees of Kevin Bacon” game.


## 🤝 Contributing

Pull requests and issues are welcome! Feel free to fork and enhance.

## 🙋‍♂️ Acknowledgments

Inspired by:
- CS50's AI course by Harvard.  
- The "Six Degrees of Kevin Bacon" concept.
