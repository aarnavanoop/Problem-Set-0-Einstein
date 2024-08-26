def convert_to_joules(n):
    energy = n * 300000000**2
    print(energy)


def main():
    mass = int(input("What's the mass? "))
    convert_to_joules(mass)



main()