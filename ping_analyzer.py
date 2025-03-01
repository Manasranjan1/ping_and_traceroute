import subprocess
import platform
import datetime
import json
import os
from typing import Dict, List, Optional

class NetworkAnalyzer:
    def __init__(self, log_file: str = "network_analysis.log"):
        """Initialize the Network Analyzer with a log file path."""
        self.log_file = log_file
        self.os_type = platform.system().lower()

    def _log_to_file(self, message: str) -> None:
        """Log messages to the specified log file with timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def ping(self, host: str, count: int = 4) -> Dict:
        """
        Ping the specified host and return results.
        
        Args:
            host: The host to ping
            count: Number of ping requests to send
            
        Returns:
            Dictionary containing ping results
        """
        try:
            if self.os_type == "windows":
                cmd = ["ping", "-n", str(count), host]
            else:
                cmd = ["ping", "-c", str(count), host]
            
            self._log_to_file(f"Pinging {host}...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Log the output
            self._log_to_file(result.stdout)
            
            return {
                "host": host,
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr if result.stderr else None,
                "timestamp": datetime.datetime.now().isoformat()
            }
        except Exception as e:
            error_msg = f"Error pinging {host}: {str(e)}"
            self._log_to_file(error_msg)
            return {
                "host": host,
                "success": False,
                "error": error_msg,
                "timestamp": datetime.datetime.now().isoformat()
            }

    def traceroute(self, host: str) -> Dict:
        """
        Perform a traceroute to the specified host.
        
        Args:
            host: The host to traceroute
            
        Returns:
            Dictionary containing traceroute results
        """
        try:
            # Use tracert for Windows, traceroute for Unix-like systems
            cmd = ["tracert" if self.os_type == "windows" else "traceroute", host]
            
            self._log_to_file(f"Tracerouting {host}...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Log the output
            self._log_to_file(result.stdout)
            
            return {
                "host": host,
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr if result.stderr else None,
                "timestamp": datetime.datetime.now().isoformat()
            }
        except Exception as e:
            error_msg = f"Error tracerouting {host}: {str(e)}"
            self._log_to_file(error_msg)
            return {
                "host": host,
                "success": False,
                "error": error_msg,
                "timestamp": datetime.datetime.now().isoformat()
            }

def main():
    # Create analyzer instance
    analyzer = NetworkAnalyzer()
    
    # List of hosts to analyze
    hosts = ["google.com", "github.com", "microsoft.com"]
    
    # Analyze each host
    for host in hosts:
        print(f"\nAnalyzing {host}...")
        
        # Perform ping
        ping_result = analyzer.ping(host)
        print("\nPing Results:")
        print(ping_result["output"] if ping_result["success"] else ping_result["error"])
        
        # Perform traceroute
        traceroute_result = analyzer.traceroute(host)
        print("\nTraceroute Results:")
        print(traceroute_result["output"] if traceroute_result["success"] else traceroute_result["error"])
        
        # Save results to JSON
        results = {
            "ping": ping_result,
            "traceroute": traceroute_result
        }
        
        # Create results directory if it doesn't exist
        os.makedirs("results", exist_ok=True)
        
        # Save to JSON file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"results/{host}_{timestamp}.json", "w") as f:
            json.dump(results, f, indent=4)

if __name__ == "__main__":
    main() 