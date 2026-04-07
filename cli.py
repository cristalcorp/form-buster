import argparse
import os

def existing_file(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"\n-> {path} n existe pas")
    return path


def build_parser():
    parser = argparse.ArgumentParser(
        description = "Complete un PDF a partir d un JSON et d un mapping"
    )

    parser.add_argument(
        "--json",
        required = True,
        help = "Chemin vers le fichier JSON d entree",
    )

    parser.add_argument(
        "--mapping",
        default = "mapping.json",
        type = existing_file,
        help = "Chemin vers le fichier de mapping (defaut: mapping.json)",
    )

    parser.add_argument(
        "--pdf",
        required = True,
        help = "Chemin vers le PDF a remplir",
    )

    subparsers = parser.add_subparsers(dest = "command", required = True)

    inspect_json_command = subparsers.add_parser(
        "inspect_json",
        help = "Inspecte un fichier JSON"
    )

    inspect_pdf_command = subparsers.add_parser(
        "inspect_pdf",
        help = "Liste les champs d un PDF"
    )

    fill_pdf_form = subparsers.add_parser(
        "fill_pdf",
        help = "Remplie les champs du PDF a partir du fichier JSON, en utilisant le fichier de mapping"
    )

    fill_pdf_position = subparsers.add_parser(
        "fill_pdf_position",
        help = "Remplie les coordonnees d un fichier PDF a partir du fichier JSON, en utilisant le fichier de mapping des coordonnees"
    )


    return parser
