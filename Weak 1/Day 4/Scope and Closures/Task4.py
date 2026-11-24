def process_task():
    status = "pending"

    def complete_task():
        nonlocal status
        status = "completed"

    complete_task()
    print("Final status:", status)

process_task()