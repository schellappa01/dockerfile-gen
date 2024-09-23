import argparse
from clone_repo import clone_repository
from detect_build_tool import detect_build_tool
from parse_maven import parse_maven_pom
from parse_gradle import parse_gradle_build
from parse_ant import parse_ant_build
from parse_config_files import parse_application_config
from generate_dockerfile import generate_dockerfile_with_ai

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Automated Dockerfile Generator Utility")
    parser.add_argument('--git-url', type=str, help='Git URL of the project repository')
    parser.add_argument('--local-path', type=str, help='Local path to the project repository')
    
    
    args = parser.parse_args()

    if args.git_url:
        repo_path = clone_repository(args.git_url)
    elif args.local_path:
        repo_path = args.local_path
    else:
        raise Exception("Either --git-url or --local-path must be provided")

    # Detect build tool
    build_tool = detect_build_tool(repo_path)

    # Parse relevant build file
    if build_tool == 'Maven':
        java_version, packaging, framework = parse_maven_pom(repo_path)
    elif build_tool == 'Gradle':
        java_version, packaging, framework = parse_gradle_build(repo_path)
    elif build_tool == 'Ant':
        java_version, packaging, framework = parse_ant_build(repo_path)
    else:
        raise Exception("Unsupported build tool or project structure")

    # Extract optional configurations like ports
    port = parse_application_config(repo_path)

    print('Port : ',port)

    # Generate Dockerfile using Azure OpenAI
    dockerfile = generate_dockerfile_with_ai(java_version, packaging, framework, port)
    
    # Output Dockerfile
    with open(f"{repo_path}/Dockerfile", "w") as f:
        f.write(dockerfile)
    print(f"{dockerfile}")

if __name__ == "__main__":
    main()
