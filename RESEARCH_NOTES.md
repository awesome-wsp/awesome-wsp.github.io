# Research update — 2026-11-03

The timeline contains 28 representative works: the original 16, 11 additions from the supplied literature survey, and AdderBoard. Diamonds identify the 12 supplemental entries. Categories organize conceptual overlap; they do not by themselves claim direct influence on WSP, priority for an entire concept, or mutual exclusivity. Explicit mentions in the WSP report are identified separately in entry descriptions. Years refer to the first public version of the listed work, while venue years appear separately in its detail view. The 1992 fast-weight paper is a historical representative, not a claim that fast weights began in 1992.

## Added works and inclusion decisions

| Year | Work / primary source | Why included |
| --- | --- | --- |
| 1992 | [Learning to Control Fast-Weight Memories](https://people.idsia.ch/~juergen/fastweights/) | Historical weight-generation background: a trained network controls another network's context-dependent weight changes. |
| 2017 | [Evolution Strategies](https://arxiv.org/abs/1703.03864) | Optimization background: target-network backpropagation is not required for parameter search. ES still uses perturbations, feedback, and an optimizer. |
| 2020 | [Rewriting a Deep Generative Model](https://arxiv.org/abs/2007.15646) | Local editing of rules encoded in a model, using a layer as associative memory. |
| 2021 | [Thinking Like Transformers / RASP](https://arxiv.org/abs/2106.06981) | Program-level abstraction of Transformer computation; precedes the Tracr compilation entry. |
| 2022 | [Model Soups](https://arxiv.org/abs/2203.05482) | Weight averaging links model merging with task arithmetic; constituent models require fine-tuning. |
| 2023 | [Activation Engineering / ActAdd](https://arxiv.org/abs/2308.10248) | Contrastive activation directions and runtime behavior steering. |
| 2023 | [Representation Engineering / RepE](https://arxiv.org/abs/2310.01405) | Population-level representation analysis and behavioral control; spans reading and intervention. |
| 2025 | [ThinkEdit](https://aclanthology.org/2025.emnlp-main.861/) ([first preprint, March](https://arxiv.org/abs/2503.22048)) | A particularly close comparison for the WSP Qwen experiment: mechanism-guided local weight editing repairs a reasoning failure. |
| 2025 | [Steering Language Models with Weight Arithmetic](https://arxiv.org/abs/2511.05408) | Connects task vectors with contrastive behavioral steering. First public November 2025; ICLR 2026. |
| 2026 | [Doc-to-LoRA](https://arxiv.org/abs/2602.15902) | Context-to-parameter generation through a specially trained hypernetwork. February preprint. |
| 2026 | [AdderBoard](https://github.com/anadim/AdderBoard) | Community challenge with trained and hand-coded tracks. The hand-coded track includes coding-agent-assisted analytic weight construction, explicitly mentioned in the WSP report. Placed in network construction, not classified as a paper or a general editing algorithm. |
| 2026 | [From Latents to Wires / L2W](https://arxiv.org/abs/2609.32434) | Named semantic target → component localization → intervention → validation. September preprint. |

## Important distinctions

- **ThinkEdit vs. WSP Qwen:** ThinkEdit removes a reasoning-length direction from selected attention-head output weights to mitigate overly short reasoning. WSP's Qwen experiment addresses repetitive thinking loops through selected MLP output weights. They overlap in mechanism-guided local repair, but differ in failure mode, edited components, and who designs the procedure. This is a methodological comparison, not evidence that one borrowed from the other. Sources: [ThinkEdit §3–4](https://aclanthology.org/2025.emnlp-main.861.pdf), [WSP report](https://rikiyat.github.io/blog/weight-space-programming/).
- **L2W is not gradient-free throughout:** localization uses Jacobian lens attribution. Its edit procedure does not justify describing the entire pipeline as having no derivatives. Source: [L2W §4–5](https://arxiv.org/html/2609.32434v1).
- **ES is not optimizer-free:** it avoids backpropagation through the target network, while estimating a search direction from parameter perturbations and task feedback. It is background for the distinction, not an instance of LLM weight programming.
- **Activation steering is not automatically weight editing:** ActAdd and CAA primarily intervene on runtime activations; weight orthogonalization persists an intervention in parameters.
- **RASP is not Tracr:** RASP supplies a programming abstraction; Tracr compiles supported RASP programs into Transformer weights.
- **Generated parameters need not imply an untrained generator:** Fast weights, HyperNetworks, Text-to-LoRA and Doc-to-LoRA rely on learned systems. Contrastive weight steering relies on fine-tuning to obtain its directions.
- **WSP is a workflow-level claim:** distinguish general-purpose LLM orchestration from the particular editing or construction operation discovered in an individual run. Absence of target gradient optimization does not imply absence of examples, forward evaluations, or candidate selection.

All dates, titles, and summaries for the additions were checked against the linked primary sources. The five-route grouping and closeness judgments are editorial interpretations, not claims made by every cited author. The original CAA and Patchscopes entries are retained even though they are not separate rows in the supplied survey.

## AdderBoard inclusion review

**Decision: include in 2026, network construction.** The [WSP report's Background and Related Works](https://rikiyat.github.io/blog/weight-space-programming/#background-and-related-works) explicitly describes AdderBoard as a tiny-scale example of coding agents setting Transformer weights by hand. This is stronger evidence of relevance than conceptual similarity alone; it does not establish that WSP reused any particular submission's implementation.

**Date:** the originating [Addition Under Pressure](https://dimitrisp.substack.com/p/addition-under-pressure) article is dated February 19, 2026; GitHub repository metadata records AdderBoard's creation on February 25, 2026. The project's own recommended citation uses 2026. Repository creation is not treated as proof of the exact date on which it became public.

**Task and distinction:** the challenge seeks the smallest autoregressive Transformer for adding two integers of up to ten digits, qualifying at at least 99% accuracy on 10,000 held-out random pairs. It distinguishes weights learned with a generic algorithm from analytically specified weights. The original Claude Code/Codex experiments train models; the subsequent hand-coded leaderboard is the closer comparison to WSP's from-scratch weight construction. The [official README](https://github.com/anadim/AdderBoard#readme) credits Codex and other coding agents on several hand-coded entries. It does not demonstrate that every entry was autonomous or agent-produced.

**Implementation evidence and limits:** an inspected [hand-coded submission](https://github.com/fblissjr/AdderBoard/blob/main/submission_1l.py) explicitly assigns tensor values in `_set_weights()` under `torch.no_grad()` and uses autoregressive token generation. It also contains a task-specific fixed attention mask, so the allocation of computation between architecture, buffers, and counted parameters matters. The board itself flags a dispute over the lowest parameter count. The timeline therefore does not assert a universal minimum, reproduce a leaderboard score as our own result, or equate analytic construction on this single task with general LLM weight-programming capability. No submission was executed in this review.
