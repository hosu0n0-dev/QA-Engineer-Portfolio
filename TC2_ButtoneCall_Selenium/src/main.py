from pathlib import Path
from test_runner import TC2Runner

def main():
    project_root = Path(__file__).resolve().parent.parent
    TC2Runner(project_root / 'output').run()

if __name__ == '__main__':
    main()
