from PIL import Image

mask_image = Image.open("C:\\Users\\acer\\Desktop\\Steganography using Python\\Images\\mask.png")

print(f"Mask Image Size : {mask_image.size}")


word_matrix_image = Image.open("C:\\Users\\acer\\Desktop\\Steganography using Python\\Images\\word_matrix.png")

print(f"Word Matrix Image Size : {word_matrix_image.size}")

mask_image_resize = mask_image.resize(word_matrix_image.size)
mask_image_resize.save("C:\\Users\\acer\\Desktop\\Steganography using Python\\Images\\resized_mask_image.png")
print(f"Mask Image Resize Dimensions : {mask_image_resize.size}. Resized image has been saved.")

resized_mask_image = Image.open("C:\\Users\\acer\\Desktop\\Steganography using Python\\Images\\resized_mask_image.png")
resized_mask_image.putalpha(150)

word_matrix_image.paste(im=resized_mask_image,box=(0,0),mask=resized_mask_image)
word_matrix_image.save("C:\\Users\\acer\\Desktop\\Steganography using Python\\Images\\deciphered_message_image.png")
print("Message has been deciphered. Image with deciphered message has been saved.")
word_matrix_image.show()
print("deciphered_messge_image.png is displayed.")


