# Cube Station Modules

This package provides a cube variant of station modules. All production, large
habitation, large storage, administration and cross modules have their
corresponding cube variants.

* "Ugly"
* Cubes are all simple 12-triangle meshes;
* Cubes are all around the same size as Argon Cross Connection module;
* Race specific modules use textures of corresponding race;
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

Even after reading through tutorials, posts, and a lot of trial & error, I still
can't do what I want.

* If I delete the original mesh then add in a new box mesh, the box will be
  rendered without any color tint.
* I can't figure out how to add new textures to the game. I just want to add a
  simple colored texture to fit race visual identities.
* I can't figure out how to specify coloring of meshes. I just want to add a
  simple color tint, so I don't need to use texture at all.
* Due to above issues, I just cut the vanilla meshes down, vertex by vertex, to
  12-triangle boxes.
* Can't figure out the purpose of `modulegroups.xml`.
* Can't figure out the correspondence of `icons.xml`. Though it seems to
  correspond to macro, and I tried to mimic the `academymod`.
