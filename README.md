# Control instruments with GPIB

## Installation

- Install Anaconda
    - Check "Add Anaconda3 to my PATH environment variable" during installation
- Open anaconda powershell prompt and activate environment
    - ```conda create -n pyvisa python=3.11```
    - ```conda activate pyvisa```
    - ```conda config --add channels conda-forge```
    - ```conda install pyvisa```
- Install VSCode to use conda environment
    - If you have activated a conda environment, you should be able to select it as your interpreter in VSCode.  

## Instruments

### Advantest R6144

Programmable DV voltage/current generator.
