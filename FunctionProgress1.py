import time
class Progress:
    """This Function is Used to Print the progress of some actions on Dataframe"""
    def __init__(self) -> None:
        self.time_taken_list =[]
        
    def print_progress(self,current_index:int, total_indexes:int, time_taken: time):
        self.time_taken_list.append(time_taken)
        time_spilled = sum(self.time_taken_list)
        average_time = (time_spilled)/len(self.time_taken_list)
        estd_time_to_complt = (average_time * total_indexes) - (time_spilled)
        print(f"{current_index}th/{total_indexes}th Completed in:", f"{time_taken:.2f} seconds." if time_taken<60 else f"{(time_taken/60):.2f} minutes. " ,\
        "| Estimated Time to Complete:", f"{estd_time_to_complt:.2f} seconds. " if estd_time_to_complt<60 else f"{(estd_time_to_complt/60):.2f} minutes. "  ,\
        "| Total Time Spilled:",f"{time_spilled:.2f} seconds. "if time_spilled <60 else f"{(time_spilled/60):.2f} minutes.",end='\r')
    