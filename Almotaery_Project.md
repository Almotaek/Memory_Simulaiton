# *Simulation Project*

    Author: Khalid Almotaery

    Date: 4/16/2023

In this project I developed three memory simulations: Virtual Address Organiztion , Page Table Size, and Page Table Entry Organization. The simulation is implemented in project.py.

Follow these steps to run the project:

```sh
1. In the command line, go to the directory of project.py
2. run > python3 project.py
```

The defult simulation will be Virtual Address Organiztion. However if you want to run the other simulations, you need to add the type option and the abbreviation of the desired simulation. 

For Page Table Size Simulation:

```sh
    > python3 project.py -t PTS
```
For Page Table Entry Organization Simulation:

```sh
    > python3 project.py -t PTE
```

There are other options in the simulations including:

    -h help
    -s seed value for random generation
    -c compute answers for me
    -p physical memory size
    -v virtual memory size
    -f frame/page size
    -w machine word

Regardless of the simulation you can always run the help, compute, and seed options.

Note that some options are useless for some simulations becuase of the nature of the simualtion. See the simulation sections below for more details. 

# Simulation 1: Virtual Address Organiztion Simulation

In this simulation, the program will create random virtual pages. Then it will generate random virtual addresses. The user will be asked to find the word (in hex) that is refrenced by each virtual address. 

You can:

- Change the size of the virtual memory by using the -v option
- Change the size of the page by using the -f option
- Change the size of the word by using the -w option
    - The defult word size is 8 which means answers would be in two bytes. 
    - Make sure to change it for a multiple of 8 or the program would floor it to the nearst multiple of 8.

# Simulation 2: Page Table Size Simulation

In this simulation, the program will create 6 random memory specifiactions and asks the user to find the page table size to padded to the neareast byte.

Since the program will create random specifiactions there is no need for the user to modify them in this simulation.

When -c is used, the program will produce a detailed response for each specifiactions set.

# Siumlation 3: Page Table Entry Organization Simulation

In this simulation, the program will create random physical and virtual page tables. Then, it will create a page table that translates between the two memories. The user will be asked to find physical frame that each VPN entry tranlates to.

You can:

- Change the size of the physical memory by using the -p option
- Change the size of the virtual memory by using the -v option
- Change the size of the page by using the -f option