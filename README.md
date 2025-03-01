# Ping and Traceroute Analyzer
Live Demo : [https://manasranjan1.github.io/ping_and_traceroute/](https://manasranjan1.github.io/ping_and_traceroute/)
A Python script that performs network analysis by running ping and traceroute commands on specified hosts. The script provides detailed output and logging capabilities.

## Features

- Ping multiple hosts with configurable ping count
- Perform traceroute analysis
- Cross-platform support (Windows, Linux, Mac)
- Detailed logging with timestamps
- JSON output for each analysis
- Error handling and reporting

## Requirements

- Python 3.6 or higher
- No additional Python packages required (uses standard library)
- System requirements:
  - Windows: `ping` and `tracert` commands (included by default)
  - Linux/Mac: `ping` and `traceroute` commands (may need to be installed)

## Usage

1. Run the script:
   ```bash
   python ping_analyzer.py
   ```

2. The script will:
   - Analyze predefined hosts (google.com, github.com, microsoft.com)
   - Display results in the console
   - Save detailed logs to `network_analysis.log`
   - Store JSON results in the `results` directory

## Output

The script generates two types of output:

1. Log file (`network_analysis.log`):
   - Timestamped entries for all operations
   - Complete command outputs
   - Error messages if any

2. JSON results (in `results` directory):
   - One file per host analysis
   - Contains both ping and traceroute results
   - Includes timestamps and success status
   - Structured format for easy parsing

## Customization

To analyze different hosts, modify the `hosts` list in the `main()` function:

```python
hosts = ["your-host-1.com", "your-host-2.com"]
```

## Error Handling

The script includes robust error handling for:
- Network connectivity issues
- Invalid hostnames
- Command execution failures
- File system operations

## License

This project is open source and available under the MIT License. 
