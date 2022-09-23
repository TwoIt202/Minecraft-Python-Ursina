from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()


def load_asset(texture, folder):
      return load_texture(f"assets/{folder}/{texture}.png")


grass = load_asset("grass", "models")
sky = load_asset("sky", "img")



class Sky(Entity):
      def __init__(self):
            super().__init__(
                  parent=scene,
                  model='sphere',
                  scale=150,
                  texture=sky,
                  double_sided=True
            )




class Voxel(Button):
      def __init__(self, position=(0, 0, 0), texture=None):
            super().__init__(
                  parent = scene,
                  position=position,
                  model='cube',
                  origin_y = .5,
                  texture=texture,
                  color=color.color(0, 0, 255),
                  highlight_color=color.gray
            )







for z in range(25):
      for x in range(25):
            voxel = Voxel((x, 0, z), texture=grass)

player = FirstPersonController()
skyRun = Sky()

app.run()
