import requests
import time
import sys
import argparse

def print_boxed_message(message, color_code):
    """
    Prints the given message inside a box with the specified color.
    """
    message_lines = message.split('\n')
    max_length = max(len(line) for line in message_lines)
    border = '+' + '-' * (max_length + 2) + '+'
    print("\033[" + color_code + "m" + border + "\033[0m")
    for line in message_lines:
        print("\033[" + color_code + "m" + '| ' + line + ' ' * (max_length - len(line)) + ' |' + "\033[0m")
    print("\033[" + color_code + "m" + border + "\033[0m")

def check_csd_vulnerability(url):
    """
    Checks if a URL is vulnerable to Client-side desync (CSD) vulnerability.
    """
    try:
        # Send a POST request with a content length of 30 to check the response time
        start_time = time.time()
        response = requests.post(url, data={}, headers={'Content-Length': '30'}, timeout=0.5)
        end_time = time.time()

        # If the response time is less than 0.5 seconds, it's a potential CSD vulnerability
        if end_time - start_time < 0.5:
            message = f"Potential CSD Vector found at:\n{url}"
            print_boxed_message(message, "32")  # Green color code for potential CSD
        else:
            message = f"No CSD vulnerability found at:\n{url}"
            print_boxed_message(message, "31")  # Red color code for no CSD

    except requests.exceptions.RequestException as e:
        message = f"No CSD vulnerability found at:\n{url}"
        print_boxed_message(message, "31")  #aaaaaaaaaaaaaaaaaaaaaaaaaaa

def main():
    """
    SSSSSS
    """
    banner = r"""
      ________  __________     ___
  \_____  \ \____    /    /  /  /\
   /   |   \  /     /    /  /   \/
  /    |    \/     /_   (  (    /\
  \_______  /_______ \   \  \   \/
          \/        \/    \__\
"""
    print("\033[95m" + banner + "\033[0m")  # Purple color for the banner 

    powered_by = "Powered by @omarzzu - Omar Alzughaibi"
    print_boxed_message(powered_by, "95")  # Purple color code for "Powered by"

    parser = argparse.ArgumentParser(description="Client-side desync")
    parser.add_argument("-l", "--urls-file", help="Path to a file containing a list of URLs to check")
    parser.add_argument("-u", "--url", help="A single URL to check")
    args = parser.parse_args()

    if args.urls_file:
        with open(args.urls_file, "r") as f:
            urls = [url.strip() for url in f.readlines()]
        for url in urls:
            check_csd_vulnerability(url)
    elif args.url:
        check_csd_vulnerability(args.url)
    else:
        print_boxed_message("Error: You must provide either -l <file> or -u <url> to check.", "33")  # Yellow color code for error

try:
    main()
except KeyboardInterrupt:
    print_boxed_message("Scanning interrupted by the user.", "33")  # Yellow color code for error
