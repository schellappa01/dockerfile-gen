import os
import xml.etree.ElementTree as ET

def parse_maven_pom(repo_path):
    pom_path = os.path.join(repo_path, 'pom.xml')
    if not os.path.exists(pom_path):
        raise Exception("POM file does not exist.")

    tree = ET.parse(pom_path)
    root = tree.getroot()

    # Get packaging
    packaging_element = root.find(".//{http://maven.apache.org/POM/4.0.0}packaging")
    packaging = packaging_element.text if packaging_element is not None else 'jar'  # Default to 'jar'

    # Get Java version
    java_version_element = root.find(".//{http://maven.apache.org/POM/4.0.0}properties/{http://maven.apache.org/POM/4.0.0}java.version")
    java_version = java_version_element.text if java_version_element is not None else '17'  # Default to 17

    # Assuming the framework is Spring Boot as it's defined in the parent
    framework = 'Spring Boot'

    return java_version, packaging, framework