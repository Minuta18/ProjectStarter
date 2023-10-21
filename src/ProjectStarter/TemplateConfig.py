import jinja2
import pathlib

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(pathlib.Path(__file__).parent / 'templates'),
    autoescape=True,
)