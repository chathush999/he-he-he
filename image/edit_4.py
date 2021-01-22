# By @TroJanzHEX

import pyrogram
import shutil
import cv2
import os
import io
from PIL import Image, ImageOps, ImageDraw
import numpy as np 


async def rotate_90(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rotate_90.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        await msg.edit("Processing Image...")
        src = cv2.imread(a)
        image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(edit_img_loc, image)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


async def rotate_180(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rotate_180.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        await msg.edit("Processing Image...")
        src = cv2.imread(a)
        image = cv2.rotate(src, cv2.ROTATE_180)
        cv2.imwrite(edit_img_loc, image)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


async def rotate_270(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rotate_270.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        await msg.edit("Processing Image...")
        src = cv2.imread(a)
        image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(edit_img_loc, image)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


def resize_photo(photo: str, userid: str) -> io.BytesIO:
    image = Image.open(photo)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width*scale), int(image.height*scale))
    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = io.BytesIO()
    resized_photo.name = "./DOWNLOADS" + "/" + userid + "resized.png"
    image.save(resized_photo, "PNG")
    return resized_photo


async def round_sticker(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rounded.webp"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        await msg.edit("Processing Image...")
        resized = resize_photo(a, userid)
        img = Image.open(resized).convert("RGB")
        npImage = np.array(img)
        h, w = img.size
        alpha = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)
        npAlpha = np.array(alpha)
        npImage = np.dstack((npImage, npAlpha))
        Image.fromarray(npImage).save(edit_img_loc)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_sticker(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


async def inverted(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "inverted.png"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        await msg.edit("Processing Image...")
        image = Image.open(a)
        inverted_image = ImageOps.invert(image)
        inverted_image.save(edit_img_loc)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass    
