# Boron Nitride Nanotubes for Genistein Drug Delivery

## Overview

This repository contains computational models, analysis files, and supporting materials related to the investigation of **boron nitride nanotubes (BNNTs) as potential nanocarriers for genistein**.

The computational work focuses on the interaction, electronic properties, and related characteristics of genistein-loaded and functionalized BNNT systems using **Density Functional Theory (DFT)** calculations performed with **BIOVIA Materials Studio / DMol³**.

The repository is organized according to the main computational analyses performed during the study.

---

## Related Publication

The files in this repository support the computational work reported in:

> Mashhoun, S., & Tavahodi, A. (2024).  
> *Boron nitride nanotubes as carriers of genistein for multitherapeutic
> cancer treatment: A DFT study of electronic and solubility properties.*  
> Frontiers in Nanotechnology, 6, 1483044.

[Read the article](https://doi.org/10.3389/fnano.2024.1483044)

---

## Research Objectives

The computational study investigates BNNT-based systems for potential applications in nanomedicine and drug delivery, with particular emphasis on:

* Modeling pristine and functionalized BNNT structures.
* Investigating the interaction between BNNTs and genistein.
* Studying different BNNT configurations and tube sizes.
* Examining Fe-doped BNNT systems.
* Analyzing electronic and molecular properties of the studied systems.
* Investigating thermodynamic and kinetic properties relevant to genistein release.

---

## Systems Studied

The repository includes computational work involving:

* `(5,5)` BNNT
* `(6,6)` BNNT
* `(7,7)` BNNT
* Fe-doped BNNT systems
* Genistein-loaded BNNT systems

These models were investigated to examine how nanotube structure and functionalization affect the properties of the resulting systems.

---

## Computational Methods

The calculations and analyses are based primarily on **Density Functional Theory (DFT)** using the following approaches:

* **PBE-GGA** exchange-correlation functional
* **DNP** basis set
* **Spin-unrestricted calculations**
* **Mulliken population analysis**
* **Hirshfeld population analysis**
* **Fukui function analysis**
* Electronic structure analysis
* Thermodynamic and kinetic analysis

---

## Software

The computational workflow primarily uses:

* **BIOVIA Materials Studio**
* **DMol³**
* **Python**

Materials Studio and DMol³ were used for molecular modeling and quantum-mechanical calculations, while Python was used for supporting data processing and analysis where applicable.

---

## Repository Structure

```text
Dmol3_materials-studio-setting/
│
├── Cosmo_Surfaces/
│   └── COSMO surface and related analysis files
│
├── DOS/
│   └── Density of States (DOS) analysis
│
├── Figures/
│   └── Figures, plots, and graphical results
│
├── Materials_Studio_Dmol3_Original_Setup/
│   └── Original DMol³ calculation and Materials Studio setup files
│
├── Sigma_Profiles/
│   └── Sigma-profile related computational data and analysis
│
├── TS_and_Release_Kinetics/
│   └── Transition-state and genistein release kinetics analysis
│
└── README.md
```

Each directory corresponds to a specific part of the computational workflow or analysis.

---

## Main Analyses

### Density of States (DOS)

The DOS directory contains files and analyses related to the electronic density of states of the investigated systems.

### COSMO Surfaces

The Cosmo_Surfaces directory contains computational files related to COSMO surface analysis and the characterization of the studied molecular systems.

### Sigma Profiles

The Sigma_Profiles directory contains files associated with sigma-profile analysis.

### Transition States and Release Kinetics

The TS_and_Release_Kinetics directory contains computational files and analyses related to transition states and the kinetics of genistein release from the investigated systems.

### DMol³ Setup

The Materials_Studio_Dmol3_Original_Setup directory contains the original Materials Studio / DMol³ setup and computational files used during the study.
 
---

## Research Context

This repository supports computational research on BNNT-based drug delivery systems, with genistein used as the investigated therapeutic molecule.

The computational analysis is intended to provide insight into the structural, electronic, and energetic characteristics of the investigated BNNT–genistein systems.
 
---

## Note

This repository is intended to document the computational models, analysis files, and supporting materials associated with the research project. The repository does not contain proprietary Materials Studio software or software licenses.
