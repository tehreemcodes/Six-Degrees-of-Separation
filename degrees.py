import csv
from collections import deque

# Data structures
names = {}
people = {}
movies = {}

# Load data from CSV files
def load_data():
    with open("people.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            person_id = row["id"]
            people[person_id] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            names.setdefault(row["name"].lower(), set()).add(person_id)

    with open("movies.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            movie_id = row["id"]
            movies[movie_id] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    with open("stars.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            person_id = row["person_id"]
            movie_id = row["movie_id"]
            if person_id in people:
                people[person_id]["movies"].add(movie_id)
            if movie_id in movies:
                movies[movie_id]["stars"].add(person_id)

    print("Data loaded successfully")

# Function to find person ID by name
def person_id_for_name(name):
    person_ids = list(names.get(name.lower(), set()))
    if not person_ids:
        print(f"No actor named '{name}'")
        return None
    elif len(person_ids) > 1:
        print(f"Multiple matches found for '{name}':")
        for pid in person_ids:
            print(f"ID: {pid} | Name: {people[pid]['name']} | Birth: {people[pid]['birth']}")
        return input("Enter the correct person ID: ").strip()
    else:
        return person_ids[0]

# Function to find all neighbors (co-stars) for a person
def neighbors_for_person(person_id):
    neighbors = set()
    for movie_id in people[person_id]["movies"]:
        for co_star_id in movies[movie_id]["stars"]:
            if co_star_id != person_id:
                neighbors.add((movie_id, co_star_id))
    return neighbors

# CORRECTED: Shortest path function using BFS
def shortest_path(source, target):
    # Handle same person case
    if source == target:
        return []
    
    # Initialize BFS
    frontier = deque([source])  # Only store person IDs in frontier
    visited = set([source])     # Track visited nodes
    parent = {source: None}     # Track parent relationships
    movie_connection = {}       # Track which movie connects parent to child
    
    while frontier:
        current_id = frontier.popleft()
        
        # Explore all neighbors of current person
        for movie_id, neighbor_id in neighbors_for_person(current_id):
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                parent[neighbor_id] = current_id
                movie_connection[neighbor_id] = movie_id
                frontier.append(neighbor_id)
                
                # Check if we reached the target
                if neighbor_id == target:
                    # Reconstruct path
                    path = []
                    current = target
                    while parent[current] is not None:
                        movie_id = movie_connection[current]
                        path.append((movie_id, current))
                        current = parent[current]
                    path.reverse()
                    return path
    
    return None  # No path found

# Alternative implementation (your original approach, but fixed)
def shortest_path_alternative(source, target):
    if source == target:
        return []
    
    frontier = deque([source])
    visited = set([source])
    paths = {source: []}

    while frontier:
        current_id = frontier.popleft()
        
        for movie_id, neighbor_id in neighbors_for_person(current_id):
            if neighbor_id == target:
                # Found target, return complete path
                return paths[current_id] + [(movie_id, neighbor_id)]
            
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                paths[neighbor_id] = paths[current_id] + [(movie_id, neighbor_id)]
                frontier.append(neighbor_id)
    
    return None

# Function to display path nicely
def display_path(source_id, target_id, path):
    if path is None:
        print("No connection found.")
        return
    
    if len(path) == 0:
        print(f"{people[source_id]['name']} and {people[target_id]['name']} are the same person.")
        return
    
    degrees = len(path)
    print(f"\n{people[source_id]['name']} to {people[target_id]['name']} — {degrees} degrees of separation:\n")
    
    current = source_id
    for movie_id, person_id in path:
        movie_title = movies[movie_id]['title']
        current_name = people[current]['name']
        next_name = people[person_id]['name']
        print(f"{current_name} → {movie_title} → {next_name}")
        current = person_id

# Main execution
def main():
    load_data()

    print("\n" + "="*60)
    print("SIX DEGREES OF KEVIN BACON")
    print("="*60)
    print("Enter actor names to find their connection, or 'quit' to exit")
    
    # Interactive mode
    while True:
        try:
            print()
            source_name = input("Enter source actor's name: ").strip()
            if source_name.lower() == 'quit':
                break
                
            target_name = input("Enter target actor's name: ").strip()
            
            source_id = person_id_for_name(source_name)
            target_id = person_id_for_name(target_name)
            
            if source_id and target_id:
                path = shortest_path(source_id, target_id)
                display_path(source_id, target_id, path)
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()