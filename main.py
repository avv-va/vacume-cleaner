# re-entering: -1 point
# each step without cleaning: -1 point
# cleaning: 20 point
# plus: clean_rate = num_of_cleaned/steps_taken 
total_score = 0
seen_places = []
num_cleaned_places = 0
def performance_measure(current_step):
    if current_step.is_dirty:
        total_score = total_score + 20
    elif current_step.is_dirty is False:
        total_score = total_score - 1        
    if current_step in seen_places:
        total_score = total_score - 1
    clean_rate = num_cleaned_places/ len(seen_places)
    total_score += total_score + clean_rate * 10