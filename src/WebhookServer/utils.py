import json


def log():
    print("--------------------------")
    r = request
    print(r.method)
    print(r.base_url)

    print("--- headers")
    for h in r.headers:
        print(h)

    print("--- json")
    try:
        j = r.get_json()
        print(json.dumps(j, indent=4))
    except Exception:
        print("no json")

    print("--------------------------")
