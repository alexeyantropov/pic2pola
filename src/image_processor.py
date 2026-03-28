import os
from PIL import Image, ImageDraw, ImageFont, ImageFile
from loguru import logger
from const import CANVAS_WIDTH, CANVAS_HEIGHT, BORDER_W_SIZE, BORDER_H_SIZE, CAPTION_SIZE, SYSTEM_FONT, FONT_SIZE, CAPTION_LINE_SPACING

def precess_file(img_path, *, date='', geo='', hashtags='', caption='') -> str:

    '''
    Process the file to create Polaroid-style output
    
    Args:
        img_path (str): An image file path to process
        geo (str, optional): Geolocation information
        hashtags (str, optional): Comma-separated hashtags
        caption (str, optional): Additional caption
    Returns:
        str: The path of the written image
    '''

    logger.info(f'Processing file: {img_path}')
    logger.info(f'Args: date={date}, geo: {geo}, hashtags: {hashtags}, caption: {caption}')
    
    new_img_path = f'polaroid_{os.path.basename(img_path)}'
    logger.info(f'Output path: {new_img_path}')

    try:
        img = Image.open(img_path)
    except Exception as e:
        logger.critical(f'Failed to open image {img_path}:\n{e}')
        return ''

    new_img = process_image(img, date=date, geo=geo, hashtags=hashtags, caption=caption)

    try:
        new_img.save(new_img_path)
    except Exception as e:
        logger.critical(f'Failed to save image {new_img_path}:\n{e}')
        return ''

    return new_img_path


def process_image(img:ImageFile.ImageFile, *, date='', geo='', hashtags='', caption='') -> Image.Image:

    '''
    Process image to create Polaroid-style output
    
    Args:
        img_path (ImageFile): An image file to process
        geo (str, optional): Geolocation information
        hashtags (str, optional): Comma-separated hashtags
        caption (str, optional): Additional caption
    Returns:
        Image.Image: The processed image
    '''

    canvas = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT), '#ffffff')

    img_width, img_height = img.size

    target_width = CANVAS_WIDTH - 2 * BORDER_W_SIZE
    target_height = CANVAS_HEIGHT - 2 * BORDER_H_SIZE - CAPTION_SIZE

    scale_factor = max(target_width / img_width, target_height / img_height)

    scaled_width = int(img_width * scale_factor)
    scaled_height = int(img_height * scale_factor)
    img_scaled = img.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)

    crop_x = (scaled_width - target_width) // 2
    crop_y = (scaled_height - target_height) // 2
    cropped_image = img_scaled.crop((
        crop_x, 
        crop_y, 
        crop_x + target_width, 
        crop_y + target_height
    ))
    
    img_x = (CANVAS_WIDTH - target_width) // 2
    img_y = (CANVAS_HEIGHT - target_height - CAPTION_SIZE) // 2
    
    canvas.paste(cropped_image, (img_x, img_y))
    add_text_elements(canvas, date=date, geo=geo, hashtags=hashtags, caption=caption)

    return canvas


def add_text_elements(canvas:Image.Image, *, date='', geo='', hashtags='', caption=''):

    '''
    Adds text elements to the canvas
    
    Args:
        canvas (Image): Canvas to add text to
        geo (str, optional): Geolocation information
        hashtags (str, optional): Comma-separated hashtags
        caption (str, optional): Additional caption
    '''

    # Tries to use a system font or fallback to default
    try:
        font = ImageFont.truetype(SYSTEM_FONT, FONT_SIZE)
    except:
        font = ImageFont.load_default(FONT_SIZE)

    draw = ImageDraw.Draw(canvas)
    
    # Just imagine a Polaroid photo:
    canvas_width, canvas_height = canvas.size
    target_width = canvas_width - 2 * BORDER_W_SIZE
    target_height = canvas_height - 2 * BORDER_H_SIZE - CAPTION_SIZE

    img_x = (canvas_width - target_width) // 2
    img_y = (canvas_height - target_height - CAPTION_SIZE) // 2
    
    text_y_start = img_y + target_height + BORDER_H_SIZE / 2 

    # The first line = date + location
    header = ''
    if date:
        header += f'{date}'
    if geo:
        header += f', {geo}'

    if header:
        draw.text((img_x, text_y_start), f'{header}', fill='black', font=font)
        text_y_start += CAPTION_LINE_SPACING
    
    if caption:
        draw.text((img_x, text_y_start), caption, fill='black', font=font)
        text_y_start += CAPTION_LINE_SPACING

    if hashtags:
        hashtag_list = hashtags.split(',')
        # 'a,b,c' -> ['a', 'b', 'c'] -> '#a #b #c'
        hashtag_text = ' '.join(f'{tag.strip()}' for tag in hashtag_list if tag.strip())
        draw.text((img_x, text_y_start), hashtag_text, fill='black', font=font)

    return None