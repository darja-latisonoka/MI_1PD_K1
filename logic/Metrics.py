import time

evaluated_nodes = 0

def make_ai_move_with_metrics(ai_function, *args):
    global evaluated_nodes
    evaluated_nodes = 0
    
    start_time = time.time()
    
    result = ai_function(*args)
    
    end_time = time.time()
    
    print(f"Laiks patērēts: {end_time - start_time:.6f} sekundes")
    print(f"Novērtētās virsotnes: {evaluated_nodes}")
    
    return result

