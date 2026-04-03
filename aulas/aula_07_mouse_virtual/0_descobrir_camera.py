from pygrabber.dshow_graph import FilterGraph

def listar_cameras_opencv():
    graph = FilterGraph()
    # Puxa a lista exata na mesma ordem de índices do OpenCV
    cameras = graph.get_input_devices()
    
    print("\n--- Câmeras Disponíveis para o OpenCV ---")
    for indice, nome in enumerate(cameras):
        print(f"Índice OpenCV ({indice})  ->  {nome}")
    print("-----------------------------------------\n")

listar_cameras_opencv()
