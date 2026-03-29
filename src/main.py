from loguru import logger

from args import parse_arguments
from image_processor import precess_file

def main() -> bool:

    args = parse_arguments()
    
    result = precess_file(
        args.img, date=args.date, geo=args.geo, hashtags=args.hashtags, caption=args.caption
    )
    
    if result:
        logger.info(f'The result is saved to "{result}"')
        return True
    
    logger.critical(f'Failed to process the image "{args.img}"')
    return False

if __name__ == "__main__":
    main()