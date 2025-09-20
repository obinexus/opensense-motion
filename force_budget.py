def apply_force(desired_force, safe_limit, actuator_force, efficiency):
    # Clamp desired force by safety, actuator limits, and efficiency
    effective_force = efficiency * actuator_force
    return min(desired_force, safe_limit, effective_force)

# Example: cookie handling
force = apply_force(desired_force=2.0,  # Newtons wanted to hold cookie
                    safe_limit=3.0,     # cookie breaks above 3N
                    actuator_force=5.0, # motor can push 5N
                    efficiency=0.8)     # friction/cloth losses

print("Final output force:", force, "N")
