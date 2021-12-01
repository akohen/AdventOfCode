import hashlib

def phase1(key, counter=0):
    while counter < 1e7:
        if hashlib.md5((key+str(counter)).encode()).hexdigest().startswith('00000'):
            return counter
        counter+=1
    return None

def phase2(key, counter=0):
    while counter < 1e7:
        if hashlib.md5((key+str(counter)).encode()).hexdigest().startswith('000000'):
            return counter
        counter+=1
    return None

if __name__ == "__main__":
    KEY = "ckczppom"

    print(f"Phase 1: {phase1(KEY)}")
    print(f"Phase 2: {phase2(KEY)}")
