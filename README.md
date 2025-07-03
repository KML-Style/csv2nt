# CSV to N-Triples Converter

This Python script converts a CSV file of RDF triples to [N-Triples](https://www.w3.org/TR/n-triples/) format, ready for graph databases.

## Features

- **CSV input:** Each row = subject, predicate, object.
- **Automatic formatting:** URIs, literals, and typed literals supported.
- **Error handling:** Malformed lines skipped with warning.

## Usage

1. Put your CSV file as `input.csv` in the script folder.
2. Run:
    ```bash
    python csv2nt.py
    ```
3. Output will be in `output.nt`.

## CSV Format

Example:
```csv
http://example.org/A,http://example.org/predicate,"hello"
<http://example.org/B>,<http://example.org/predicate>,"42"^^<http://www.w3.org/2001/XMLSchema#integer>
```

## Requirements

Python 3.x
