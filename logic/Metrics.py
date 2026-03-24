import time

evaluated_nodes = 0

def make_ai_move_with_metrics(ai_function, *args, **kwargs):
    global evaluated_nodes
    evaluated_nodes = 0
    
    start_time = time.time()
    
    result = ai_function(*args, **kwargs)
    
    end_time = time.time()
    
    print(f"Patērētais laiks: {end_time - start_time:.6f} sekundes")
    print(f"Novērtēto virsotņu skaits: {evaluated_nodes}")
    
    return result
