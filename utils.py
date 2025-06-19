def read_fasta(file):
    lines = file.read().decode("utf-8").splitlines()
    return ''.join(line.strip() for line in lines if not line.startswith(">"))
