# Getting Started
## Setting up Jupyter Hub

### Logging in
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
<br>
At this point, you should see a screen that looks like the one below in Figure 4. From the Launcher tab, select the “Terminal” launcher under the “Other” category. This is a Linux terminal running the bash shell which will be used extensively in the following examples.

<figure>
  <img src="/imgs/jhub_start_page.png" alt="OOI JupyterHub start page" width="500"/>
  <figcaption><em>Figure 4. JupyterLab session with Launcher tab on the right showing the different notebook and console options, and a file browser to the
left. The ooi directory is the third one down in the file browser on the left. This would be the only you would see the first time you set up
your JupyterHub.</em></figcaption>
</figure>


### Download the summer school repository on JupyterHub

The OOI Summer School on Acoustics will be sharing materials via a [GitHub repository](https://github.com/oceanobservatories-community/2025-Summer-School-Acoustics). Here we will be providing notebooks and instructions for participants to follow along. To download this repository into JupyterHub, we will use the `git clone` command. 

First, go to the summer school [repository](https://github.com/oceanobservatories-community/2025-Summer-School-Acoustics) and copy the URL by clicking the green `<> Code` button on the repo home page.
<img src="/imgs/GitHub_clone.png" alt="GitHub Clone Button" width="300"/>

Then open the JupyterHub terminal and run the commands below to 1) download the GitHub repository and 2) navigate into the downloaded repository. Replace `<git url>` with the URL you just copied.
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
