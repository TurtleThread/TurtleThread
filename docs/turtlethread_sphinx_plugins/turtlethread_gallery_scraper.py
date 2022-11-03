import re
import turtlethread
from textwrap import indent

from sphinx_gallery.scrapers import (HLIST_HEADER, HLIST_IMAGE_MATPLOTLIB, figure_rst)


def turtlethread_scraper(block, block_vars, gallery_conf, **kwargs):
    image_path_iterator = block_vars["image_path_iterator"]
    image_rsts = []

    for turtle in block_vars["example_globals"].values():
        if not isinstance(turtle, turtlethread.Turtle):
            continue

        for name, pattern in turtle._gallery_patterns:
            extension = name.split(".")[-1]
            if extension.upper() not in {"PNG", "SVG"}:
                continue

            # The +1 here is because we start image numbering at 1 in filenames
            image_path = image_path_iterator.image_path.format(len(image_path_iterator) + 1)
            image_path = ".".join(image_path.split(".")[:-1]) + f".{extension}"
            image_path_iterator.paths.append(image_path)

            pattern.write(image_path)
            image_rsts.append(figure_rst([image_path], gallery_conf["src_dir"], name))
        turtle._gallery_patterns = []

    # Copied from sphinx_gallery.scrapers.matplotlib_scraper
    rst = ""
    if len(image_rsts) == 1:
        rst = image_rsts[0]
    elif len(image_rsts) > 1:
        image_rsts = [
            re.sub(r":class: sphx-glr-single-img", ":class: sphx-glr-multi-img", image) for image in image_rsts
        ]
        image_rsts = [HLIST_IMAGE_MATPLOTLIB + indent(image, " " * 6) for image in image_rsts]
        rst = HLIST_HEADER + "".join(image_rsts)
    return rst
