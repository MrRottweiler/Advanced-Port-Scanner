# Advanced Port Scanner

A fast, multi-threaded port scanner built with Python. This tool allows you to scan single or multiple targets for open ports with customizable threading and timeout options.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🚀 **Multi-threaded scanning** for fast performance
- 🎯 **Multiple target support** - scan multiple hosts simultaneously
- 🔢 **Flexible port specification** - single ports, ranges, or combinations
- 🎨 **Color-coded output** for easy readability
- 📊 **Summary report** generation
- ⚙️ **Customizable settings** - adjust threads and timeout values
- 🔍 **Service detection** - identifies services running on open ports

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/advanced-port-scanner.git
cd advanced-port-scanner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Mode

Basic usage:
```bash
python scanner.py -t <target> -p <ports>
```

### Examples

Scan a single target for ports 1-1000:
```bash
python scanner.py -t 192.168.1.1 -p 1-1000
```

Scan multiple targets for specific ports:
```bash
python scanner.py -t 192.168.1.1,192.168.1.2 -p 80,443,8080
```

Scan with custom port ranges and specific ports:
```bash
python scanner.py -t scanme.nmap.org -p 1-100,443,8080-8090
```

Increase thread count for faster scanning:
```bash
python scanner.py -t 192.168.1.1 -p 1-1000 -w 200
```

Adjust timeout for slower networks:
```bash
python scanner.py -t 192.168.1.1 -p 1-1000 --timeout 2.0
```

### Interactive Mode

Run without arguments for interactive prompts:
```bash
python scanner.py
```

### Command Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--targets` | `-t` | Target IP(s) or hostname(s), comma-separated | Interactive prompt |
| `--ports` | `-p` | Ports to scan (e.g., 1-1000, 80,443) | Interactive prompt |
| `--workers` | `-w` | Number of concurrent threads | 100 |
| `--timeout` | | Socket timeout in seconds | 1.0 |

## Output

The scanner provides color-coded output:
- 🟢 **Green**: Open ports found
- 🔵 **Cyan**: General information
- 🟡 **Yellow**: Timestamps and warnings
- 🔴 **Red**: Errors
- 🟣 **Magenta**: Report headers

Example output:
```
============================================================
       ADVANCED PORT SCANNER
============================================================

[*] Starting scan for 192.168.1.1
[*] Scan started at 2024-02-13 10:30:45
[+] Port 22     OPEN    Service: ssh
[+] Port 80     OPEN    Service: http
[+] Port 443    OPEN    Service: https

[*] Scan completed at 2024-02-13 10:31:02
[*] Found 3 open ports on 192.168.1.1

============================================================
SCAN SUMMARY REPORT
============================================================

Target: 192.168.1.1
  Port 22     - ssh
  Port 80     - http
  Port 443    - https
```

## How It Works

1. **Target Resolution**: Resolves hostnames to IP addresses
2. **Port Distribution**: Divides ports across multiple threads
3. **Concurrent Scanning**: Uses ThreadPoolExecutor for parallel scanning
4. **Service Detection**: Attempts to identify services on open ports
5. **Report Generation**: Compiles results into a summary report

## Performance Tips

- **Increase workers** (`-w 200`) for faster scans on local networks
- **Decrease timeout** (`--timeout 0.5`) for faster scans on reliable networks
- **Increase timeout** (`--timeout 2.0`) for slower or remote networks
- Scan common ports first (80, 443, 22, 21, 25, etc.) before full range scans

## Legal Disclaimer

⚠️ **Important**: This tool is for educational purposes and authorized security testing only.

- Only scan systems you own or have explicit permission to test
- Unauthorized port scanning may be illegal in your jurisdiction
- The authors are not responsible for misuse of this tool

Always ensure you have proper authorization before scanning any network or system.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's `socket` and `concurrent.futures` libraries
- Color output provided by `termcolor`

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/advanced-port-scanner](https://github.com/yourusername/advanced-port-scanner)

## Roadmap

- [ ] Add support for UDP scanning
- [ ] Implement stealth scan techniques
- [ ] Add output to file (JSON, CSV, XML)
- [ ] OS detection capabilities
- [ ] Integration with vulnerability databases
- [ ] GUI interface

---

**⭐ If you find this tool useful, please consider giving it a star!**
