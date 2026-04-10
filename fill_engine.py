import json
from typing import Any
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject


def load_json(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_mapping(path: str) -> dict[str, str]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_value(data: Any, path: str) -> Any:
    current = data
    for part in path.split("."):
        if "[" in part and part.endswith("]"):
            name, index = part[:-1].split("[")
            current = current[name][int(index)]
        else:
            current = current[part]
    return current


def build_pdf_field_values(
    data: dict[str, Any],
    mapping: dict[str, str],
) -> dict[str, str]:
    result: dict[str, str] = {}
    for pdf_field_name, json_path in mapping.items():
        try:
            value = get_value(data, json_path)
        except (KeyError, IndexError, TypeError):
            value = ""
        result[pdf_field_name] = "" if value is None else str(value)
    return result


def fill_pdf_form(
    template_path: str,
    output_path: str,
    field_values: dict[str, str],
) -> None:
    from pypdf.generic import create_string_object

    reader = PdfReader(template_path)
    writer = PdfWriter()
    writer.append(reader)

    def iter_fields(fields_array, parent_name=""):
        for field_ref in fields_array:
            field = field_ref.get_object()
            local_name = field.get("/T")
            full_name = f"{parent_name}.{local_name}" if parent_name and local_name else (local_name or parent_name)
            if "/Kids" in field:
                iter_fields(field["/Kids"], full_name)
            else:
                if full_name in field_values:
                    field.update({
                        NameObject("/V"): create_string_object(field_values[full_name]),
                    })

    root = writer._root_object
    if "/AcroForm" not in root:
        raise ValueError("Le PDF ne contient pas de formulaire AcroForm.")

    acroform = root["/AcroForm"].get_object()
    acroform.update({NameObject("/NeedAppearances"): BooleanObject(True)})

    if "/Fields" in acroform:
        iter_fields(acroform["/Fields"])

    with open(output_path, "wb") as f:
        writer.write(f)


def fill_pdf_acro(
    json_path: str,
    mapping_path: str,
    template_path: str,
    output_path: str,
) -> None:
    data = load_json(json_path)
    mapping = load_mapping(mapping_path)
    field_values = build_pdf_field_values(data, mapping)
    fill_pdf_form(
        template_path=template_path,
        output_path=output_path,
        field_values=field_values,
    )
