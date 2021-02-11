GLOBAL_STATE = {}

class booking_frame(Frame):
    ...
    GLOBAL_STATE["chosen_name"] = "Steve"

class calendar_frame(Frame):
    ...
    print(GLOBAL_STATE.get("chosen_name"))