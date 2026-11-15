default_settings = {"theme": "light", "notifications": True, "auto_save": True}
user_settings = {"theme": "dark", "notifications": False}

combined_settings = {**default_settings, **user_settings}
print("Final settings:", combined_settings)