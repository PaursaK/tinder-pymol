import os
from pymol import cmd

# Global state
current_index = [-1]  # Mutable so it's preserved between command calls
models = []           # Will be filled with model names

# Configuration
pdb_dir = "<PATH TO CANDIDATE PDB DIRECTORY HERE>" # Directory containing candidate PDB files
colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "orange", "purple", "grey", "white"]
target_pdb = "<YOUR TARGET PATH HERE>"

# Ensure the target PDB file exists
output_dir = os.path.dirname(target_pdb)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Create directories for liked and disliked models
liked_dir = os.path.join(output_dir, "liked_models")
disliked_dir = os.path.join(output_dir, "disliked_models")
os.makedirs(liked_dir, exist_ok=True)
os.makedirs(disliked_dir, exist_ok=True)

#CLI directions
print("Welcome to MolTinder! This is a PyMOL plugin for selecting models.")
print("start by running the command: setup_models()")
print("Then, Press → or ← to like/dislike models and move onto the next model.")
print("The liked and disliked models will be saved in the same directory as the target model.")

def setup_models():
    ''' function to load the target model and candidate models into PyMOL'''

    # Load target model
    cmd.load(target_pdb, "target_model")
    cmd.show("cartoon", "target_model")
    cmd.color("white", "target_model")

    # Load and align candidates
    pdb_files = sorted(f for f in os.listdir(pdb_dir) if f.endswith(".pdb"))
    
    #iterate through the pdb files and load them
    for i, f in enumerate(pdb_files):
        path = os.path.join(pdb_dir, f)
        name = f"model_{i+1}"
        models.append(name)

        cmd.load(path, name)
        cmd.align(name, "target_model")
        cmd.color(colors[i % len(colors)], name)
        cmd.hide("cartoon", name)

    cmd.orient()
    print(f"Loaded {len(models)} models. Click into 3D panel and begin swiping on structures you like/dislike.")
    next_model() # Show the first model

def next_model():
    # Hide previous model
    if current_index[0] >= 0 and current_index[0] < len(models):
        cmd.hide("cartoon", models[current_index[0]])

    # Advance index
    current_index[0] += 1

    if current_index[0] >= len(models):
        print("No more models to show.")
        return

    name = models[current_index[0]]
    cmd.show("cartoon", name)
    cmd.orient(name)
    print(f"Showing {name}.")

def liked_model():
    ''' function to save the liked model to the liked directory'''

    if current_index[0] >= 0 and current_index[0] < len(models):
        name = models[current_index[0]]
        output_path = os.path.join(liked_dir, f"{name}.pdb")
        cmd.save(output_path, name)
        print(f"Saved liked model to: {output_path}")

    next_model() # Move to the next model

def disliked_model():
    ''' function to save the disliked model to the disliked directory'''

    if current_index[0] >= 0 and current_index[0] < len(models):
        name = models[current_index[0]]
        output_path = os.path.join(disliked_dir, f"{name}.pdb")
        cmd.save(output_path, name)
        print(f"Saved disliked model to: {output_path}")

    next_model() # Move to the next model


    next_model()

from pymol import cmd

def delayed_binding():
    ''' function to bind the left and right arrow keys to the like/dislike functions'''

    # Wait a bit before setting the key (PyMOL UI needs to be fully ready)
    import threading
    def bind():
        import time
        time.sleep(1)  # Give GUI time to initialize

        # Set key bindings
        cmd.set_key('RIGHT', lambda: liked_model())
        cmd.set_key('LEFT', lambda: disliked_model())
        print("Key binding set!")

    threading.Thread(target=bind).start()





# Register PyMOL commands
cmd.extend("setup_models", setup_models)
cmd.extend("next_model", next_model)
delayed_binding() # Set key bindings after loading
