<h2><a href="https://codeforces.com/contest/1176/problem/C" target="_blank" rel="noopener noreferrer">1176C — Lose it!</a></h2>

| | |
|---|---|
| **Difficulty** | 1300 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1176C](https://codeforces.com/contest/1176/problem/C) |

## Topics
`dp` `greedy` `implementation`

---

## Problem Statement

<div class="header"><div class="title">C. Lose it!</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given an array $$$a$$$ consisting of $$$n$$$ integers. Each $$$a_i$$$ is one of the six following numbers: $$$4, 8, 15, 16, 23, 42$$$.</p><p>Your task is to remove the minimum number of elements to make this array <span class="tex-font-style-bf">good</span>.</p><p>An array of length $$$k$$$ is called <span class="tex-font-style-bf">good</span> if $$$k$$$ is divisible by $$$6$$$ and it is possible to split it into $$$\frac{k}{6}$$$ <span class="tex-font-style-bf">subsequences</span> $$$4, 8, 15, 16, 23, 42$$$.</p><p>Examples of good arrays:</p><ul> <li> $$$[4, 8, 15, 16, 23, 42]$$$ (the whole array is a required sequence); </li><li> $$$[4, 8, 4, 15, 16, 8, 23, 15, 16, 42, 23, 42]$$$ (the first sequence is formed from first, second, fourth, fifth, seventh and tenth elements and the second one is formed from remaining elements); </li><li> $$$[]$$$ (<span class="tex-font-style-bf">the empty array is good</span>). </li></ul><p>Examples of bad arrays: </p><ul> <li> $$$[4, 8, 15, 16, 42, 23]$$$ (the order of elements should be exactly $$$4, 8, 15, 16, 23, 42$$$); </li><li> $$$[4, 8, 15, 16, 23, 42, 4]$$$ (the length of the array is not divisible by $$$6$$$); </li><li> $$$[4, 8, 15, 16, 23, 42, 4, 8, 15, 16, 23, 23]$$$ (the first sequence can be formed from first six elements but the remaining array cannot form the required sequence). </li></ul></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 5 \cdot 10^5$$$) — the number of elements in $$$a$$$.</p><p>The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ (each $$$a_i$$$ is one of the following numbers: $$$4, 8, 15, 16, 23, 42$$$), where $$$a_i$$$ is the $$$i$$$-th element of $$$a$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print one integer — the minimum number of elements you have to remove to obtain a <span class="tex-font-style-bf">good</span> array.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id007324985020201467" id="id00921498575005269" class="input-output-copier">Copy</div></div><pre id="id007324985020201467">5
4 8 15 16 23
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005779687597190103" id="id005318648665451793" class="input-output-copier">Copy</div></div><pre id="id005779687597190103">5
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006624096304545236" id="id005346097520362442" class="input-output-copier">Copy</div></div><pre id="id006624096304545236">12
4 8 4 15 16 8 23 15 16 42 23 42
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00943105800934464" id="id009982386282752633" class="input-output-copier">Copy</div></div><pre id="id00943105800934464">0
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id002938710174750655" id="id007549727505110493" class="input-output-copier">Copy</div></div><pre id="id002938710174750655">15
4 8 4 8 15 16 8 16 23 15 16 4 42 23 42
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008705101122928184" id="id00502862260227251" class="input-output-copier">Copy</div></div><pre id="id008705101122928184">3
</pre></div></div></div>