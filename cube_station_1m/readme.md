# Cube Station Modules

This package provides a cube variant of station modules. All production, large
habitation, large storage, administration and cross modules have their
corresponding cube variants.

* "Ugly"
* Cubes are all simple 12-triangle meshes;
* Cubes are all around the same size as Argon Cross Connection module;
* Race specific modules use textures of corresponding race;
* You have to buy these modules like vanilla ones, from corresponding races, and
  notoriety counts.
* Cubes have exactly the same specification & price as vanilla ones, except:
  - No turret
  - No shield
  - No ads
  - No eye candies

## Known issues

* Though I've roughly tested collisions, and they seem to work fine. I can't
  figure out why it complains about octree error, e.g.

        [=ERROR=] 7.47 Could not process collision mesh extensions\cube_station\assets\cube_argon_data\part_main-collision.xmf for octree generation (index buffer is corrupt)

* I've tried and failed to add icons to these cubes, so they all appear as
  unknown modules in the build plan screen.

## Development Notes

* [Help Index](https://forum.egosoft.com/viewtopic.php?f=181&t=402382)
* [A Java XML Patcher](https://forum.egosoft.com/viewtopic.php?f=181&t=407862)
* [My XML Patcher](https://github.com/eidng8/xml-patch-cli)

#### XML

* File location is not critical, though ego has their conventions.
* Macro & component template files do not need to be break up to one ware per
  file.
* Each component must has its corresponding `ANI` file.
* Each component must has its corresponding data directory, and correctly
  reference in the `source` tag.
* Be careful while filling in paths in macro & component index files.

#### Model

* Mods (including official DLC) must be patched (XML patch) to primary files to
  have any effect during mod development.
* Models, textures, etc., shall be copied over to corresponding primary location
  before actually working with them.
* References in Mods (files copied to primary locations) must be updated to
  reference primary locations.
* UV mapping in Blender can be correctly exported.
* Vertex color can be correctly exported.
* Remember not to use the Blender profile when export to DAE.

##### Samples

Use [XRConverter](https://forum.egosoft.com/viewtopic.php?f=129&t=360045) to
import a split model, you'll find out the split hull texture could not be found.
The material just appears as a dark color surface. Apply the `material_library`
diff from split DLC to the primary file, then
use [XRConverter](https://forum.egosoft.com/viewtopic.php?f=129&t=360045) to
import again. Now you see the split hull material in Blender.

As of this mod, I've copied all 5 cube components & data directories
to `assets\structures\connectionmodules`, updated the the `source` tag to
reference the copy of data directory in `assets\structures\connectionmodules`.
Import & work with those copies, save back & export changed models. Copy changed
files from `assets\structures\connectionmodules` data directories, over to my
mod's data directory.

### Processes

* Just cut the vanilla meshes down, vertex by vertex, to 12-triangle boxes.

### Obstacles

Even after reading through tutorials, posts, and a lot of trial & error, I still
can't do what I want.

* Can't figure out the purpose of `modulegroups.xml`.
* Can't figure out the correspondence of `icons.xml`. Though it seems to
  correspond to macro, and I've tried to mimic the `academymod`.

#### A bit of history

These issues were abandoned or workaround has been done.

* If I delete the original mesh then add in a new box mesh, the box will be
  rendered without any color tint.
* I can't figure out how to add new textures to the game. I just want to add a
  simple colored texture to fit race visual identities.
* I can't figure out how to specify coloring of meshes. I just want to add a
  simple color tint, so I don't need to use texture at all.
