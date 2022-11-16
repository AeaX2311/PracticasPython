"""
    Una pizzeria ofrece los siguientes ingredientes
    Vegetarianos:
    - Pimiento
    - Tofu
    No Vegetarianos:
    - Prperoni
    - Jamon
    - Salmon

    Escribir un programa, que pregunte si quiere una vegetariana o no, en base a la respuesta muestre el menu
    Solo se puede elegir un ingrediente ademas del ingrediente defecto, mozarella y tomate.
    Al final debe mostrar todos los ingredientes
"""

from pickletools import read_unicodestringnl


def pizzaVegana() :
    print("+---------------------------------------------");
    print("Pizza vegana")
    print("[1] Pimiento");
    print("[2] Tofu");
    sel = input("Seleccione su ingrediente extra: ");
    print("+---------------------------------------------");

    if sel == "1" :
        return "Pimiento";
    else :
        return "Tofu";

def pizzaNoVegana() :
    print("+---------------------------------------------");
    print("Pizza no vegana")
    print("[1] Peperoni");
    print("[2] Jamon");
    print("[3] Salmon")
    sel = input("Seleccione su ingrediente extra: ");
    print("+---------------------------------------------");

    if sel == "1" :
        return "Peperoni";
    elif sel == "2" :
        return "Jamon";
    else :
        return "Salmon";

def main() :
    print("+---------------------------------------------");
    print("Pizzeria El Alansillo")
    print("Que tipo de pizza desea llevar en esta ocasion?");
    print("[1] - Vegana");
    print("[2] - No vegana");
    sel = input("Seleccione el tipo: ");
    print("+---------------------------------------------");

    return sel;

pizza = main();
if(pizza == "1") :
    ing = pizzaVegana();
elif(pizza == "2") :
    ing = pizzaNoVegana();

if ing != None :
    print("+---------------------------------------------");
    print("Su pizza contiene:");
    print("Mozarella, Tomate y", ing);
    print("Gracias por su compra!");
    print("+---------------------------------------------");


