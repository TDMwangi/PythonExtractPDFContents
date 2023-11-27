# Extract image from PDF
import fitz
import PIL.Image
import io

pdf = fitz.open('document.pdf')

counter = 1

for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_image = pdf.extract_image(image[0])
        image_data = base_image['image']
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_image['ext']
        img.save(open(f'image{counter}.{extension}', 'wb'))
        counter += 1