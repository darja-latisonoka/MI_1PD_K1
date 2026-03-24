def count_total_tree_nodes(number):
    if number == 2 or number == 3:
        return 1
    
    total_nodes = 1
    
    if number % 2 == 0:
        total_nodes += count_total_tree_nodes(number // 2)
        
    if number % 3 == 0:
        total_nodes += count_total_tree_nodes(number // 3)
        
    return total_nodes
