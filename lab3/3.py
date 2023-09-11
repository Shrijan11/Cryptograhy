def is_primitive_root(g, p):
    if g <= 1 or g >= p:
        return False

    residues = set()
    for i in range(1, p):
        residue = pow(g, i, p)
        if residue in residues:
            return False
        residues.add(residue)

    return len(residues) == p - 1

def find_primitive_roots(p):
    primitive_roots = []
    for g in range(2, p):
        if is_primitive_root(g, p):
            primitive_roots.append(g)
    return primitive_roots

if __name__ == "__main__":
    p = int(input("Enter a prime number: "))
    primitive_roots = find_primitive_roots(p)

    if len(primitive_roots) > 0:
        print(f"The primitive roots of {p} are: {primitive_roots}")
    else:
        print(f"No primitive roots found for {p}.")