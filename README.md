# LLM Hallucination & Fact Checking Benchmark

> Evidence-linked claim review with abstention and error analysis.

A data-first benchmark scaffold for reviewing claims against provided evidence. It computes claim-level coverage and unsupported rates from human adjudication labels. It deliberately does not pretend keyword matching can establish truth.

## Why this project

This project reflects portfolio interests in AI operations, careful evaluation, annotation quality, and reproducible data workflows. It is a personal demonstration built from synthetic or sample data; it does not represent client work or measured professional outcomes.

## Quick start

Python 3.10+ is recommended. Run from the repository root:

```bash
python src/factcheck.py data/claims.jsonl
```

## Repository contents

- `src/` contains the core implementation.
- `data/` contains small illustrative fixtures where applicable.
- Outputs are generated locally and are not checked in.

## Method and interpretation

The implementation favors readable baselines and explicit assumptions. Scores from demonstration data are not general performance estimates. Human review remains necessary for semantic correctness, evidence quality, and policy or safety judgments.

## Limitations

- Included records are synthetic or illustrative and are not client data.
- No production deployment, external model API, or independently validated result is claimed.
- Review the assumptions and adapt the workflow before using it on consequential data.

## License

MIT. See [LICENSE](LICENSE).
