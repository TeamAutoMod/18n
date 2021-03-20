import json


def flush(lang):
    with open(f"./i18n/{lang}.json", "r", encoding="utf8", errors="ignore") as f:
        strings = json.load(f)
    
    failed = 0
    for x in strings:
        try:
            strings[x] = ""
        except Exception:
            failed += 1

    with open(f"./i18n/{lang}.json", "w", encoding="utf8") as f:
        json.dump(strings, f, indent=4)
    
    print(f"Flushed {len(strings) - failed}/{len(strings)} strings from the {lang} file!")



if __name__ == "__main__":
    flush("de_DE")