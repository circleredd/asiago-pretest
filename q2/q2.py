import csv
import json

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    讀取逗號分隔的 CSV，將每一列轉成 dict，然後寫出成 JSON 陣列。
    """
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)

    with open(json_path, 'w', encoding='utf-8') as f:
        # ensure_ascii=False 保留中文，indent=2 美化排版
        json.dump(rows, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    csv_to_json('activity.csv', 'activity.json')
    print("已輸出 activity.json")