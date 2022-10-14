import typer
from ssg.site import Site


def main(source="content", dest="dest"):
    config = {"source": source, "dest": dest}

    # print(config)
    Site(**config).build()


typer.run(main)
