# Getting Started
## Setting up Jupyter Hub

### Logging in
Access to the NSF Ocean Observatories Initiative (OOI) JupyterHub (https://jupyter.oceanobservatories.org), which creates encapsulated JupyterLab environments unique to each user, is available to researchers and students looking to interact with OOI data. The JupyterHub is set up to provide users with the option of using either [Python](https://www.python.org/), [R](https://www.r-project.org/), [MATLAB](https://www.mathworks.com/products/matlab.html) (users need to provide their own individual or institutional license for [MATLAB](https://www.mathworks.com/products/matlab.html)), or [Julia](https://julialang.org/) to access, explore and analyze OOI data using a high-performance computing cluster co-located with the data (both the [raw](https://rawdata.oceanobservatories.org/files/) and processed [netCDF](https://www.unidata.ucar.edu/software/netcdf/) files, which are also accessible via the [OOI Gold Copy THREDDS catalog](https://thredds.dataexplorer.oceanobservatories.org/thredds/catalog/ooigoldcopy/public/catalog.html)).

Additional information on JupyterHub and JupyterLab can be found online:
- [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/)
- [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)

If you haven’t already, request access to the JupyterHub via from the link on the login page. This will open an email that you can use to make the request. Please provide your name, the institution or program you are working with, an email address to assign to the account (see further information below), and a brief description of how you plan on using the data. 

The email account you provide when applying for access will be used to create an account for you on the JupyterHub. OOI uses [CILogon](https://cilogon.org/) to manage access to the JupyterHub (we do not maintain a database of access credentials, rather a listing of allowed users), so you need to provide an email account that is linked to a known identity provider (e.g., your home organization).

You can login to the hub using [CILogon](https://cilogon.org/) with your email account and the appropriate identity provider (use the drop-down menu in Figure 2, select your institution, and Log In). You will need to login using your home organization’s credential system. Again, OOI will not store this information and has no access to it or control over it, instead the JupyterHub will use cookies set by [CILogon](https://cilogon.org/) after you are authenticated to grant access if the account is in the allowed listing.

<p float="left">
  <img src="/imgs/jhub_ooi_login.png" alt="OOI JupyterHub login page" width="300"/>
  <img src="/imgs/jhub_cilogon.png" alt="OOI JupyterHub CILogon page" width="300"/>
</p>

For these instructions, we're going to use `conda` as our package and environment manager. 

### Get a copy of the repository on Jupyter Hub
**fork the summer school repository** On GitHub, create a personal fork of the OOI summer school repository

**create a clone of the summer school repository on jupyter hub**
in the jupyter hub terminal app, clone the repository. Replace `<git url>` with the git url for your personal forked repo. You can copy the url by clicking the green `<> Code` button on the repo home page.
<img src="/imgs/GitHub_clone.png" alt="GitHub Clone Button" width="300"/>


```bash
git clone <git url>
cd 2025-Summer-School-Acoustics
```


### Setting up Conda
We'll be using conda as the python environment manager for this summer school. The OOI JupyterHub requires some set up so that conda works. These steps only need to be completed once.

- initialize conda by running `init_conda.sh` script
    - in the terminal app, navigate to the `scripts/` directory in summer school repository. (Assuming that you are already in the repository type `cd scripts` in the terminal)
    - then run the initialization script
    ```bash
    bash init_conda.sh
    ```

```{admonition} More about the script
:class: dropdown
This bash script does the following:
- initializes bash by running the .bashrc file
- set terminal to run .bashrc at every start
- configure .condarc so it remembers and saves custom user environments
```

#### Create a conda virtual environment using 

In the terminal app in jupyter hub create the new conda environment
```bash
conda create --name ooi_acoustics
```

Install python (we'll use version 3.12)

```bash
conda install python=3.12
```

Install the Summer School repository as a python package. This will automatically install all python packages that we'll be using for the summer school.

```bash
conda activate ooi_acoustics
pip install -e .
```

Register the conda environment as a Jupyter kernel
```bash
python -m ipykernel install --user --name ooi_acoustics --display-name "Python (ooi_acoustics)"
```

Refresh your browser page so that the jupyter hub server refreshes.

Now, when you open a jupyter notebook, you can select the ipython kernel to be the conda environment that we just created. Click `Python 3 (ipykernel)` in the top right

<img src="/imgs/ipy_kernel1.png" alt="GitHub Clone Button" width="300"/>

select the dropdown, and select the environment that we just created
<img src="/imgs/ipy_kernel2.png" alt="GitHub Clone Button" width="300"/>
