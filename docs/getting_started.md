# Getting Started
## Setting up Jupyter Hub
For these instructions, we're going to use conda as our package manager. 

**fork the summer school repository**

**create a clone of the summer school repository on jupyter hub**
in the jupyter hub terminal app, clone the repository. Replace `<git url>` with the git url for your personal forked repo. You can copy the url by clicking the green `<> Code` button on the repo home page.
<img src="/imgs/GitHub_clone.png" alt="GitHub Clone Button" width="300"/>


```bash
git clone <git url>
cd 2025-Summer-School-Acoustics
```

**Create a new virtual environment for the summer school**

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
