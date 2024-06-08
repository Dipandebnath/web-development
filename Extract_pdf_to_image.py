from pdf2image import convert_from_path

image=convert_from_path(r'C:\Users\user\Downloads\Argus Toluene and Xylenes Daily (2024-04-01).pdf',
                        poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

for i in range(len(image)):
    image[i].save(rf'C:\Users\user\Downloads\Argus_images\page{i}.jpg','JPEG')