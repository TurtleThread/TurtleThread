import re
import sys
from textwrap import dedent

from sphinx.directives.code import (
    LiteralInclude,
    List,
    Node,
    nodes,
    Any,
    Dict,
)
from sphinx.application import Sphinx


def change_save_dir(code, out_dir):
    return re.sub("(\w*.save[(]['\"])(.*[)])", f"\\1{out_dir}/\\2", code)


class IncludeTurtlethread(LiteralInclude):
    """
    Like ``.. include:: :literal:``, but only warns if the include file is
    not found, and does not raise errors.  Also has several options for
    selecting what to include.
    """

    def run(self) -> List[Node]:
        document = self.state.document

        try:
            rel_filename, filename = self.env.relfn2path(self.arguments[0])
            stdout = self.create_eps_and_svg(filename)
        except Exception as exc:
            return [document.reporter.warning(exc, line=self.lineno)]

        out = super().run()
        if stdout.strip():
            stdout_node = nodes.literal_block(stdout, stdout)
            stdout_node['classes'].append("sphx-glr-script-out")
            out.append(stdout_node)

        return out

    def create_eps_and_svg(self, filename):
        from pathlib import Path
        from subprocess import run

        filename = Path(filename)
        out_dir = filename.parent / "manual_code_output"
        out_dir.mkdir(exist_ok=True)
        svg_file = out_dir / f"{filename.stem}.svg"
        eps_file = out_dir / f"{filename.stem}.eps"
        pdf_file = out_dir / f"{filename.stem}.pdf"
        stdout_file = out_dir / f"{filename.stem}.out"

        if eps_file.is_file() and svg_file.is_file() and stdout_file.is_file():
            with stdout_file.open() as f:
                stdout = f.read()

            return stdout

        with open(filename, "r") as f:
            code = f.read()

        code = code.replace(".visualise()", ".visualise(done=False, bye=False)")
        code = code.replace("__file__", f"'{filename}'")
        code = change_save_dir(code, out_dir)
        # TODO: Make sure that only one call to visualise

        save_eps_code = dedent(f"""
            s = turtle.Screen()
            s.setup(3_000, 3_000)
            turtle.update()
            s.getcanvas().postscript(file='{eps_file}')
            turtle.bye()
            """)
        code = f"import turtle\nturtle.tracer(0)\n{code}\n{save_eps_code}"
        print(f"Creating figure for {filename}")

        if not eps_file.is_file() or not stdout_file.is_file():
            output = run([sys.executable, "-c", code], capture_output=True, text=True)  # TODO: Store stdout and stderr
            stdout = output.stdout
            print(output.stderr)
            with stdout_file.open("w") as f:
                f.write(stdout)
        else:
            with stdout_file.open() as f:
                stdout = f.read()

        # We are not able to get inkscape to open EPS-files from a docker container even if ghostscript is installed
        run(["ps2pdf", "-dEPSCrop", str(eps_file), str(pdf_file)])
        run(["inkscape", str(pdf_file), "--export-area-drawing", "--export-type=svg", f"--export-filename={svg_file}"])
        return stdout


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_directive("include-turtlethread", IncludeTurtlethread)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
