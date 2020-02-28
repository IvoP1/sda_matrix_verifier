# Verify SDA fabric switches versions

Simple way of verifying deployed switch versions agaisnt the compatibility matrix

## Requirements

- Python3
- pip3 install -r requirements.txt

## Usage

Clone this repository, install the required libraries, and run.

```python
python3 verifier.py username password url dna_version
```

## Example
```bash
ivpinto@IVPINTO-M-K16Y sda_matrix_verifier % python3 verifier.py devnetuser 'Cisco123!' 'https://sandboxdnac.cisco.com/' 1.2.2 
Unsupported Version; Hostname: cat_9k_1.abc.inc Current version: 16.6.4a
Unsupported Version; Hostname: cat_9k_2.abc.inc Current version: 16.6.4a
Unsupported Version; Hostname: cs3850.abc.inc Current version: 16.6.2s

ivpinto@IVPINTO-M-K16Y sda_matrix_verifier % python3 verifier.py devnetuser 'Cisco123!' 'https://sandboxdnac.cisco.com/' 1.3.1.4
Correct version: cat_9k_1.abc.inc
Correct version: cat_9k_2.abc.inc
Unsupported Version; Hostname: cs3850.abc.inc Current version: 16.6.2s
```

We can see the devices cat_9k_1.abc.inc/cat_9k_2.abc.inc running version 16.6.4a are not supported on DNAC version 1.2.2 but is supported on version 1.3.1.4

## Considerations

- Script is not taking into consideration the device role
- Not all device types are supported (e.g. extended nodes)