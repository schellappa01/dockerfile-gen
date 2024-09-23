import re
import os

def parse_gradle_build(repo_path):
    gradle_path = os.path.join(repo_path, 'build.gradle')
    with open(gradle_path, 'r') as file:
        content = file.read()

    java_version = re.search(r'sourceCompatibility\s*=\s*["\'](\d+)["\']', content).group(1) if 'sourceCompatibility' in content else None
    packaging = 'war' if 'war' in content else 'jar'
    
    framework = None
    if 'org.springframework.boot' in content:
        framework = "Spring Boot"
    elif 'spring-webmvc' in content:
        framework = "Spring MVC"
    elif 'javax.servlet' in content:
        framework = "J2EE"

    return java_version, packaging, framework
