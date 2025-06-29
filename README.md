# Minecraft-UUID-Fetcher

A simple Python script to retrieve the UUID of a Minecraft user by their nickname using Mojang's official API.

## Opportunities

- Get UUID of any Minecraft player by nickname.
- Output the UUID to the console.
- Detect and display if the player does not exist.

## Requirements

- Python 3.6 or higher  
- Modules from the standard library: `sys`, external: `requests`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IVSamDev/Minecraft-UUID-Fetcher.git
   ```
2. Make sure you have Python 3.6+ installed:

   ````bash
   python3 --version
   ````

## Usage

```bash
python3 uuid.py <username>
```

### Attributes (parameters)

| Option           | Description                                    | Commitment      | Possible values       |
| ---------------- | ---------------------------------------------- | --------------- | --------------------- |
| `username`       | Minecraft player nickname                      | **necessarily** | `Notch, Dream, etc.`  |

### Examples

Get the UUID of a player and display it in the console:

   ```bash
   python3 uuid.py Notch
   ```

Output:

   ````bash
   UUID for nickname Notch: 069a79f444e94726a5befca90e38aaf5
   ````

Player not found:

   ````bash
   python3 uuid.py SomeRandomIGN
   ````

Output:

   ````bash
   The player with the nickname SomeRandomIGN not found.
   ````

## License

MIT License © IVSamDev

