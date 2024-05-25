import requests
import time
from colorama import init, Fore, Style
import sys
import argparse
import textwrap

# Initialize colorama
init(autoreset=True)

def banner():
    """
    Prints an eye-catching banner for CSD Detective.
    """
    print(Fore.MAGENTA + r"""
╔═════════════════════════════════════════════════════════════════╗
║                                                                 ║
║                     OZ CSD DETECTIVE TOOL                       ║
║                     ╔═╗  ╔═╗  ╔═╗  ╔═╗  ╔═╗                     ║
║                     ║O║  ║Z║  ║:║  ║)║  ║C║                     ║
║                     ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝                     ║
║                 Powered by: @omarzzu - Omar Alzughaibi          ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

def wrap_text(text, width=65):
    """
    Wraps text for printing within a box.
    """
    return textwrap.fill(text, width=width)

def check_csd_vulnerability(url):
    """
    Checks if a URL is vulnerable to Cached Server-side Data (CSD) vulnerability.
    """
    try:
        # Send a POST request with a small Content-Length to check the response time
        start_time = time.time()
        response = requests.post(url, data={}, headers={'Content-Length': '30'}, timeout=0.1)
        end_time = time.time()

        # If the response time is less than 0.5 seconds and the status code is 200 or 302, it's a potential CSD vulnerability
        if end_time - start_time < 0.5 and response.status_code in [200, 302]:
            print(Fore.LIGHTGREEN_EX + "╔═════════════════════════════════════════╗")
            print(Fore.LIGHTGREEN_EX + "║  Potential CSD vulnerability found at:  ║")
            print(Fore.LIGHTGREEN_EX + f"║ {wrap_text(url)} ║")
            print(Fore.LIGHTGREEN_EX + "╚═════════════════════════════════════════╝" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + "╔═════════════════════════════════════════╗")
            print(Fore.LIGHTRED_EX + "║       No CSD vulnerability found at:    ║")
            print(Fore.LIGHTRED_EX + f"║ {wrap_text(url)} ║")
            print(Fore.LIGHTRED_EX + "╚═════════════════════════════════════════╝" + Style.RESET_ALL)

    except (requests.exceptions.RequestException, ValueError) as e:
        error_message = str(e)
        print(Fore.LIGHTRED_EX + "╔═════════════════════════════════════════╗")
        print(Fore.LIGHTRED_EX + "║       No CSD vulnerability found at:    ║")
        print(Fore.LIGHTRED_EX + f"║ {wrap_text(url)} ║")
        print(Fore.LIGHTRED_EX + "╚═════════════════════════════════════════╝" + Style.RESET_ALL)

def main():
    """
    The main function that handles the command-line arguments and runs the checks.
    """
    banner()
    
    parser = argparse.ArgumentParser(description="OZ CSD Detective Tool - Powered by @omarzzu - Omar Alzughaibi")
    parser.add_argument("-l", "--urls-file", help="Path to a file containing a list of URLs to check")
    parser.add_argument("-u", "--url", help="A single URL to check")
    args = parser.parse_args()

    if args.urls_file:
        with open(args.urls_file, "r") as f:
            urls = [url.strip() for url in f.readlines()]
        for url in urls:
            check_csd_vulnerability(url)
            time.sleep(0.1)  # Wait for 0.1 second between checks to avoid overwhelming the target
    elif args.url:
        check_csd_vulnerability(args.url)
    else:
        print(Fore.LIGHTRED_EX + "╔═════════════════════════════════════════╗")
        print(Fore.LIGHTRED_EX + "║ Error: You must provide either -l <file> or -u <url> to check. ║")
        print(Fore.LIGHTRED_EX + "╚═════════════════════════════════════════╝" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.LIGHTYELLOW_EX + "╔═════════════════════════════════════════╗")
        print(Fore.LIGHTYELLOW_EX + "║      Scanning interrupted by the user.  ║")
        print(Fore.LIGHTYELLOW_EX + "╚═════════════════════════════════════════╝" + Style.RESET_ALL)
