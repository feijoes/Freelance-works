

import os
import glob
import os
import glob
import pandas as pd

def search_word_in_files(folder_path: str, target_words : list[str]):
    
    file_paths = glob.glob(os.path.join(folder_path, '**/*.txt'), recursive=True)
    results = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            file_content = file.read()
            words_found = [word for word in target_words if word.strip() in file_content and word]
            if words_found:
                results.append((file_path.split("/")[-1], words_found))

    return pd.DataFrame(results, columns=['Nombre del archivo', 'Encontrado'])
