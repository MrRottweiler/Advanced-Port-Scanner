import socket
import termcolor
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import sys
from datetime import datetime


class PortScanner:
    def __init__(self, timeout=1, max_workers=100):
        self.timeout = timeout
        self.max_workers = max_workers
        self.open_ports = {}
    
    def scan_port(self, target, port):
        """Scan a single port on the target"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                return (port, service)
            return None
        except socket.gaierror:
            print(termcolor.colored(f"[-] Hostname {target} could not be resolved", 'red'))
            return None
        except socket.error:
            return None
    
    def scan_target(self, target, ports):
        """Scan multiple ports on a target using multithreading"""
        print(termcolor.colored(f"\n[*] Starting scan for {target}", 'cyan'))
        print(termcolor.colored(f"[*] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 'yellow'))
        
        open_ports = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.scan_port, target, port): port 
                      for port in ports}
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    port, service = result
                    open_ports.append((port, service))
                    print(termcolor.colored(f"[+] Port {port:<6} OPEN    Service: {service}", 'green'))
        
        self.open_ports[target] = open_ports
        
        print(termcolor.colored(f"\n[*] Scan completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 'yellow'))
        print(termcolor.colored(f"[*] Found {len(open_ports)} open ports on {target}\n", 'cyan'))
        
        return open_ports
    
    def generate_report(self):
        """Generate a summary report of all scans"""
        print(termcolor.colored("\n" + "="*60, 'magenta'))
        print(termcolor.colored("SCAN SUMMARY REPORT", 'magenta', attrs=['bold']))
        print(termcolor.colored("="*60, 'magenta'))
        
        for target, ports in self.open_ports.items():
            print(termcolor.colored(f"\nTarget: {target}", 'cyan', attrs=['bold']))
            if ports:
                for port, service in sorted(ports):
                    print(f"  Port {port:<6} - {service}")
            else:
                print(termcolor.colored("  No open ports found", 'yellow'))


def parse_port_range(port_input):
    """Parse port input (e.g., '1-1000', '80,443,8080', '1-100,443,8080-8090')"""
    ports = set()
    
    for part in port_input.split(','):
        part = part.strip()
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                ports.update(range(start, end + 1))
            except ValueError:
                print(termcolor.colored(f"[-] Invalid port range: {part}", 'red'))
        else:
            try:
                ports.add(int(part))
            except ValueError:
                print(termcolor.colored(f"[-] Invalid port: {part}", 'red'))
    
    return sorted(ports)


def main():
    parser = argparse.ArgumentParser(
        description='Advanced Multi-threaded Port Scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scanner.py -t 192.168.1.1 -p 1-1000
  python scanner.py -t 192.168.1.1,192.168.1.2 -p 80,443,8080
  python scanner.py -t scanme.nmap.org -p 1-100,443,8080-8090 -w 200
        """)
    
    parser.add_argument('-t', '--targets', 
                       help='Target IP(s) or hostname(s), comma-separated')
    parser.add_argument('-p', '--ports', 
                       help='Ports to scan (e.g., 1-1000, 80,443, 1-100,8080)')
    parser.add_argument('-w', '--workers', type=int, default=100,
                       help='Number of concurrent threads (default: 100)')
    parser.add_argument('--timeout', type=float, default=1.0,
                       help='Socket timeout in seconds (default: 1.0)')
    
    args = parser.parse_args()
    
    # Interactive mode if no arguments provided
    if not args.targets:
        targets_input = input(termcolor.colored("[*] Enter target(s) to scan (comma-separated): ", 'cyan'))
    else:
        targets_input = args.targets
    
    if not args.ports:
        ports_input = input(termcolor.colored("[*] Enter ports (e.g., 1-1000, 80,443,8080): ", 'cyan'))
    else:
        ports_input = args.ports
    
    # Parse inputs
    targets = [t.strip() for t in targets_input.split(',')]
    ports = parse_port_range(ports_input)
    
    if not ports:
        print(termcolor.colored("[-] No valid ports specified", 'red'))
        sys.exit(1)
    
    # Initialize scanner
    scanner = PortScanner(timeout=args.timeout, max_workers=args.workers)
    
    # Banner
    print(termcolor.colored("\n" + "="*60, 'magenta'))
    print(termcolor.colored("       ADVANCED PORT SCANNER", 'magenta', attrs=['bold']))
    print(termcolor.colored("="*60 + "\n", 'magenta'))
    
    # Scan targets
    if len(targets) > 1:
        print(termcolor.colored(f"[*] Scanning {len(targets)} targets", 'green'))
    
    for target in targets:
        try:
            scanner.scan_target(target, ports)
        except KeyboardInterrupt:
            print(termcolor.colored("\n[!] Scan interrupted by user", 'red'))
            break
        except Exception as e:
            print(termcolor.colored(f"[-] Error scanning {target}: {str(e)}", 'red'))
    
    # Generate final report
    scanner.generate_report()


if __name__ == "__main__":
    main()
