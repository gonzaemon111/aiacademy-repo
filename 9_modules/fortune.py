# coding: UTF-8

def get_fortune():
    import random # randamではなく、randomなので注意です
    results = ["aaa", "bbb"]
    print("----")
    print("random.choice(results)", str(random.choice(results)))
    print("----")
    return random.choice(results)