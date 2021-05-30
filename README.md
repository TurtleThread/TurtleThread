# TurtleThread
TurtleTread is a Python library inspired by [TurtleStitch](https://www.turtlestitch.org/). The goal of TurtleThread is to provide an easy-to-use turtle based interface to making embroidery patterns and learn about Python programming and art. To accomplish this, we use the excellent [PyEmbroidery](https://github.com/EmbroidePy/pyembroidery) library, which implements all the embroidery specific logic (e.g. exporting the patterns as embroidery files).

## Lisense
The code is licensed under a GPLv3 license, which means that you can use it for anything you'd like. However, if you use it to make your own tools, your tool must be open source and licensed with the GPLv3 license. For more information, see this [guide](https://www.gnu.org/licenses/quick-guide-gplv3.en.html).

## Installation
TurtleThread is available on PyPI, so it can be pip installed easily by writing

```bash
pip install turtlethread
```

In a terminal window. Alternatively, to install the latest development version, you can install directly from GitHub

```bash
pip install git+https://github.com/marieroald/turtlethread.git
```

## Development
TurtleThread is developed by Marie Roald and Yngve Mardal Moe. It is still under development, so we appreciate any issues about eventual bugs you may encounter. We are also happy for community contributions, so if you want to add some functionality, then we encourage you to describe it in an issue and submit a pull request with the feature.

## Examples
```python
from turtlethread import Turtle

pen = Turtle()
with pen.running_stitch(stitch_length=20):
    for side in range(4):
        pen.forward(80)
        pen.right(90)

with pen.jump_stitch():
    pen.forward(160)

with pen.running_stitch(stitch_length=20):
    for side in range(3):
        pen.forward(80)
        pen.right(120)

pen.save("pattern.png")
pen.save("pattern.jef")
```

## TODO
There are a few features we currently do not support but aim to in the future.

 * Other stitches like zig-zag or satin stitch
 * Text
 * Filled dots
 * Visualisation with Turtle graphics
