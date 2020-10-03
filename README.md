# ansible <project>

Cookiecutter Instructions
1. Replace `<project>` with your project name.
  ```
  sed 's/<project>/newprojectname/g' README.md > README.md
  sed 's/<project>/newprojectname/g' README.md > test-role.yml 
  ```
2. Add plays to playbook `tasks/main.yml`. 

## Quickstart
1. To test playbook locally:
  ```
  ansible-playbook test-role.yml
  ```

## License
[GPLv3](LICENSE)
