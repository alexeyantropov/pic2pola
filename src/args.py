import argparse

def parse_arguments() -> argparse.Namespace:

    '''
    Parses command-line arguments for the pic2pola application.
    '''

    parser = argparse.ArgumentParser(
            description='Convert a picture into a Polaroid-style photo with optional captions.'            
    )
    
    parser.add_argument('--img',      required=True, help='Path to the input image file.')
    parser.add_argument('--date',     default='', help='Date of the event.')
    parser.add_argument('--geo',      default='', help='Geolocation information (e.g. "Paris, France"')
    parser.add_argument('--hashtags', default='', help='Comma-separated list of hashtags (e.g. "vacation,travel,photo")')
    parser.add_argument('--caption',  default='', help='Additional caption text')

    return parser.parse_args()