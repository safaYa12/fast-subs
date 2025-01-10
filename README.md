# fast-subs
Enumerate Subdomains fastly with python code with threading.
## Features

- Fast subdomain enumeration using `ThreadPoolExecutor`.
- Outputs discovered subdomains to a file.
- Simple to use and extend.
- ASCII banner display using `pyfiglet`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/safaYa12/fast-subs.git
    cd fast-subs
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your `subdomains.txt` wordlist with potential subdomains.
2. Run the tool:
    ```bash
    python main.py
    ```
3. Enter the domain you want to enumerate subdomains for when prompted.
4. The results will be saved in a file named `<domain>_subdomains.txt`.

## Example

```bash
python main.py
