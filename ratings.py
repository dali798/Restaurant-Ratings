"""Restaurant rating lister."""
import sys
import random
import os

def read_file(filename):
    file_name = open(filename)
    rating = {}
    for line in file_name:
        line = line.strip("\n").split(':')
        rating[line[0]] = line[1]
    return rating

def print_rating(rating):
    sorted_keys = sorted(rating)
    for key in sorted_keys:
        print(f"{key} rating is {rating[key]}.")

def ask_user(rating):
    name = input("Add restaurant name: ").title()
    while True:
        res_score = input("Add restaurant score: ")
    
        if res_score.isdigit():
            res_score = int(res_score)
            if res_score > 0 and res_score < 6:
                rating[name] = res_score
                break
            else:
                print("input must be between 1 and 5.")
        else:
            print("invalid input.")

def update_random(rating): 
    random_rest = random.choice(list(rating.keys()))
    print(f"{random_rest} rating is {rating[random_rest]}.")
    rating[random_rest] = input("Update rating to: ")

def update_chosen(rating):
    ask_input = input("Please choose a restaurant: ")
    if rating.get(ask_input, 0) != 0:
        print(f"{ask_input} rating is {rating[ask_input]}.")
        rating[ask_input] = input("Please update rating: ")
    else:
        print("Restaurant does not exist.")

def select_choice(rating):
    while True:
        choice = input("Please enter your choice (view/add/quit/random/update/change file/upload file): ").lower().strip()
        if choice == "view":
            print_rating(rating)
        if choice == "add":
            ask_user(rating)
        if choice == "random":
            update_random(rating)
        if choice == "update":
            update_chosen(rating)
        if choice == "change file":
            choose_file()
        if choice == "upload file":
            upload_file()
        if choice == "quit":
            break
        else:
            continue

def upload_file():
    filepath = input("Enter filepath to file for upload: ")
    if os.path.isfile(filepath):
        old_filename = filepath.split("/")[-1]

        f = open(filepath)
        old_file = f.read()
        f.close()

        cwd = os.getcwd()
        print(cwd)
        new_path = cwd + "/" + old_filename

        new_file = open(new_path, "w")
        new_file.write(old_file)
        new_file.close()
        print(f"Adding {new_path}...")

def choose_file():
    directory_files = os.listdir()
    print(f"Files available: {directory_files}")
    chosen_file = input("Choose a file: ")
    scores = read_file(chosen_file)
    select_choice(scores)

choose_file()