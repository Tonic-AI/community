# Tonic-AI Community Contribution Guide

Welcome to the Tonic-AI Community! This guide is intended to help community members contribute to various libraries that are part of our community repository, which includes forks of repositories from other organizations.

## Getting Started

Before you begin, ensure you have Git installed on your system. If not, you can download and install it from [Git's official site](https://git-scm.com/).

### Setting Up Your Local Environment

- **Clone a Specific Folder from the Repository**

   Since our community repository contains multiple libraries, you might want to clone only the specific folder relevant to your contribution.

   ```bash
   # Initialize a new repository
   git init myrepo
   cd myrepo

   # Add the remote repository
   git remote add origin https://github.com/Tonic-AI/community.git

   # Fetch the data from the remote repository
   git fetch origin

   # Enable sparse-checkout
   git sparse-checkout init --cone

   # Set the specific directory to be checked out
   git sparse-checkout set <folder-name>

   # Pull the files from the remote repository
   git pull origin main

Replace <Your-GitHub-Username> and <folder-name> with your GitHub username and the specific folder name, respectively.

### Making Changes and Contributing

1. Create a New Branch

Always create a new branch for your changes. This keeps the main branch clean and simplifies the process of integrating your changes.

```bash
git checkout -b <your-branch-name>
```
Replace <your-branch-name> with a descriptive name for your branch.

2. Make Your Changes

With your environment set up, you're ready to make changes. Ensure that your changes are as specific as possible to the issue or feature you're addressing.

3. Commit Your Changes

After making changes, commit them to your branch.

```bash
git add .
git commit -m "A descriptive message about your changes"
```

4. Push Changes to Your Fork

Push your changes to your fork on GitHub.

```bash
git push origin <your-branch-name>
```

### Creating a Pull Request

once the changes have been pushed , Tonic-AI community members will review the changes before opening a PR to the upstream repository.

### Best Practices for Contribution

- Follow Coding Standards: Ensure your code adheres to the coding standards used in the project.
- Write Meaningful Commit Messages: Your commit messages should clearly describe what the commit achieves.
- Update Documentation: If your changes require it, update the documentation.
- Test Your Changes: Before submitting your pull request, thoroughly test your changes.

🙏🏻Thank you for contributing to the Tonic-AI community!🚀
