from grade import grade

if __name__ == "__main__":
    raw = input("Zadaj získané body: ")
    print("Výsledná známka:", grade(float(raw)))