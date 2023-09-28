import pydicom
import sys


def pprint_dcm(dcm: pydicom.Dataset, _index=("1")):
    """
    Human readable dcmdump (see dcmtk)
    """
    def _get_line(element):
        description = element.name if element.is_private else element.keyword
        value = element.value
        tag = f"{element.VR} {element.tag}"
        tpe = type(value).__name__
        offset = " " * (40 - len(description))
        return description, value, tag, tpe, offset

    if dcm.get("file_meta") is not None:
        print("---------------------------")
        pprint_dcm(dcm.file_meta)
        print("---------------------------")
    for element in dcm:
        desc, val, tag, tpe, offset = _get_line(element)
        ntab = "\t" * (len(_index) - 1)
        if isinstance(val, pydicom.sequence.Sequence):
            n = len(val)
            print(f"{tag} {ntab}{desc}({n})")
            for j, subdcm in enumerate(val):
                if desc == "ContentSequence":
                    ref = ".".join(_index) + f".{j+1} "
                    ref += "-" * (15 - len(ref))
                    print(f"{ref} {ntab}   {j+1}")
                else:
                    ref = "---------------"
                pprint_dcm(subdcm, (*_index, str(j + 1)))
        elif isinstance(val, str):
            print(f"{tag} {ntab}{desc}{offset}\t{val}")
        elif isinstance(val, bytes):
            print(f"{tag} {ntab}{desc}{offset}\t<{tpe}>")
        else:
            print(f"{tag} {ntab}{desc}{offset}\t{val}  <{tpe}>")


if __name__ == "__main__":
    pprint_dcm(pydicom.dcmread(sys.argv[1]))
