'''
It scans specification text looking for
    - implementation-defined
    - implementation-specific
    - may
    - optional
    - shall
    etc.
Basically
Candidate sentence finder.
This reduces LLM workload.
candidate_detector.py

Find potential architectural parameter sentences
from RISC-V specification text.

This reduces LLM extraction workload.
'''

import re
import json
import argparse
from pathlib import Path


KEYWORDS = {

    # Strong indicators
    "implementation-defined": 1.0,
    "implementation-specific": 1.0,

    # Optional behavior
    "optional": 0.8,
    "may": 0.6,

    # Requirement language
    "shall": 0.5,
    "must": 0.5,

    # Configurability
    "configurable": 0.9,
    "platform-dependent": 0.9,

    # Discoverability
    "discover": 0.8,
    "software can": 0.8,

    # RISC-V specific
    "WARL": 0.9,
    "WPRI": 0.9,
    "WLRL": 0.9,
}


def split_sentences(text):
    """
    Simple sentence splitter.
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


def find_candidates(text, threshold=0.5):

    candidates = []

    sentences = split_sentences(text)

    for idx, sentence in enumerate(sentences, start=1):

        sentence_lower = sentence.lower()

        matched_keywords = []
        score = 0


        for keyword, weight in KEYWORDS.items():

            if keyword.lower() in sentence_lower:
                matched_keywords.append(keyword)
                score = max(score, weight)


        if score >= threshold:

            candidates.append(
                {
                    "line": idx,
                    "sentence": sentence,
                    "matched_keywords": matched_keywords,
                    "score": score
                }
            )


    return candidates



def generate_output_path(input_file):

    """
    Convert:

    snippets/priveleged_19.3.1.txt

    into:

    candidates/candidates_19.3.1.json
    """

    filename = Path(input_file).stem

    # remove prefix
    version = filename.replace(
        "priveleged_",
        ""
    )

    output_dir = Path("candidates")

    output_dir.mkdir(
        exist_ok=True
    )


    return output_dir / f"candidates_{version}.json"



def main():

    parser = argparse.ArgumentParser(
        description="Find candidate architectural parameter sentences"
    )


    parser.add_argument(
        "input",
        help="Specification text file"
    )


    args = parser.parse_args()


    input_file = Path(args.input)


    text = input_file.read_text(
        encoding="utf-8"
    )


    candidates = find_candidates(text)


    output_file = generate_output_path(
        input_file
    )


    output_file.write_text(
        json.dumps(
            candidates,
            indent=4
        ),
        encoding="utf-8"
    )


    print(
        f"Found {len(candidates)} candidate sentences"
    )

    print(
        f"Saved: {output_file}"
    )



if __name__ == "__main__":
    main()