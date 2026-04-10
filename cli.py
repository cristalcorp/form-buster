import argparse
import os

def existing_file(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"\n-> {path} n existe pas")
    return path

def add_inspect_json_parser(subparsers):
    parser = subparsers.add_parser("inspect_json", help = "Inspecte un JSON")
    parser.add_argument("--json", required = True, help = "Chemin vers le JSON")
    return parser

def add_inspect_pdf_parser(subparsers):
    parser = subparsers.add_parser("inspect_pdf", help = "Inspecte les champs d un fichier PDF" )
    parser.add_argument("--pdf", required = True, help = "Chemin vers le PDF")
    return parser

def add_fill_pdf_accro_parser(subparsers):
    parser = subparsers.add_parser("fill_pdf", help = "Remplie un PDF avec les donnees d un fichier JSON")
    parser.add_argument("--json", required = True, help = "Chemin vers le JSON")
    parser.add_argument("--mapping", default = "mapping.json", type = existing_file, help = "Chemin vers le fichier de mapping (defaut: mapping.json)")
    parser.add_argument("--pdf", required = True, help = "Chemin vers le PDF")
    parser.add_argument("--output", default = "output.pdf", help = "Chemin vers le fichier de sortie (defaut: output.pdf)")

def build_parser():
    parser = argparse.ArgumentParser(
        description = "Complete un PDF a partir d un JSON et d un mapping"
    )
    subparsers = parser.add_subparsers(dest = "command", required = True)
    
    add_inspect_json_parser(subparsers)
    add_inspect_pdf_parser(subparsers)
    add_fill_pdf_accro_parser(subparsers)

    return parser
