import os
import json
import csv
import pickle

"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит 
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию. 
Для каждого объекта укажите файл это или директория. 
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней 
с учётом всех вложенных файлов и директорий"""
def save_directory_tree(directory):
    tree = generate_directory_tree(directory)
    save_to_json(tree, "directory_tree.json")
    save_to_csv(tree, "directory_tree.csv")
    save_to_pickle(tree, "directory_tree.pickle")


def generate_directory_tree(directory):
    tree = []
    for root, dirs, files in os.walk(directory):
        parent_dir = os.path.basename(root)
        if parent_dir:
            parent_dir = os.path.dirname(root)
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            tree.append({
                "name": file,
                "parent": parent_dir,
                "type": "file",
                "size": size
            })
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            size = get_directory_size(dir_path)
            tree.append({
                "name": dir,
                "parent": parent_dir,
                "type": "directory",
                "size": size
            })
    return tree


def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


def save_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def save_to_csv(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


save_directory_tree("test")
