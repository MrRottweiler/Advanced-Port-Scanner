# Contributing to Advanced Port Scanner

First off, thank you for considering contributing to Advanced Port Scanner! It's people like you that make this tool better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (command you ran, expected vs actual output)
- **Describe the behavior you observed**
- **Include your environment details** (OS, Python version)
- **If possible, include error messages or screenshots**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any similar features** in other tools if applicable

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure your code follows the existing style
4. Make sure your code lints (passes basic Python style checks)
5. Write a clear commit message describing your changes
6. Submit your pull request!

## Development Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/yourusername/advanced-port-scanner.git
cd advanced-port-scanner
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make your changes and test thoroughly

## Style Guidelines

### Python Style Guide

- Follow PEP 8 guidelines
- Use 4 spaces for indentation
- Maximum line length of 100 characters
- Use descriptive variable names
- Add docstrings to functions and classes
- Keep functions focused and modular

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when relevant

Example:
```
Add support for UDP port scanning

- Implement UDP socket handling
- Add --udp flag to command line arguments
- Update documentation

Fixes #123
```

## Testing

Before submitting a pull request:

1. Test your changes with various inputs
2. Verify it works on different operating systems if possible
3. Check for any new dependencies and update requirements.txt
4. Ensure no existing functionality is broken

## Feature Branches

Please use descriptive branch names:
- `feature/add-udp-scanning`
- `bugfix/timeout-error`
- `docs/update-readme`

## Questions?

Feel free to open an issue with your question, or reach out to the maintainers directly.

Thank you for contributing! 🎉
