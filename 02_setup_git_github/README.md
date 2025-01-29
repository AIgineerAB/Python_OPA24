# Setup Git and Github
In this section, we will go through how to use Git and Github for version control. We will only cover the basics here which are necessary for this course. If you are interested in more features and benefits of Git, check out the links in the *Read more* section below. Follow the instructions below to get started: 

## Instructions

### 1. Installing Git in local machine
By installing Git in your local machine, you are able to perform version control on your project offline. You can also review your codes locally before pushing the changes to a remote repository available to other developers in your team. 

- download Git [here](https://git-scm.com/downloads) for your operation system
- you can check if Git is installed succesfully with the syntax below in terminal 
  
  ```console
  git --version
  ```

  <p style="text-align: center;">
  <img src="..\figures\downloadgit.png" alt="Description" width="500">
  </p>


### 2. Creating remote repository in Github 
We will be using Github to host our remote repository. This is the central codebase online where other developers in your team can access and contribute to. 

- sign up for Github [here](https://github.com) if you do not have an account in github yet
- go to *Your repositories* and click on *New* to create a new remote repository
- name the repository in this way: [course name]\_[first name]\_[family name]_[class name]. See the example below with the example name Chris Smith
- After clicking *Create repository*, your new repository will be listed under the page *Your repositories*
  <p style="text-align: center;">
  <img src="..\figures\newrepo.png" width="500">
  </p>

### 3. Basic Git commands

- `git clone`

  Now that you have created a remote repository on Github, you are ready to work on your project from your local machine. The first step is to clone the remote repository to your local machine by using its web URL. You can find the web URL in the dropdown list *Code* as below:

  <p style="text-align: center;">
  <img src="..\figures\repourl.png" width="500">
  </p>

  Create a folder, for example, called *Course*, where you would like your repository to be stored. Then, change the directory in the terminal:

  <p style="text-align: center;">
  <img src="..\figures\cd.png" width="500">
  </p>
  
  Use the command `git clone` and the web URL to clone the remote repository to the directory:

  <p style="text-align: center;">
  <img src="..\figures\clone.png" width="500">
  </p>

  Then you can find your local repository in the chosen directory:

  <p style="text-align: center;">
  <img src="..\figures\afterclone.png" width="500">
  </p>

  Note that you will be asked for the credential of your github account when cloning private repositories for the first time on your local machine.

- `git add`, `git commit` and `git status`</br>
  Normally when you are working with, for example, word files, saving means overwriting the existing files or creating new files. However, in Git, saving are broken down into two steps:
  
  `git add` will add the changes to a staging area while `git commit` will eventually make the staged changes to the local repository. You can use `git status` to track the staged changes and unstage them before commiting them to the local repository.

  Below, we have added text for chapter 1 in the .md file and commited this change.


  <p style="text-align: center;">
  <img src="..\figures\gitadd.png" width="500">
  </p>


- `git push origin main`
  
  When you are satisfied with the version of your local repository, you can update the remote repository on Github accordingly. The command `git push origin main` will serve this purpose. Here *origin* is the default name of the remote repository with the web URL used previously for cloning. Note that this name can be changed. While *main* refers to the branch you are pushing your changes to on the remote repository. After this, the changes will be reflected in the remote repository on Github: 

  <p style="text-align: center;">
  <img src="..\figures\gitpush.png" width="500">
  </p>

## Read more
-[Git repositories](https://www.geeksforgeeks.org/working-with-git-repositories/) </br>
-[Basics Git commands](https://www.atlassian.com/git/glossary#commands)



