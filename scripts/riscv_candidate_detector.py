"""
riscv_candidate_detector.py

RISC-V specification aware candidate sentence detector.

Finds sentences likely containing architectural parameters
using RISC-V specific terminology.

Output:
candidates/riscv_candidates_<spec>.json
"""


import re
import json
import argparse
from pathlib import Path



# RISC-V specific indicators
RISCV_KEYWORDS = {

    # Register / CSR behavior
    "WARL": 1.0,
    "WPRI": 1.0,
    "WLRL": 1.0,
    "CSR": 0.8,

    # Register fields
    "field": 0.7,
    "encoding": 0.8,
    "reserved": 0.7,

    # Software visibility
    "software": 0.6,
    "discover": 0.9,

    # Access properties
    "read-only": 0.8,
    "writeable": 0.8,
    "writable": 0.8,

    # Specification language
    "implementation-defined": 1.0,
    "implementation-specific": 1.0,

    # Constraints
    "must be zero": 0.9,
    "optional": 0.7,

    # Architecture terms
    "extension": 0.7,
    "parameter": 0.8,
    "configuration": 0.8,
}



def split_sentences(text):

    """
    Basic sentence splitting.
    """

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    return [
        s.strip()
        for s in sentences
        if s.strip()
    ]



def find_candidates(text, threshold=0.6):

    candidates = []


    sentences = split_sentences(text)


    for index, sentence in enumerate(
        sentences,
        start=1
    ):

        sentence_lower = sentence.lower()


        matched = []
        score = 0



        for keyword, weight in RISCV_KEYWORDS.items():

            if keyword.lower() in sentence_lower:

                matched.append(keyword)

                score = max(
                    score,
                    weight
                )



        if score >= threshold:

            candidates.append(
                {
                    "sentence_id": index,
                    "sentence": sentence,
                    "matched_keywords": matched,
                    "confidence": score
                }
            )


    return candidates



def generate_output(input_file):

    """
    Example:

    snippets/priveleged_19.3.1.txt

    becomes:

    candidates/riscv_candidates_19.3.1.json
    """

    name = Path(input_file).stem


    version = name.replace(
        "priveleged_",
        ""
    )


    output_dir = Path(
        "candidates"
    )


    output_dir.mkdir(
        exist_ok=True
    )


    return (
        output_dir /
        f"riscv_candidates_{version}.json"
    )



def main():

    parser = argparse.ArgumentParser(
        description=
        "RISC-V specification candidate detector"
    )


    parser.add_argument(
        "input",
        help="RISC-V specification text file"
    )


    args = parser.parse_args()



    text = Path(
        args.input
    ).read_text(
        encoding="utf-8"
    )



    candidates = find_candidates(
        text
    )



    output = generate_output(
        args.input
    )



    output.write_text(
        json.dumps(
            candidates,
            indent=4
        ),
        encoding="utf-8"
    )



    print(
        f"Found {len(candidates)} RISC-V candidates"
    )

    print(
        f"Saved: {output}"
    )



if __name__ == "__main__":

    main()