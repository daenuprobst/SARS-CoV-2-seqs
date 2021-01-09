import json
import gzip
from collections import defaultdict
from typing import Dict
from Bio import SeqIO


def get_seqs() -> Dict[str, str]:
    """Creates a mapping of accession.version ids to the protein sequences.

    Returns:
        A mapping of accession.version ids to the protein sequences.
    """
    mapping = {}
    for record in SeqIO.parse("data/ncbi_dataset/data/protein.faa", "fasta"):
        id = record.id.split(":")[0]
        mapping[id] = str(record.seq)
    return mapping


def main():
    # Get the id to sequence map. The ID is speciefied as accession.version
    id_seq = get_seqs()
    stats = {
        "region_counts": defaultdict(lambda: 0),
        "country_counts": defaultdict(lambda: 0),
        "subcountry_counts": defaultdict(lambda: 0),
    }

    # Write interesting annotations into a CSV file
    with gzip.open("data/annotated_seqs.csv.gz", "wb") as f_out:
        with open("data/ncbi_dataset/data/data_report.jsonl", "r") as f:
            for line in f.readlines():
                data = json.loads(line)
                if (
                    data["completeness"] == "COMPLETE"
                    and "annotation" in data
                    and "location" in data
                ):
                    for genes in data["annotation"]["genes"]:
                        if "cds" in genes:
                            for cd in genes["cds"]:
                                id = cd["protein"]["accessionVersion"]

                                region = data["location"]["geographicRegion"]
                                location = data["location"]["geographicLocation"]
                                location = location.split(":")

                                country = location[0].strip()
                                subcountry = ""
                                if len(location) > 1:
                                    subcountry = location[1].strip()

                                # Update stats
                                stats["region_counts"][region] += 1
                                stats["country_counts"][country] += 1
                                stats["subcountry_counts"][subcountry] += 1

                                f_out.write(
                                    ",".join(
                                        [
                                            id,
                                            genes["name"],
                                            data["isolate"]["collectionDate"],
                                            region,
                                            country,
                                            subcountry,
                                            id_seq[id],
                                        ]
                                    ).encode()
                                )

                                f_out.write("\n".encode())


if __name__ == "__main__":
    main()