import xml.etree.ElementTree as ET

def parse_ant_build(repo_path):
    build_file = os.path.join(repo_path, 'build.xml')
    tree = ET.parse(build_file)
    root = tree.getroot()

    java_version = None  # Ant projects typically specify Java in a different way
    packaging = 'jar'  # Default for Ant, unless a WAR or EAR task is detected

    framework = None
    # Add logic to detect J2EE, Spring based on tasks or dependencies

    return java_version, packaging, framework
