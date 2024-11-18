from pathlib import Path

def manage_files():
    
    file_path = Path('example_file.txt')
    
    
    with file_path.open('w') as file:
        file.write("Hello, World!")
    
    
    with file_path.open('r') as file:
        content = file.read()
        print(f"File Content: {content}")
    
    
    with file_path.open('a') as file:
        file.write("\nAppended text")
    
    
    with file_path.open('r') as file:
        content = file.read()
        print(f"Updated File Content: {content}")
    
    
    file_path.unlink()
    print(f"Deleted File: {file_path}")

if __name__ == "__main__":
    manage_files()
