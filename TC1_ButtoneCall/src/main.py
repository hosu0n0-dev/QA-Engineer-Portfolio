from pathlib import Path
from test_runner import TC1Runner

def main():
    project_root = Path(__file__).resolve().parent.parent
    TC1Runner(project_root / 'output').run()

if __name__ == '__main__':
    main()
