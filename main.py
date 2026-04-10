from json_utils import read_json
from pdf_service import read_pdf_acro
from fill_engine import fill_pdf_acro
from cli import build_parser


def main():
    print("""
          ###############
          # JSON -> PDF #
          ###############
          \n""")

    parser = build_parser()
    args = parser.parse_args()

    if args.command == "inspect_json":
        print(f"Inspection du fichier JSON : {args.json}")
        read_json(args.json)

    elif args.command == "inspect_pdf":
        print(f"Liste des champs du fichier PDF : {args.pdf}")
        read_pdf_acro(args.pdf)

    elif args.command == "fill_pdf":
        print(f"Remplissage du PDF {args.pdf} depuis le fichier {args.json}")
        fill_pdf_acro(args.json, args.mapping, args.pdf, args.output)

    else :
        print("Commande invalide")
    #write_pdf_fitz()



if __name__ == "__main__":
    main()
