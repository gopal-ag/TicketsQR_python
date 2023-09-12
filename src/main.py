from config import *
import sys

if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else 'help'

    if command == 'gen':
        agree = input('New file? (y/n) ')
        if agree == 'y':
            from excel_handler import generate_ticket_link
            generate_ticket_link(INPUT_FILE_PATH, OUTPUT_FILE_PATH, DOMAIN_NAME)

    elif command == 'server':
        from webserver import run_server
        run_server()

    elif command == 'help':
        print('Available commands:')
        print('\tadd_ticket_id')
        print('\trun_webserver')
        print('\thelp')
