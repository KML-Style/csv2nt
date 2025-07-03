import csv
import os.path as op

def format_uri_or_literal(value):
    value = value.strip()

    # URI
    if value.startswith('<') and value.endswith('>'):
        return value

    if value.startswith('http'):
        return f"<{value}>"

    # Litterals
    if '^^' in value: #(Typed litteral)
        literal, dtype = value.split('^^', 1)
        literal = literal.strip().strip('"').replace('\\', '\\\\').replace('"', '\\"')
        return f"\"{literal}\"^^<{dtype.strip('<>')}>"

    cleaned = value.strip('"').replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\n')
    return f"\"{cleaned}\""


def csv2nt(path):
    ifile = op.join(path, 'input.csv')
    ofile = op.join(path, 'output.nt')
    
    with open(ifile, newline='', encoding='utf-8') as csvfile, open(ofile, 'w', encoding='utf-8') as ntfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if len(row) < 3:
                print(f"Skipping malformed line {i+1}: {row}")
                continue

            subject, predicate, object_ = row[0], row[1], row[2]
            subject_str = format_uri_or_literal(subject)
            predicate_str = format_uri_or_literal(predicate)
            object_str = format_uri_or_literal(object_)
            ntfile.write(f"{subject_str} {predicate_str} {object_str} .\n")
