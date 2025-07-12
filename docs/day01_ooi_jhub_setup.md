# Setting up Jupyter Hub

## Logging in
Access to the NSF Ocean Observatories Initiative (OOI) JupyterHub (https://jupyter.oceanobservatories.org), which creates encapsulated JupyterLab environments unique to each user, is available to researchers and students looking to interact with OOI data. The JupyterHub is set up to provide users with the option of using either [Python](https://www.python.org/), [R](https://www.r-project.org/), [MATLAB](https://www.mathworks.com/products/matlab.html) (users need to provide their own individual or institutional license for [MATLAB](https://www.mathworks.com/products/matlab.html)), or [Julia](https://julialang.org/) to access, explore and analyze OOI data using a high-performance computing cluster co-located with the data (both the [raw](https://rawdata.oceanobservatories.org/files/) and processed [netCDF](https://www.unidata.ucar.edu/software/netcdf/) files, which are also accessible via the [OOI Gold Copy THREDDS catalog](https://thredds.dataexplorer.oceanobservatories.org/thredds/catalog/ooigoldcopy/public/catalog.html)).

Additional information on JupyterHub and JupyterLab can be found online:
- [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/)
- [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)

You can login to the hub at https://jupyter.oceanobservatories.org using [CILogon](https://cilogon.org/) (Figure 1) with your email account and the appropriate identity provider (use the drop-down menu in Figure 2, select your institution, and Log In). You will need to login using your home organization’s credential system. Again, OOI will not store this information and has no access to it or control over it, instead the JupyterHub will use cookies set by [CILogon](https://cilogon.org/) after you are authenticated to grant access if the account is in the allowed listing.

<table style="width:100%">
  <colgroup>
    <col style="width:50%">
    <col style="width:50%">
  </colgroup>
  <tr>
    <td align="center">
      <img src="/imgs/jhub_ooi_login.png" alt="OOI JupyterHub login page" width="500"/><br/>
      <em>Figure 1. Initial login page for the OOI JupyterHub using CILogon.</em>
    </td>
    <td align="center">
      <img src="/imgs/jhub_cilogon.png" alt="OOI JupyterHub CILogon page" width="500"/><br/>
      <em>Figure 2. Selection of identity provider in CILogon;<br/>usually the user’s home institution allowing them to select<br/>and use their institution’s credential system.</em>
    </td>
  </tr>
</table>

The next step is to choose the server size and type (Figure 3). For this summer school, a “Standard” server will suffice. 

<figure>
  <img src="/imgs/jhub_server_sizes.png" alt="OOI JupyterHub server sizes" width="500"/>
  <figcaption><em>Figure 3. Selection of the server type and size.</em></figcaption>
</figure>
<br/><br/>
At this point, you should see a screen that looks like the one below in Figure 4. From the Launcher tab, select the “Terminal” launcher under the “Other” category. This is a Linux terminal running the bash shell which will be used extensively in the following examples.

<figure>
  <img src="/imgs/jhub_start_page.png" alt="OOI JupyterHub start page" width="500"/>
  <figcaption><em>Figure 4. JupyterLab session with Launcher tab on the right showing the different notebook and console options, and a file browser to the
left. The ooi directory is the third one down in the file browser on the left. This would be the only you would see the first time you set up
your JupyterHub.</em></figcaption>
</figure>


## Download the summer school repository on JupyterHub

The OOI Summer School on Acoustics will be sharing materials via a [GitHub repository](https://github.com/oceanobservatories-community/2025-Summer-School-Acoustics). Here we will be providing notebooks and instructions for participants to follow along. To download this repository into JupyterHub, we will use the `git clone` command. 

First, go to the summer school [repository](https://github.com/oceanobservatories-community/2025-Summer-School-Acoustics) and copy the URL by clicking the green `<> Code` button on the repo home page.
<figure>
<img src="/imgs/GitHub_clone.png" alt="GitHub Clone Button" width="300"/>
<figcaption><em>Figure 5. GitHub clone button offers a URL from which `git clone` can download the repository.</em></figcaption>
</figure>

Then open the JupyterHub terminal and run the commands below to 1) download the GitHub repository and 2) navigate into the downloaded repository. Replace `<git url>` with the URL you just copied.
```bash
git clone <git url>
cd 2025-Summer-School-Acoustics
```

## Setting up Conda
We'll be using `conda` as the python environment manager for this summer school. The OOI JupyterHub requires some set up so that `conda` works. These steps only need to be completed once.

- Initialize `conda` by running `init_conda.sh` script
    - In the JupyterHub terminal, navigate to the `scripts/` directory in the cloned summer school repository. (Assuming that you are already in the repository type `cd scripts` in the terminal)
    - Run the initialization script
    ```bash
    bash init_conda.sh
    ```

```{admonition} More about the script
:class: dropdown
This bash script does the following:
- Initializes bash by running the .bashrc file
- Set terminal to run .bashrc at every start
- Configure .condarc so it remembers and saves custom user environments
```

### Create a `conda` virtual environment

For testing OOI data access setup, we will be creating a `conda` virtual environment to be able to run a notebook that will load data from the [OOI Gold Copy THREDDS
catalog](https://thredds.dataexplorer.oceanobservatories.org/thredds/catalog/ooigoldcopy/public/catalog.html).

In the JupyterHub terminal, create the `conda` virtual environment by first navigating to the `environment.yml` file in the summer school repository and running the `create` command.
```bash
cd ~/2025-Summer-School-Acoustics/NoteBooks/day01_ooi_data_access
conda env create -f environment.yml
```
This will take some time. Type `y` and hit `ENTER` when prompted if you want to install any packages.

After the environment has been created, `activate` it and register it as a Jupyter kernel
```bash
conda activate ooi
python -m ipykernel install --user --name=ooi
```

## Setting up OOI data access credentials

In order to access data and/or metadata (e.g., calibration coefficients) collected from the OOI, we need to set our access credentials. Once you have your credentials set up on your computer, you do not need to re-run these commands.

- If you haven't already done so, either create a user account on the [OOI Data Portal](https://ooinet.oceanobservatories.org/) (original OOI website and API server for the OOI M2M system), or use the [CILogon](https://cilogon.org/) button with an academic or Google account (login button is towards the upper right corner of the web page) to login to the portal.
- After you login, the “Log In” text will change to your username.
- Click on your username and then on the “User Profile” element of the drop down.
- Copy and save the following values from the user profile: `API Username` and `API Token`.

Users need to create a .netrc file in their home directory to store these access credentials. Set up these access credentials by running the `setup_ooi_creds.sh` script.
- In the JupyterHub terminal, navigate to the `scripts/` directory in the cloned summer school repository
- Edit the `setup_ooi_creds.sh` script to replace `API_Username` and `API_Token` with your copied values from above. The `nano` command will help you edit
```bash
nano setup_ooi_creds.sh
```
- Run the OOI access credentials setup script
```bash
bash setup_ooi_creds.sh
```

## Running the test notebook

Now we can run the provided example notebook within the ooi-data-explorations directory to see if all the packages have been installed properly. We are done using the JupyterHub terminal and can now start using the navigation window on the left to find and open the `day01_phsen_data_access.ipynb` notebook.

<figure>
<img src="/imgs/jhub_notebook.png" alt="JupyterHub notebook" width="300"/>
<figcaption><em>Figure 6. When you open a jupyter notebook, you can select the ipython kernel to be the conda environment that we just created. Click `Python 3 (ipykernel)` in the top right.</em></figcaption>
</figure>

Change the kernel from the default `Python 3 (ipykernel)` to the `ooi` environment we created.

Jupyter notebooks allow users to have cells containing Markdown notes along with cells containing code and code outputs. Each of these can be minimized or expanded. Let's all add our names to the top of the notebook by creating a Markdown cell.

Now, let's run all the cells and see this notebook work. This notebook simply loads and plots data from the [OOI Gold Copy THREDDS catalog](https://thredds.dataexplorer.oceanobservatories.org/thredds/catalog/ooigoldcopy/public/catalog.html). The data is stored [here](https://thredds.dataexplorer.oceanobservatories.org/thredds/catalog/ooigoldcopy/public/CE01ISSM-RID16-06-PHSEND000-telemetered-phsen_abcdef_dcl_instrument/catalog.html?dataset=ooigoldcopy/public/CE01ISSM-RID16-06-PHSEND000-telemetered-phsen_abcdef_dcl_instrument/deployment0002_CE01ISSM-RID16-06-PHSEND000-telemetered-phsen_abcdef_dcl_instrument_20141010T183039-20150411T233350.nc) which is data from a pH sensor on the Oregon Inshore Surface Mooring (CE01ISSM) midwater platform (aka the Near Surface Instrument Frame, NSIF), deployed at 7 m depth (site depth is 25 m). Furthermore, this is telemetered data from Deployment 2 (October 2014 through April 2015). 

After importing the necessary packages, our notebook will first load and categorize the pH values according to quality based on a subset of QARTOD flags.

The next cell will plot the data from October 2014 through April 2015 and color code the values as red if their QARTOD flags indicated instrument failure.