# Usage of sz2-scanner

This document provides comprehensive examples for using the **sz2-scanner** tool, which helps you effectively scan and analyze your projects.

## Command-Line Options

### General Syntax

```bash
sz2-scanner [options]
```

### Available Options

- `-h`, `--help`: Display help information.
- `-v`, `--version`: Show the current version of the tool.
- `-i <path>`, `--input <path>`: Specify the input file or directory to scan.
- `-o <path>`, `--output <path>`: Specify the output file where results will be saved.
- `-s`, `--scan-type <type>`: Choose the type of scan to perform. Options: `quick`, `full`, `custom`.

## Scanning Scenarios

### Basic Scan
To perform a basic scan of a directory:
```bash
sz2-scanner -i /path/to/your/project/
```

### Specifying Output
To specify an output file for the scan results:
```bash
sz2-scanner -i /path/to/your/project/ -o results.json
```

### Running a Full Scan
To run a comprehensive scan:
```bash
sz2-scanner -i /path/to/your/project/ -s full
```

## Output Format Explanations

The results can be output in several formats, including JSON and XML. For JSON format:

- Each result is represented as an object with keys: `file`, `issues`, `severity`.
- Example:
```json
[
  {
    "file": "src/example.js",
    "issues": [
      { "issue": "Unused variable", "severity": "warning" }
    ]
  }
]
```

For XML format:

- The structure contains a root element with "file" elements:
```xml
<results>
  <file path="src/example.js">
    <issue severity="warning">Unused variable</issue>
  </file>
</results>
```

### Conclusion

This guide provides the necessary information to utilize the sz2-scanner tool effectively. For more details, visit our [official documentation](http://example.com/docs).