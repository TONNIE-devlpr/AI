try:
    name = input("please tell me ur name so as a will remember u well  ")
    user = input(f"Hi! {name}, what u did today?  ").lower()
    tasks = {
        "education": ["coding", "learning", "studying", "teaching"],
        "hobbies": ["singing", "drawing", "dancing", "playing", "gaming"],
        "lifestyle": ["drinking", "smoking", "exercising", "working"]
    }
    user_type = "others"
    while user!="exit":
        for task, words in tasks.items():
            for word in words:
                if word in user:
                    user_type = task
                    break

        print(f'your task is categorized as: {user_type}')
        suggest = {
            "education": "focus on small exercises today!",
            "hobbies": "have some fun for a moment",
            "lifestyle": "take some break for it!"
        }
        print(f'my suggestion is: {suggest[user_type]}')
break
    else:
        print("byee")

except KeyError:
    print("write a suitable activity")


