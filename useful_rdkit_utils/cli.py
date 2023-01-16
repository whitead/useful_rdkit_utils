from .ring_systems import *


@click.command()
@click.option("--mode", prompt="mode [build|search]", help="[build|search]")
@click.option("--infile", prompt="Input csv file", help="input file")
@click.option("--outfile", prompt="Output csv file", help="output file")
def main(mode, infile, outfile):
    mode_list = ["build", "search"]
    if mode not in mode_list:
        print(f"mode must be one of {mode_list}")
        sys.exit(0)
    if mode == "build":
        create_ring_dictionary(infile, outfile)
    if mode == "search":
        test_ring_system_lookup(infile, outfile)


if __name__ == "__main__":
    main()
