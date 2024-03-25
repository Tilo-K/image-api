import cv2
import random
import os
import io


def resize_images(images):
    max_width = max(img.shape[1] for img in images)

    resized_images = [
        cv2.resize(img, (max_width, int(img.shape[0] * (max_width / img.shape[1]))))
        for img in images
    ]

    return resized_images


def combine(images):
    resized_images = resize_images(images)

    combined_image = cv2.vconcat(resized_images)

    return combined_image


def images_to_data(images):
    image_data = []

    for image in images:
        tmp_file = str(random.randint(100000, 9999999)) + ".jpg"
        image.save(tmp_file)
        img_data = cv2.imread(tmp_file)

        image_data.append(img_data)
        os.remove(tmp_file)

    return image_data


def images_to_return_data(image_data):
    combined = combine(image_data)
    tmp_file = str(random.randint(100000, 9999999)) + ".jpg"
    cv2.imwrite(tmp_file, combined, [cv2.IMWRITE_JPEG_QUALITY, 80])
    return_data = io.BytesIO()

    with open(tmp_file, "rb") as fo:
        return_data.write(fo.read())

    return_data.seek(0)
    os.remove(tmp_file)

    return return_data, tmp_file
