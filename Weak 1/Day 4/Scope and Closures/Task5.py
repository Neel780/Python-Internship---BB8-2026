mode = "global_mode"

def outer():
    mode = "enclosing_mode"

    def inner():
        mode = "local_mode"
        print("Inside inner (Local):", mode)

    inner()
    print("Inside outer (Enclosing):", mode)

outer()
print("Outside functions (Global):", mode)