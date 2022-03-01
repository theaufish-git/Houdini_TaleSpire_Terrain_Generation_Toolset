# Houdini_TaleSpire_Terrain_Generation_Toolset
A toolset to procedurally create terrain for TaleSpire in Houdini.

## About the Toolset
This is a set of tools to aid in the creation of [TaleSpire](https://talespire.com/) Terrain 
in [SideFX Software's Houdini](https://www.sidefx.com/products/houdini/).
It is designed to let creativity flow, you can use every aspect of Houdini to help you sculpt creations for 
TaleSpire by hand or procedurally. 
At its core these tools utilize the Heightfield features of Houdini to craft landscapes so if you are 
new to Houdini learning that aspect of the software is a good start.

Houdini is a node-based procedural system so the Toolset consist of a set of Houdini Nodes called
HDA's (Houdini Digital Assets)

### Current Nodes
#### TaleSpire_Terrain
The main node for managing a terrain project, this node contains subnetworks that allow a workspace to 
craft your terrain. It is also the main interface for setting up the terrain and exporting the final results.
#### TaleSpire_Object
This node is used to import a TaleSpire Tile, Prop or Slab for use in the system. It has controls over the 
placement of these objects in regard to how they interact with other nodes like TaleSpire_Tiler and TaleSpire_Scatter.
#### TaleSpire_Biome
This node defines a Biome which controls what TaleSpire Tiles and Props get put on to the terrain. It has 
subnetworks within for defining sets of objects, rules for placing Tiles and rules for placing/scattering Props.
#### TaleSpire_Tiler
This node is used within the TaleSpire_Biome node to define what areas specific sets of tiles are placed on the terrain.
#### TaleSpire_Scatter
This node is used within the TaleSpire_Biome node to scatter props on to a terrain based on rules and masks.

## Installation
- Install Houdini 19.0.x, If you have the option in the installer I recommend installing Houdini Labs as well.
- Launch Houdini, so it creates the proper working folders then close it.
- Download and Unzip the release of this tool, put the directory wherever you want, I like to put it in
`Documents\TaleSpire\Houdini_TaleSpire_Terrain_Generation_Toolset`
- In your Houdini19.0 directory, usually located in `Documents\Houdini19.0` create a `packages\` directory and
inside that directory create a file called `HTTGT.json`. Copy the following code block in to the contents of the file
but replace the path with where you installed the toolset, make sure it points to the `packages` directory:
`..\Documents\Houdini19.0\packages\HTTGT.json`
```
{
    "package_path": "D:\Users\<username>\Documents\TaleSpire\Houdini_Terrain_Generation_Toolset\packages"
}
```


## Contact
Join us on Discord to discuss the toolset, share work and inspiration and to get the latest news.

https://discord.gg/fUp8eK2mgK