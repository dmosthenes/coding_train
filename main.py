from TileMapMaker import CreateTileMap

tilemap = CreateTileMap()

tilemap.create_grid(size=20)
tilemap.fill_grid(tilemap.tilesets[0])
tilemap.make_image('LowResCircuit', step=56)

tilemap.create_grid(size=10)
tilemap.fill_grid(tilemap.tilesets[1])
tilemap.make_image('HighResCircuit', step=56)

tilemap.create_grid(size=35)
tilemap.fill_grid(tilemap.tilesets[2])
tilemap.make_image('GrassTiles', step=16)

tilemap.create_grid(size=10)
tilemap.fill_grid(tilemap.tilesets[3])
tilemap.make_image('Mountains', step=56)

tilemap.create_grid(size=10)
tilemap.fill_grid(tilemap.tilesets[4])
tilemap.make_image('Pipes', step=56)

tilemap.create_grid(size=10)
tilemap.fill_grid(tilemap.tilesets[5])
tilemap.make_image('PolkaDots', step=56)

tilemap.create_grid(size=10)
tilemap.fill_grid(tilemap.tilesets[6])
tilemap.make_image('Rails', step=56)