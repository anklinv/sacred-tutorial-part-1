from experiment import ex 

C = [0.001, 0.01, 0.1, 1.0, 10]
for c in C:
    run_config = {"C" : c}
    ex.run(config_updates=run_config, options={'--comment' : "SVC_c_grid_search", '--name' : f"c_{c}"})
