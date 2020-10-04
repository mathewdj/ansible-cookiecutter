# ansible-cookiecutter
This cookiecutter template is used to bootstrap a minimal self contained ansible playbook.

## How to use this cookiecutter template file
1. Install cookiecutter
  ```pip3 cookiecutter```
2. Generate project from a cookiecutter template:
  ```cookiecutter https://github.com/sorting-mjatt/ansible-cookiecutter```
  OR local
  ```cookiecutter ${PWD}/ansible-cookiecutter```
3. Add plays to the generated project:  
  1. `cd <project name>`
  2. Add plays to playbook `tasks/darwin.yml` for mac, `tasks/debian.yml` for ubuntu or raspbian. 
  3. Run playbook `ansible-playbook test-role.yml`


## License
[GPLv3](LICENSE)
