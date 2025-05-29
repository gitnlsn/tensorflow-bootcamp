# Installation and Setup

Chapter: 2

## Anaconda Installation and Environment Setup

This guide will walk you through setting up your development environment for the course, covering the installation of Anaconda, restoring a specific environment, and a brief introduction to Jupyter Notebook.

### 1. Downloading and Installing Anaconda

**What is Anaconda?**
Anaconda is a popular distribution of Python for data science, bundling many essential data science packages.

**Download Process:**

- Go to [**anaconda.com/download**](https://anaconda.com/download) in your browser.
- Select your operating system: **Windows**, **macOS**, or **Linux**.
- Click **Download**.

**Installation Steps:**

- **Windows & macOS:** The installer is graphical. Simply follow the on-screen prompts.
- **Linux:** Download the `.sh` installer file. You'll need to run this from your command line using `bash /path/to/installer.sh`. Detailed commands are available on the Anaconda website under "How to Install Anaconda" for Linux.

**Important Note for Installation (PATH Variable):**
During the installation process, you'll be asked whether to **add Anaconda to your PATH environment variable**.

- Anaconda **recommends against this**, as it can interfere with existing Python installations.
- **For this course, you *should* check this option.** This ensures Anaconda is your primary Python distribution for the course. If you don't, you'll have to manually add it to your PATH later.

### 2. Restoring the Course Environment File

After installing Anaconda, the next step is to restore the specific environment used for this course. This ensures you have all the correct library versions.

**Prerequisites:**

- You should have already downloaded the **course zip file** (from the FAQ or course overview lecture) and **unzipped it** to a known location on your computer. This unzipped folder will contain the `.yml` environment file.

**Opening your Command Line/Terminal:**

- **macOS/Linux:** Open your **Terminal** (search for "terminal").
- **Windows:** Open **Command Prompt** (search for "cmd") or, if you encounter issues, use the **Anaconda Prompt** (search for it). The Anaconda Prompt is particularly useful if you get "Conda not recognized" errors.

**Navigating to the Course Notes Directory:**

- Use the `cd` (change directory) command to navigate to the unzipped course notes folder.
    - To go back up a directory: `cd ..`
    - To enter a directory: `cd folder_name` (you can use **Tab** for auto-completion).
- **Verify you're in the correct directory:** Once you're in the TensorFlow bootcamp folder (or wherever your unzipped course materials are), you should be able to type `TFDL_env.yml` and hit **Tab** to auto-complete the filename. If it doesn't auto-complete, you're likely in the wrong directory.

**Creating the Environment:**

- Run the following command:
Bash
    
    `conda env create -f TF_DL_env.yml`
    
- You may be prompted to confirm installations by typing `y` and pressing Enter. This command will create an environment named `TF Deep Learning` with all the necessary libraries.

**Activating the Environment:**
Once the environment is created, you need to activate it:

- **macOS/Linux:**Bash
    
    `source activate TF_Deep_Learning`
    
- **Windows:**Bash
    
    `activate TF_Deep_Learning`
    
- You'll know it's active when you see `(TF_Deep_Learning)` at the beginning of your command line prompt.
- To deactivate the environment: `deactivate`

---

## Introduction to Jupyter Notebook

Jupyter Notebook is an interactive web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text.

### Launching Jupyter Notebook

- **Ensure your `TF_Deep_Learning` environment is active.**
- In your command line/terminal, type:
Bash
    
    `jupyter notebook`
    
- This should automatically open a new tab in your web browser. If it doesn't, copy the URL (including the token, if it's your first time) displayed in your terminal and paste it into your browser.

### Basic Jupyter Notebook Usage

**1. Creating a New Notebook:**

- In the Jupyter Notebook interface, click **New** (usually on the right side).
- Select **Python 3** (or whatever kernel is listed under "Notebook").

**2. Renaming a Notebook:**

- Click on the current name (e.g., "Untitled") at the top of the page.
- Type your desired name and click **Rename**.

**3. Understanding Cells:**

- Jupyter Notebooks are structured into **cells**. You can run code in these cells independently.
- To run a cell: **Shift + Enter**.

**4. Testing TensorFlow Installation:**

- In a new cell, type and run the following code:
Python
    
    `import tensorflow as tf
    
    hello = tf.constant("Hello world")
    sess = tf.Session()
    print(sess.run(hello))`
    
- If everything is working correctly, you should see the output `Hello world`.

**5. Cell Types (Code vs. Markdown):**

- **Code Cells:** These are the default where you write and execute Python code.
- **Markdown Cells:** You can change a cell type to "Markdown" (from the dropdown menu in the toolbar). This allows you to write notes, explanations, and formatted text using Markdown syntax (e.g., headings, italics). Run Markdown cells with **Shift + Enter** to render the text.

**6. Useful Shortcuts and Features:**

- **Tab Completion:** If you have a defined variable (e.g., `s = "a string"`), type `s.` and then press **Tab** to see a list of available methods for that variable. The variable must have been run in a previous cell for this to work.
- **Docstrings (Shift + Tab):** To view the documentation (docstring) for a function, method, or class, place your cursor inside the parentheses of the function/method call and press **Shift + Tab**. Pressing **Shift + Tab** again will expand the docstring.
- **Inserting Cells:**
    - Go to **Insert** in the menu bar.
    - Choose **Insert Cell Above** or **Insert Cell Below**.