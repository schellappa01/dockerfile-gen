import os

def detect_build_tool(repo_path):
    if os.path.exists(os.path.join(repo_path, 'pom.xml')):
        return 'Maven'
    elif os.path.exists(os.path.join(repo_path, 'build.gradle')):
        return 'Gradle'
    elif os.path.exists(os.path.join(repo_path, 'build.xml')):
        return 'Ant'
    else:
        raise Exception("No supported build tool detected")
