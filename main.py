import argparse

def main():
    parser = argparse.ArgumentParser(description='Web Vulnerability Scanner Tool')
    parser.add_argument('url', type=str, help='Target URL to scan')
    parser.add_argument('--depth', type=int, default=1, help='Depth of the scan')
    parser.add_argument('--output', type=str, help='Output file for scan results')

    args = parser.parse_args()

    print(f'Scanning {args.url} with depth {args.depth}')
    # Here would go the code to perform the scanning...
    
    if args.output:
        print(f'Output will be saved to {args.output}')

if __name__ == '__main__':
    main()