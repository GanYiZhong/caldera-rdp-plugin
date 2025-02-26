# Caldera RDP Plugin

A Caldera plugin for RDP attack simulation and screen capture. This plugin provides capabilities for performing RDP attacks, capturing remote desktop screenshots, and displaying results in the Caldera UI.

## Features

- RDP attack simulation using MITM techniques
- Remote desktop screen capture
- Web interface for viewing attack results
- Integration with Caldera's ability framework

## Installation

1. Clone this repository into your Caldera plugins directory:
```bash
cd /path/to/caldera/plugins
git clone https://your-repo/rdp_plugin.git
```

2. Install required dependencies:
```bash
pip install -r rdp_plugin/requirements.txt
```

3. Add the plugin to your Caldera configuration (`conf/default.yml`):
```yaml
plugins:
  - rdp_plugin
```

4. Generate SSL certificates for RDP MITM:
```bash
openssl req -x509 -newkey rsa:4096 -keyout plugins/rdp_plugin/data/key.pem -out plugins/rdp_plugin/data/cert.pem -days 365 -nodes
```

## Usage

1. Access the Caldera web interface
2. Navigate to the Abilities page
3. Look for the "RDP Attack" ability under the "lateral-movement" tactic
4. Create an operation using this ability
5. View results at `/plugin/rdp/results`

## Configuration

The plugin uses the following default settings:
- Target Port: 3389 (standard RDP port)
- Screenshot Directory: `plugins/rdp_plugin/data/screens`
- Certificate Path: `plugins/rdp_plugin/data/cert.pem`
- Private Key Path: `plugins/rdp_plugin/data/key.pem`

## Technical Details

The plugin implements:
- RDP MITM attack using PyRDP
- Screen capture functionality
- Web interface for result visualization
- Integration with Caldera's ability framework

## Security Considerations

This plugin is designed for authorized security testing only. Ensure you have proper permissions before using this tool. The plugin includes:
- SSL/TLS certificate validation
- Secure storage of captured data
- Integration with Caldera's authentication system

## Contributing

Contributions are welcome! Please submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
