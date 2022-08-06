import random

def get_random_color_palette():
    colorpalettes = [
        ['#f94144', '#f3722c', '#f8961e', '#f9844a', '#f9c74f', '#90be6d', '#43aa8b', '#4d908e', '#577590', '#277da1'],
        ["#001219", "#005f73", "#0a9396", "#94d2bd", "#e9d8a6", "#ee9b00", "#ca6702", "#bb3e03", "#ae2012", "#9b2226"],
        ["#012a4a", "#013a63", "#01497c", "#014f86", "#2a6f97", "#2c7da0", "#468faf", "#61a5c2", "#89c2d9", "#a9d6e5"],
        ["#03071e", "#370617", "#6a040f", "#9d0208", "#d00000", "#dc2f02", "#e85d04", "#f48c06", "#faa307", "#ffba08"],
        ["#7400b8", "#6930c3", "#5e60ce", "#5390d9", "#4ea8de", "#48bfe3", "#56cfe1", "#64dfdf", "#72efdd", "#80ffdb"]
    ]
    random.shuffle(colorpalettes)
    return colorpalettes[0]
