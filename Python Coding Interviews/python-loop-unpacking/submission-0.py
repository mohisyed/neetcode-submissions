from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    temp_name,temp_score = "test",0
    for name, score in scores:
        if temp_score < score:
            temp_score = score
            temp_name = name
    return temp_name
    


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
