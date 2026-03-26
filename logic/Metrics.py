import time

evaluated_nodes = 0
visited_nodes = set()
total_nodes = 0

total_time = 0.0
total_unique_visited = 0
total_tree_nodes = 0
move_count = 0

def make_ai_move_with_metrics(ai_function, *args):
    global evaluated_nodes, total_nodes
    global total_time, total_unique_visited, total_tree_nodes, move_count
    
    evaluated_nodes = 0

    start_time = time.time()
    result = ai_function(*args)
    end_time = time.time()

    elapsed = end_time - start_time
    unique = len(visited_nodes)

    total_time += elapsed
    total_unique_visited += unique
    total_tree_nodes += total_nodes
    move_count += 1

    return result

def print_summary():
    if move_count == 0:
        return
    print(f"--- Spēles statistika ---")
    print(f"Gājienu skaits: {move_count}")
    print(f"Vidējais laiks uz gājienu: {total_time / move_count:.6f} sekundes")
    print(f"Kopā unikālās novērtētās virsotnes: {total_unique_visited}")
    print(f"Kopā koka virsotnes: {total_tree_nodes}")