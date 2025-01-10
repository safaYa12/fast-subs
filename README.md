# fast-subs
Enumerate Subdomains fastly with python code by threading.
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

1.
2. Can Prepare your own `subdomains.txt` wordlist with potential subdomains.
3. Run the tool:
    ```bash
    python main.py
    ```
4. Enter the domain you want to enumerate subdomains for when prompted.
5. The results will be saved in a file named `<domain>_subdomains.txt`.

## Example

```bash
python main.py
