# Setup Python
In this section, we will go through steps to set up python and related tools in your local machine. The target is to use Visual Studio Code as the code editor to work on jupyter notebooks under a virutal environment. The demo below is using windows OS, but there are additional notes for differences in mac OS. 

## Video 
**Installing python on windows part 1** </br>
<a href="https://youtu.be/dteU94PSNoQ" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/python_videos/setup_part1.png?raw=true" alt="python setup part 1" width="600">
</a>

**Installing python on windows part 2**</br>
<a href="https://youtu.be/Lkr6yRUCHbA" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/python_videos/setup_part2.png?raw=true" alt="python setup part 1" width="600">
</a>


## Instructions

### 1. Install Python

Before you start, check if you have python and its package manager installed with command prompt:
<img src="https://github.com/kokchun/assets/blob/main/install_python/check_window.png?raw=true" alt="dbeaver navigation">

> ## 🍎 For macOS:
> ![DBeaver Navigation](https://github.com/kokchun/assets/blob/main/install_python/check_mac.png?raw=true)

If you do not have python installed, download it by choosing your desired python version and the correct OS:
<img src="https://github.com/kokchun/assets/blob/main/install_python/downloadpython.png?raw=true" alt="dbeaver navigation">

During installation, choose to add python.exe to PATH. This is for easily running python scripts and installing python packages without citing the location of the python executable.
<img src="https://github.com/kokchun/assets/blob/main/install_python/path(1).png?raw=true" alt="dbeaver navigation">

Additionally for mac OS, you need to double click the file called *Install Certificates.command* under *Application* folder after installation. This is to avoid issues with SSL that python can encounter, for instance, when installing packages from the internet. 
> ## 🍎 For macOS:
> ![DBeaver Navigation](https://github.com/kokchun/assets/blob/main/install_python/installcert.png?raw=true)

### 2. Install VS Code

Then, download and install VS Code from online by choosing the correct OS. 
<img src="https://github.com/kokchun/assets/blob/main/install_python/downloadvsc.png?raw=true" alt="dbeaver navigation">

Now you can create a folder for your project under *Documents*. You can now navigate to the project in command prompt and open the project in VS Code with the syntax ```code```: 
<img src="https://github.com/kokchun/assets/blob/main/install_python/openvsc.png?raw=true" alt="dbeaver navigation">

### 3. Create virtual environment

> [!NOTE]                                                                      
> A virtual environment is an isolated environment for a specific project. Being isolated means that you can install different python libraries for each project. Furthermore, you can install different versions of the same library for different project </br>
>
> There are different ways to create virtual envrionment. In this course, we will be using *uv virtual environment*
> 
> For instance, if you have created two projects, *My first python project* and *My second python project*, you can create two virtual environments for them. This is to avoid conflicts between libraries necessary for different projects </br>
> 
> When you ```pip install [xxx]```, you are installing the library globally. A project without a virtual environment will then use the globally installed libraries </br>
>
> When you create a virtual environment for a project, and then ```uv pip install [xxx]```. The project will use the libraries installed in this virtual environment 


Here comes instructions for creating a virtual environment. You will be using uv virtual environment to manage dependencies in a project. You need to first install uv globally with command prompt: 
<img src="https://github.com/kokchun/assets/blob/main/install_python/installuv.png?raw=true" alt="dbeaver navigation">

Now you can open your project in VS Code. In the terminal of VS code, use ```uv venv``` to create an uv virutal environment for your project. You can then activate it and install *ipykernel* in the venv. 

> [!NOTE]
> A *.venv* folder is now created under your project directory. But you still need to activate this virtural environment before installing libraries into it.      

<img src="https://github.com/kokchun/assets/blob/main/install_python/venv.png?raw=true" alt="dbeaver navigation">

If you encounter an error of *uv not found* in this step, make sure that you have the python scripts directory in the environment variable in your machine: 
<img src="https://github.com/kokchun/assets/blob/main/install_python/environment_variable.png?raw=true" alt="dbeaver navigation">
<img src="https://github.com/kokchun/assets/blob/main/install_python/environment_variable_2.png?raw=true" alt="dbeaver navigation">
<img src="https://github.com/kokchun/assets/blob/main/install_python/python_paths.png?raw=true" alt="dbeaver navigation">

With *ipykernel*, you will be able to run jupyter notebooks: 

> [!NOTE]
> Alternatively, you can create a file called requirements.txt in your project directory, and list the libraries or libraries with their specific versions in the file. Then you can use the syntax below to install dependencies in your virtual environment all at once.
>  ``` console
> uv pip install -r requirements.txt
>```

> [!NOTE]
> The primary file types used to write python codes are ```.py``` and ```.ipynb``` </br>
> 
> ```.py```is the standard file type for python scripts. It can be executed directly from command line as below and imported by other python scripts
> ``` console
> python main.py
>```
> ```.ipynb``` is an jupyter notebook file. It stands for interative python notebook. It is widely used for documentation and exploratory analysis. Because it combines code, text and visualization nicely in a single file. So that we can see the outputs of different code blocks to better understanding of the entire script

<img src="https://github.com/kokchun/assets/blob/main/install_python/test.png?raw=true" alt="dbeaver navigation">









