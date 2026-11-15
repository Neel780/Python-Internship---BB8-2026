admin_perms = {"read", "write", "delete", "manage_users"}
editor_perms = {"read", "write"}

action_required = "delete"
can_perform_action = action_required in editor_perms

print(f"Can editor perform '{action_required}'? {can_perform_action}")