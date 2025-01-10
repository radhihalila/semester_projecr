This semester project aims to automate the process of OAI log.
The first step is to transfer the qmdl/qmdl2 files to text files, this process is done by Qcat manually, instead we automated this step.
We took screenshots of the button we use manually to transform the files, and we added a script that automates a series of interactions with the graphical interface of Qcat using the PyAutoGUI library.
We used a series of functionalities to get to this goal:
1- Locate and Interact with UI Elements:
First, the script captures screenshots to locate specific objects on the screen,       using file paths for reference images.
If an object is found, it clicks on the object. If not, it prints "Object not found."
2- Steps to automate the process:
Step 1: Locate and click the "Open Option" button.
Step 2: Locate and click the "Open File" option.
Step 3: Locate and click the "Open Button" to proceed.
Step 4: Locate and click the "Save to Text" button to initiate saving.
Step 5: Locate and click the "Save" button.
Step 6 (Optional): If a file already exists, locate and click the "Yes" button to overwrite it.

We used a timing delay between steps to ensure the elements we need to click are ready for interaction.