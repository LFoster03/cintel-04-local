# cintel-04-local
## Action 1: Create a GitHub Project Repo
Login to GitHub. Click Repositories. Create a new project repo named cintel-04-local with a default README.md and a default .gitignore for Python. 

Add File: A useful requirements.txt

Use the GitHub web interface to add a file named requirements.txt. For best results, match the spelling and capitalization exactly - and paste in the following packages, one per line as shown below. You may add other packages as you like, for example, some may want to explore AltairLinks to an external site or other interactive chart options as well. 

 

faicons
palmerpenguins
pandas
pyarrow
plotly
seaborn
shiny
shinylive
shinywidgets
 

Add File: app.py - the main Shiny app file
Use the GitHub web interface to add a file named app.py (exactly!). Paste in the content from your P3 Shiny app.py and click Commit to save the file. 

Verify your project repo has all 4 files and that they serve their purpose well:

README.md (note the capitalization)
.gitignore (it's an unusual name, but it must be exactly this)
app.py
requirements.txt
Your code is safely stored in the cloud - you can copy from it (and improve it) as you work through this module and complete Project 4. 
## Action 2: Download Python for Windows
Step completed in past course.
## Action 3: Install Python, Add to Path, and Verify
Step completed in past course.
## Action 4: Get Help with Python Basics
[Ask ChatGPT](https://chatgpt.com/share/686d2103-ac1c-8005-b1bf-cf3ca2ea66de)
## Action 5: Clone the GitHub Repository for VS Code
cd Projects
git clone URL
cd project file path
code .
## Action 6: Virtual Environment
In a VS Code terminal in the root project folder (cintel-04-local):

Run `py -m venv .venv` to create a virtual environment in the directory named .venv.   Mac/Linux may need python3 instead. Get the spacing and folder name (.venv) exactly correct. 

py -m venv .venv
## Action 7: Activate the Virtual Environment (often)
.venv/scripts/activate
## Action 8: Install Dependencies  (as needed)
Install requirements.txt
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
## Action 9: Commit Changes
git add .
git commit -m "message"
git push

## Action 10: Build Client-Side App
We will build the app to the docs folder of our repository and test it locally.  

With your project virtual environment active in the terminal and the necessary packages installed into our .venv project virtual environment, remove any existing assets and use
 shinylive export to build the app in the penguins folder to the docs folder:


shiny static-assets remove
shinylive export penguins docs

After the app is built, serve the app locally from the docs folder to test before publishing to GitHub Pages.

In the terminal, run the following command from the root of the project folder with the project virtual environment active:


py -m http.server --directory docs --bind localhost 8008

If you get the line: code 404, message File not found
"GET /favicon.ico HTTP/1.1" 404 -

This just means your app doesn’t have a favicon.ico file in the docs/ folder. You can ignore this unless you want to add a browser tab icon.

If you want to fix it, just drop a small icon named favicon.ico into the docs/ folder.

To test: open a browser (tested with Chrome, recommended) and navigate to http://localhost:8008Links to an external site. - or whatever URL it tells you - to view the web app in the docs folder running locally.  If you make changes, refresh the page a couple times or open in an incognito tab - browsers cache (store) content for performance and changes won't always be reflected immediately. 
Git commit.

## Action 11: Publish GitHub Pages for the Repo
This is a one-time step. We need to set up your GitHub repo (in the cloud) so that it will host with GitHub Pages. 

The first time you set up an app to use Pages, navigate to the repository on GitHub and configure the settings to publish the app with GitHub Pages.
After configuring the repository once, each time you push changes to the main branch, the app will automatically update.

Go to the repository on GitHub and navigate to the **Settings** tab.
Scroll down and click the **Pages** section down the left.
Select branch main as the source for the site.
Change from the root folder to the docs folder to publish from.
Click Save and wait for the site to build.
Eventually, be patient, your app will be published and if you scroll to the top of the Pages tab, you'll see your github.io URL for the hosted web app. Copy this to your clipboard. 
Back on the main repo page, find the About section of the repo (kind of upper right).
Edit the "About" section of the repository to include a link to your hosted web app by using the Pages URL. 
When Finished

When you finish, you should have a working, unique version of a penguin dashboard that you can work with locally on your machine and have published for free on the web. It should have several inputs including a drop down to select a column for display that works and a checkbox group for species that is used to reactively filter the species shown on the charts. It should use a reactive calc to filter the dataframe and use the filtered dataframe for your tables, grids, and charts. 
## Action 12: Change Title and Add Favicon
Back on your machine, in VS Code, open the new docs folder. Edit docs/index.html - find the line that has the <title> and </title> opening and closing tags. The inner text between these two tags will appear in your tab. It's currently the same for everyone. Make this unique. 

Replace the title with your own short custom title - it will display in the browser tab when your app runs. 
Add your own custom favicon  (the little icon that appears in the web browser tab) next to the title. Try https://favicon.io/Links to an external site. and create a favicon (the little icon that appears in the web browser tab) using a bit of text (e.g. PP for popper's penguins  - or better yet, your own unique icon). Download the zip file and extract the files. Take just the favicon.ico file and paste it into your docs folder.  Two changes are required:

Confirm there is a favicon.ico in your docs folder. 
Edit docs/index.html -  Just below the title line, add the following link tag like so. This code is the same for all of us - only the favicon appearance is different. If your favicon.ico has a different name or path, let VS Code help you provide the correct path. 

    <title>PyShiny Penguins</title>
    <link rel="icon" type="image/x-icon" href="./favicon.ico">
    Git commit.