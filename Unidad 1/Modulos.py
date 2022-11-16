import random;

def main(x) :
    if x > 100 :
        return;
    print(random.randint(21,2332))
    return main(x + 1);

main(97);