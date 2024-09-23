import os
import yaml

def parse_application_properties(repo_path):
    """
    Parse application.properties for configurations such as port.
    """
    properties_path = os.path.join(repo_path, 'src/main/resources/application.properties')
    
    if os.path.exists(properties_path):
        with open(properties_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('server.port'):
                return line.split('=')[1].strip()
    
    return None

def parse_application_yaml(repo_path):
    """
    Parse application.yaml or application.yml for configurations such as port.
    """
    yaml_files = [
        os.path.join(repo_path, 'src/main/resources/application.yaml'),
        os.path.join(repo_path, 'src/main/resources/application.yml')
    ]
    
    for yaml_path in yaml_files:
        if os.path.exists(yaml_path):
            with open(yaml_path, 'r') as file:
                config = yaml.safe_load(file)

            if 'server' in config and 'port' in config['server']:
                return str(config['server']['port'])
    
    return None

def parse_application_config(repo_path):
    """
    Check for either application.properties or application.yaml/yml and extract configurations like port.
    """
    # First, check for properties file
    port = parse_application_properties(repo_path)
    print('parse_application_properties port ', port)
    # If not found, check for YAML file
    if not port:
        port = parse_application_yaml(repo_path)
    
    print('parse_application_yaml port ', port)
    # Default to 8080 if no port is found
    return port if port else '8080'