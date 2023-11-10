import os

# Obtén la ruta del directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Retrocede un directorio para llegar al directorio principal (Artworks)
ruta_principal = os.path.dirname(ruta_script)

# Accede directamente a la carpeta "wikiart" en el mismo nivel que "Artworks"
ruta_wikiart = os.path.join(ruta_principal, "wikiart", "data")

print("Ruta completa a la carpeta 'data':", ruta_wikiart)
