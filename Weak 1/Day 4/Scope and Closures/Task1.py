call_count = 0

def track_calls():
    global call_count
    call_count += 1

track_calls()
track_calls()
track_calls()
track_calls()
print("Total calls:", call_count)