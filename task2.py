import os

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            cats = f.readlines()
            
        for cat in cats:
            cat = cat.strip()
            if not cat:
                continue
            try:
                cat_id, name, age = cat.split(',')
                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": int(age) 
                })
            except (ValueError, IndexError):
                print(f"Invalid data format for cat: {cat}")
                continue

    except FileNotFoundError:
        print("File not found")
        return []

    return cats_info  

cats_info = get_cats_info("cats.txt")
print(cats_info)
