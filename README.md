# BurnCare (Alpha 0.1 Release)
BurnCare Training Game is designed to teach any care provider (or interested persons) from EMT up to ICU doctor the specialized treatments involved with a patient experiencing severe full thickness thermal injuries. The goal is to improve patient outcomes by providing a free, portable, specialized training simulation for care providers interested in burn care treatment. This work is a collaborative effort between Applied Research Associates Inc., and U.S Institute of Surgical Research (USISR). Our government representative is Dr. Matthew Hackett. 

## Technical Details

BurnCare is designed to run on Android OS tablets and Windows machines. The game engine is designed using Unreal 4 and supports back-end connections to the [BioGears engine](https://github.com/BioGearsEngine/core). For more documentation and details regarding BioGears visit the [website](https://www.biogearsengine.com/). For more details on the BioGears thermal injury physiology model, please read the following [paper](https://ieeexplore.ieee.org/abstract/document/8857686/).

**Note:** This is an alpha release designed for initial testing and feedback, a full release will be available *free of charge* via the Google Play store in the next 6-12 months.

The game is designed in a modular fashion where each module supports different burn specific treatment. For this Alpha release the game supports total body surface area burn estimation and escharotomy training (location, and depth). Future releases will include more modules such as: fluid resuscitation, multi-trauma, and pain management. 

## Accessing the Game
The game is pre-built and this project includes all dependencies required to run. All dependencies will be included into a single executable for the official release. To run the game navigate to 

- `Game/` 
  - `Binaries/` 
  	- `Win64/` 
	
From this folder double click (or run) the executable titled Game-Win64-Shipping.exe. This should boot the game. If you have issues please contact: abaird@ara.com.

Programmatics
===============
The BurnCare project is funded by contract number: W911NF-18-C-0037  

Disclaimer:

This work is supported by the US Army Medical Research and Materiel Command. The views, opinions and/or findings contained in this report are those of the author(s) and should not be construed as an official Department of the Army position, policy, or decision unless so designated by other documentation.


