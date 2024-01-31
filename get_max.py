def get_value(file_path):
    accs = []
    nmis = []
    aris = []
    f1s = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Split the line and extract values
            values = line.split(',')
            accs.append(float(values[0].split()[2].strip()))
            nmis.append(float(values[1].split()[1].strip()))
            aris.append(float(values[2].split()[1].strip()))
            f1s.append(float(values[3].split()[1].strip()))
    return accs, nmis, aris, f1s

def get_max_metrics(file_path):
    _1, _2, _3, _4 = get_value(file_path)
    return max(_1), max(_2), max(_3), max(_4)
