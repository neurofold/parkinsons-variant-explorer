from Bio.PDB import PDBParser, Superimposer

def calculate_rmsd(pdb_file1, pdb_file2):
    parser = PDBParser(QUIET=True)
    structure1 = parser.get_structure("wt", pdb_file1)
    structure2 = parser.get_structure("mut", pdb_file2)

    atoms1 = [a for a in structure1.get_atoms() if a.get_id() == 'CA']
    atoms2 = [a for a in structure2.get_atoms() if a.get_id() == 'CA']

    if len(atoms1) != len(atoms2):
        raise ValueError("Structures have different numbers of CA atoms.")

    sup = Superimposer()
    sup.set_atoms(atoms1, atoms2)
    sup.apply(structure2.get_atoms())
    return round(sup.rms, 3)

