# Selenium Example

## 1 - How open browser and specific site with Selenium?
- Setup(use in windows):
    - install choco(use power shell - admn mode):
    ```
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```
    - After install,test choco:
    ```
    choco
    ```
    - Install firefox:
    ```
    choco install firefox
    ```
    - Install Selenium and webdrivers:
        - https://community.chocolatey.org/packages?q=selenium
    ```
    choco install selenium
    choco install selenium-all-drivers
    ```

- Initial commands:
    - install selenium(prefer to use virtual env):
        ```
        pip install selenium
        ```
- refactor your code

References:
- Playlist Live de Python: https://www.youtube.com/watch?v=PHHXksljGNA&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B

- Selenium: https://selenium-python.readthedocs.io/

- Chocolatey: https://chocolatey.org/install