#module for extracting data

def trait(trait, path):
    """
    Given a trait in a config/info file, returns the value of the trait.
    Input: trait, path
    Output: value
    """
    with open('{}'.format(path), 'r') as f:
        for line in f:
            split = line.split('=')
            if split[0] == trait:
                return split[1].strip()
