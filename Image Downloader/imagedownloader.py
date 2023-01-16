
import bs4, requests

link = input("Input image link without http: ")

try:
    image_link = requests.get(f"https://{link}")
except:
    print("Something went wrong while downloading your image. Try again.")
else:
    img_name = input("Input image name: ")
    img_format = input("Input image format: ")
    execute = input(f"Your picture will be downloaded as {img_name}.{img_format}! Press Y to confirm your download: ").lower()

    if execute == "y":
        f = open (f"/Users/macbook/Documents/GitHub/Projetos-Python/Image Downloader/Downloads/{img_name}.{img_format}", "wb") #wb = write binary
        f.write(image_link.content)
        f.close()
    else:
        print("Download canceled.")
