#!/usr/bin/env python3
"""
Politie API Console Lookup Tool
A cool command-line interface for querying the Politie API
"""

import requests
import json
import sys
from typing import Optional, Dict, Any

# API Configuration
API_BASE_URL = "http://politieapi.test/api"  # Change this to match your Laravel server URL
API_KEY = ""  # Set your API key here or use menu option 8 to configure it

# Colors for terminal output
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    WHITE = '\033[97m'

# Police ASCII Art
POLICE_ASCII = f"""
{Colors.BLUE}{Colors.BOLD}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        ██████╗  ██████╗ ██╗     ██╗████████╗██╗███████╗  ║
    ║        ██╔══██╗██╔═══██╗██║     ██║╚══██╔══╝██║██╔════╝  ║
    ║        ██████╔╝██║   ██║██║     ██║   ██║   ██║█████╗    ║
    ║        ██╔═══╝ ██║   ██║██║     ██║   ██║   ██║██╔══╝    ║
    ║        ██║     ╚██████╔╝███████╗██║   ██║   ██║███████╗  ║
    ║        ╚═╝      ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝╚══════╝  ║
    ║                                                           ║
    ║              🚔   API LOOKUP CONSOLE   🚔                ║
    ║                                                           ║
    ║        ╔═══════════════════════════════════════╗         ║
    ║        ║  🔍  Search Investigations & Records  ║         ║
    ║        ╚═══════════════════════════════════════╝         ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{Colors.END}
"""

def print_header():
    """Print the police ASCII art header"""
    print(POLICE_ASCII)

def make_request(endpoint: str) -> Optional[Dict[Any, Any]]:
    """Make a GET request to the API"""
    global API_KEY
    
    if not API_KEY:
        print(f"{Colors.RED}❌ Error: API key is not configured{Colors.END}")
        print(f"{Colors.YELLOW}💡 Please set your API key using menu option 8{Colors.END}")
        return None
    
    try:
        url = f"{API_BASE_URL}/{endpoint}"
        headers = {
            'X-API-Key': API_KEY,
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print(f"{Colors.RED}❌ Error: Could not connect to API at {API_BASE_URL}{Colors.END}")
        print(f"{Colors.YELLOW}💡 Make sure your Laravel server is running!{Colors.END}")
        return None
    except requests.exceptions.Timeout:
        print(f"{Colors.RED}❌ Error: Request timed out{Colors.END}")
        return None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            error_data = e.response.json() if e.response.content else {}
            error_msg = error_data.get('error', 'Unauthorized')
            print(f"{Colors.RED}❌ Error: {error_msg}{Colors.END}")
            print(f"{Colors.YELLOW}💡 Check your API key - it may be invalid or expired{Colors.END}")
        elif e.response.status_code == 404:
            print(f"{Colors.RED}❌ Error: Resource not found{Colors.END}")
        else:
            error_data = e.response.json() if e.response.content else {}
            error_msg = error_data.get('error', f'HTTP {e.response.status_code}')
            print(f"{Colors.RED}❌ Error: {error_msg}{Colors.END}")
        return None
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {str(e)}{Colors.END}")
        return None

def print_separator():
    """Print a visual separator"""
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")

def format_json(data: Any, indent: int = 2) -> str:
    """Format JSON data for display"""
    return json.dumps(data, indent=indent, ensure_ascii=False)

def display_investigations():
    """Display all investigations"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}📋 Fetching all investigations...{Colors.END}\n")
    data = make_request("investigations")

    if data is None:
        return

    if not data:
        print(f"{Colors.YELLOW}⚠️  No investigations found{Colors.END}")
        return

    print_separator()
    for idx, investigation in enumerate(data, 1):
        # Find title field (check common variations)
        title = (investigation.get('title') or
                investigation.get('name') or
                investigation.get('case_title') or
                investigation.get('description') or
                'No title available')

        print(f"\n{Colors.BOLD}{Colors.BLUE}Investigation #{idx}{Colors.END}")
        print(f"{Colors.WHITE}ID: {Colors.GREEN}{investigation.get('id', 'N/A')}{Colors.END}")
        print(f"{Colors.WHITE}Title: {Colors.GREEN}{title}{Colors.END}")

        print_separator()

def display_investigation_by_id(investigation_id: str):
    """Display a specific investigation by ID"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}🔍 Fetching investigation #{investigation_id}...{Colors.END}\n")
    data = make_request(f"investigations/{investigation_id}")

    if data is None:
        return

    print_separator()
    print(f"\n{Colors.BOLD}{Colors.BLUE}Investigation Details{Colors.END}\n")

    # Find title field (check common variations)
    title = (data.get('title') or
            data.get('name') or
            data.get('case_title') or
            data.get('description') or
            'No title available')

    print(f"{Colors.WHITE}ID: {Colors.GREEN}{data.get('id', 'N/A')}{Colors.END}")
    print(f"{Colors.WHITE}Title: {Colors.GREEN}{title}{Colors.END}")

    print_separator()

