import os

def get_total_salary(workers_file):
    try:
        with open(workers_file, 'r', encoding='utf-8') as f:
            workers = f.readlines()

        salaries = []
        for worker in workers:
            try:
                salary = float(worker.split(',')[1])
                salaries.append(salary)
            except (IndexError, ValueError):
                print(f"Invalid data format for worker: {worker.strip()}")
                continue

    except FileNotFoundError:
        print("File not found")
        return 0, 0

    total = int(sum(salaries))
    average = int(total / len(salaries)) if salaries else 0
    return total, average


total, average = get_total_salary("workers.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

