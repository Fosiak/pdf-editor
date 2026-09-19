# PDF Editor

Desktop application for viewing and editing PDF documents.

The project is developed in Python with a focus on clean architecture, maintainability, testing, and learning professional software development practices.

## Features

### Currently available

- Main application window

### Planned

- [ ] Open PDF documents
- [ ] Display PDF pages
- [ ] Zoom
- [ ] Navigate between pages
- [ ] Select text
- [ ] Edit text
- [ ] Delete text
- [ ] Change text color
- [ ] Change font
- [ ] Change font size
- [ ] Bold text
- [ ] Italic text
- [ ] Merge PDF files
- [ ] Split PDF files
- [ ] Delete pages
- [ ] Reorder pages
- [ ] Rotate pages
- [ ] Undo / Redo
- [ ] Export edited PDF
- [ ] More features planned

## Tech Stack

- **Python** — application logic
- **PySide6** — desktop graphical user interface
- **PyMuPDF** — PDF processing and rendering
- **pypdf** — PDF document operations
- **pytest** — automated testing
- **PyInstaller** — application packaging

## Project Structure

```text
pdf-editor/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── __init__.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

The project structure will evolve as new functionality is implemented.

## Development

### Requirements

- Python 3.12+
- Git
- Windows 10/11

### Setup

Clone the repository:

```bash
git clone <repository-url>
cd pdf-editor
```

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

### Run the application

```powershell
py -m app.main
```

### Run tests

```powershell
py -m pytest
```

## Project Status

🚧 Early development

The application is currently under active development.

## License

License will be added later.