def display_witnesses():
    """Display all witnesses"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}👥 Fetching all witnesses...{Colors.END}\n")
    data = make_request("witnesses")

    if data is None:
        return

    if not data:
        print(f"{Colors.YELLOW}⚠️  No witnesses found{Colors.END}")
        return

    print_separator()
    for idx, witness in enumerate(data, 1):
        print(f"\n{Colors.BOLD}{Colors.BLUE}Witness #{idx}{Colors.END}")
        for key, value in witness.items():
            print(f"{Colors.WHITE}{key.replace('_', ' ').title()}: {Colors.GREEN}{value}{Colors.END}")
        print_separator()

def display_witness_by_id(witness_id: str):
    """Display a specific witness by ID"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}🔍 Fetching witness #{witness_id}...{Colors.END}\n")
    data = make_request(f"witnesses/{witness_id}")

    if data is None:
        return

    print_separator()
    print(f"\n{Colors.BOLD}{Colors.BLUE}Witness Details{Colors.END}\n")
    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{Colors.WHITE}{key.replace('_', ' ').title()}:{Colors.END}")
            for sub_key, sub_value in value.items():
                print(f"  {Colors.CYAN}  {sub_key.replace('_', ' ').title()}: {Colors.GREEN}{sub_value}{Colors.END}")
        else:
            print(f"{Colors.WHITE}{key.replace('_', ' ').title()}: {Colors.GREEN}{value}{Colors.END}")
    print_separator()

def display_people():
    """Display all people"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}👤 Fetching all people...{Colors.END}\n")
    data = make_request("people")

    if data is None:
        return

    if not data:
        print(f"{Colors.YELLOW}⚠️  No people found{Colors.END}")
        return

    print_separator()
    for idx, person in enumerate(data, 1):
        print(f"\n{Colors.BOLD}{Colors.BLUE}Person #{idx}{Colors.END}")
        for key, value in person.items():
            print(f"{Colors.WHITE}{key.replace('_', ' ').title()}: {Colors.GREEN}{value}{Colors.END}")
        print_separator()

def display_person_by_id(person_id: str):
    """Display a specific person by ID"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}🔍 Fetching person #{person_id}...{Colors.END}\n")
    data = make_request(f"people/{person_id}")

    if data is None:
        return

    print_separator()
    print(f"\n{Colors.BOLD}{Colors.BLUE}Person Details{Colors.END}\n")
    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{Colors.WHITE}{key.replace('_', ' ').title()}:{Colors.END}")
            for sub_key, sub_value in value.items():
                print(f"  {Colors.CYAN}  {sub_key.replace('_', ' ').title()}: {Colors.GREEN}{sub_value}{Colors.END}")
        else:
            print(f"{Colors.WHITE}{key.replace('_', ' ').title()}: {Colors.GREEN}{value}{Colors.END}")
    print_separator()

def show_menu():
    """Display the main menu"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║         MAIN MENU                      ║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}╠════════════════════════════════════════╣{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}1.{Colors.END} List all investigations        {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}2.{Colors.END} Get investigation by ID        {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}3.{Colors.END} List all witnesses             {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}4.{Colors.END} Get witness by ID              {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}5.{Colors.END} List all people                {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}6.{Colors.END} Get person by ID               {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}7.{Colors.END} Change API URL                {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}8.{Colors.END} Set API Key                   {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.WHITE}0.{Colors.END} Exit                          {Colors.BOLD}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}╚════════════════════════════════════════╝{Colors.END}\n")

def main():
    """Main application loop"""
    global API_BASE_URL, API_KEY
    
    # Clear screen and show header
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    
    print(f"{Colors.GREEN}🚔 Welcome to the Politie API Lookup Console!{Colors.END}")
    print(f"{Colors.YELLOW}📡 API Base URL: {Colors.BOLD}{API_BASE_URL}{Colors.END}")
    if API_KEY:
        masked_key = API_KEY[:4] + '*' * (len(API_KEY) - 8) + API_KEY[-4:] if len(API_KEY) > 8 else '*' * len(API_KEY)
        print(f"{Colors.YELLOW}🔑 API Key: {Colors.BOLD}{masked_key}{Colors.END}")
    else:
        print(f"{Colors.RED}🔑 API Key: {Colors.BOLD}Not configured{Colors.END} {Colors.YELLOW}(Use option 8 to set){Colors.END}")
    print()

    while True:
        show_menu()
        choice = input(f"{Colors.CYAN}Enter your choice: {Colors.END}").strip()

        if choice == '0':
            print(f"\n{Colors.GREEN}👮 Thank you for using Politie API Lookup! Stay safe! 👮{Colors.END}\n")
            sys.exit(0)
        elif choice == '1':
            display_investigations()
        elif choice == '2':
            investigation_id = input(f"{Colors.CYAN}Enter investigation ID: {Colors.END}").strip()
            if investigation_id:
                display_investigation_by_id(investigation_id)
        elif choice == '3':
            display_witnesses()
        elif choice == '4':
            witness_id = input(f"{Colors.CYAN}Enter witness ID: {Colors.END}").strip()
            if witness_id:
                display_witness_by_id(witness_id)
        elif choice == '5':
            display_people()
        elif choice == '6':
            person_id = input(f"{Colors.CYAN}Enter person ID: {Colors.END}").strip()
            if person_id:
                display_person_by_id(person_id)
        elif choice == '7':
            new_url = input(f"{Colors.CYAN}Enter new API base URL (e.g., http://localhost:8000/api): {Colors.END}").strip()
            if new_url:
                API_BASE_URL = new_url
                print(f"{Colors.GREEN}✅ API URL updated to: {API_BASE_URL}{Colors.END}")
        elif choice == '8':
            new_key = input(f"{Colors.CYAN}Enter API key: {Colors.END}").strip()
            if new_key:
                API_KEY = new_key
                masked_key = API_KEY[:4] + '*' * (len(API_KEY) - 8) + API_KEY[-4:] if len(API_KEY) > 8 else '*' * len(API_KEY)
                print(f"{Colors.GREEN}✅ API key updated: {masked_key}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠️  API key cannot be empty{Colors.END}")
        else:
            print(f"{Colors.RED}❌ Invalid choice. Please try again.{Colors.END}")

        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}👮 Interrupted by user. Goodbye!{Colors.END}\n")
        sys.exit(0)

