from json_utils import read_json
from pdf_service import read_pdf_accro
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
        read_pdf_accro(args.pdf)

    else :
        print("Commande invalide")
    #write_pdf_fitz()



if __name__ == "__main__":
    main()
