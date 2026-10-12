# Responses and manuscript locators

## A useful response shape

Give the answer, change, and focused evidence in a connected paragraph. Use a second paragraph when an explanation/exception needs one. Follow the comment's structure, not a compulsory list of headings.

Illustrative wording, to adapt only when supported:

> We have clarified the parameter-counting scope. The revised table reports image-encoder parameters and stored encoder state, and the accompanying text separately describes the auxiliary transmitter modules. This distinguishes the footprint reduced by distillation from the complete transmitter footprint.

An opening acknowledgment can thank a reviewer for a specific type of feedback. Keep it once at the start of their section; removing repeated comment-level thanks does not make replies impolite.

Avoid answering a technical concern only with praise for the question. Do not say a concern is resolved while its relevant experiment remains pending.

## Color and macro behavior

Keep existing macros whenever they work. Color declarations should be scoped so a label's color does not leak into ordinary prose.

For a new template, this illustrates the intended behavior, not a mandatory preamble replacement:

```latex
\newcommand{\response}{\par\noindent
  {\color{green}\textbf{Authors' response:}}\ \color{black}}
\newcommand{\action}{\par\noindent
  {\color{green}\textbf{Authors' actions on the revised manuscript:}}\
  \color{black}}
\newcommand{\revblue}[1]{{\color{blue}#1}}
```

An action and quote can be arranged as follows:

```latex
\action We have clarified the routing-budget definition in the
relevant method subsection.
\begin{quote}
\uline{Section~IV-A, Page~5:}
``{\color{blue}The same transmission budget is used for each routing policy.}''
\end{quote}
```

This is a syntax example. Its wording and locator are illustrative, not a quotation or page number to copy into a real letter. Replace them with actual manuscript text and the final compiled locator.

## What to quote

Quote the paragraph, equation, caption, or table text demonstrating the change. Avoid a complete subsection when one paragraph suffices. An introduction paragraph cannot substantiate an implementation detail it does not state.

Extract from current source, including revisions. Resolve macros to the same rendered wording. Normalize whitespace and local formatting for comparison; do not remove a qualification, change a number, or reorder logic.

If converting citations into manual bracket numbers, use the final bibliography numbering. Quote content and citation numbering are distinct checks.

## Locators

Resolve section/subsection, figure, table, equation, and page numbers from the final PDF/label map. A figure number can remain stable while its page changes. A moved float or shortened caption can invalidate a locator even when quote text is unchanged.

For manual references, maintain a temporary stable-label-to-number/page mapping. Apply it only to authorized files. Inspect `??`, unresolved external `\ref`/`\pageref`, and explicit page references in changed responses.

Run the locator check after the last layout-affecting edit. Compile enough passes for local references to stabilize. Do not rely on an older PDF or earlier successful compile.

## Self-contained reviewer replies

A response may refer to a manuscript section/table every reviewer receives. It should not depend on another reviewer's response document. Replace "Response 2.2" with the focused estimate and condition needed to answer the present comment.

Keep comparisons faithful to their statistical unit. A paired mean per-image AP difference does not automatically supply a pooled-mAP interval. Evaluation randomness and training randomness need separate descriptions.

## Concise correction language

Describe the corrected boundary/method and re-evaluated result. Avoid emotionally loaded wording when a neutral technical explanation suffices. Necessary corrections and invalidated conclusions still need to be clear.

Do not claim code was unavailable merely to justify dropping a comparison. Check appropriate primary sources when a search is required, then state what was not found within that search. When a result does not measure the named method, remove or recompute the comparison and dependent claims.

## Delivery checks

Keep reviewer comments, advisor notes, and response numbering intact. Check that action statements match quotes, quoted evidence answers the actual comment, and the summary promises no work absent from the replies.

Report pending code verification outside the letter unless its absence is needed to interpret the response. Formatting alone is not authority to rewrite scientific claims or submit the letter.
