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
ivpinto@IVPINTO-M-K16Y Desktop % python3 verifier.py admin 'C!sc0123' https://localhost 1.2.12
Unsupported Version; Hostname: POD3-BR-01.lab.cisco.com Current version: 16.12.1s
Unsupported Version; Hostname: POD3-FE-01.lab.cisco.com Current version: 16.12.2s
Unsupported Version; Hostname: POD3-FE-02.lab.cisco.com Current version: 16.12.2s
Unsupported Version; Hostname: POD3-FE-03.lab.cisco.com Current version: 16.12.2s
Unsupported Version; Hostname: POD3-INT-01.lab.cisco.com Current version: 16.12.2s
Verification for device type WS-C3560CX-8PT-S not supported

ivpinto@IVPINTO-M-K16Y Desktop % python3 verifier.py admin 'C!sc0123' https://localhost 1.3.0.7
Correct version: POD3-BR-01.lab.cisco.com
Unsupported Version; Hostname: POD3-FE-01.lab.cisco.com Current version: 16.12.2s
Unsupported Version; Hostname: POD3-FE-02.lab.cisco.com Current version: 16.12.2s
Unsupported Version; Hostname: POD3-FE-03.lab.cisco.com Current version: 16.12.2s
Unsupported Version; Hostname: POD3-INT-01.lab.cisco.com Current version: 16.12.2s
Verification for device type WS-C3560CX-8PT-S not supported
```

We can see the device POD3-BR-01.lab.cisco.com running version 16.12.1s is not supported on DNAC version 1.2.12 but is supported on version 1.3.0.7

## Considerations

- Script is not taking into consideration the device role
- Not all device types are supported (e.g. extended nodes)