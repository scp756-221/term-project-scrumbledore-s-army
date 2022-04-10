from copy import deepcopy
import json
import subprocess

with open('tools/seating-table-items.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    demo = deepcopy(fcc_data['seating'][0])
    fcc_data['seating'].pop()
    count = 0
    for i in range(75, 1025):
        count = count + 1
        if count < 25:
            sample = deepcopy(demo)
            sample['PutRequest']['Item']['table_id']['N'] = str(i)
            fcc_data['seating'].append(sample)
        else:
            with open('utils/seating-table-items.json', 'w', encoding='utf-8') as f:
                json.dump(fcc_data, f, ensure_ascii=False, indent=4)
            count = 0
            result = subprocess.run(["cd utils && make populate-table"], shell=True, stderr=subprocess.PIPE, text=True)
            print(result)
            fcc_data['seating'] = []
