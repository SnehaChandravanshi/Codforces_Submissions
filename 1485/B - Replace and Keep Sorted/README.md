<h2><a href="https://codeforces.com/contest/1485/problem/B" target="_blank" rel="noopener noreferrer">1485B — Replace and Keep Sorted</a></h2>

| | |
|---|---|
| **Difficulty** | 1200 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1485B](https://codeforces.com/contest/1485/problem/B) |

## Topics
`dp` `implementation` `math`

---

## Problem Statement

<div class="header"><div class="title">B. Replace and Keep Sorted</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Given a positive integer $$$k$$$, two arrays are called $$$k$$$-similar if:</p><ul> <li> they are <span class="tex-font-style-bf">strictly increasing</span>; </li><li> they have the same length; </li><li> all their elements are positive integers between $$$1$$$ and $$$k$$$ (inclusive); </li><li> they differ in <span class="tex-font-style-bf">exactly</span> one position. </li></ul><p>You are given an integer $$$k$$$, a <span class="tex-font-style-bf">strictly increasing</span> array $$$a$$$ and $$$q$$$ queries. For each query, you are given two integers $$$l_i \leq r_i$$$. Your task is to find how many arrays $$$b$$$ exist, such that $$$b$$$ is $$$k$$$-similar to array $$$[a_{l_i},a_{l_i+1}\ldots,a_{r_i}]$$$. </p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains three integers $$$n$$$, $$$q$$$ and $$$k$$$ ($$$1\leq n, q \leq 10^5$$$, $$$n\leq k \leq 10^9$$$) — the length of array $$$a$$$, the number of queries and number $$$k$$$.</p><p>The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots,a_n$$$ ($$$1 \leq a_i \leq k$$$). This array is strictly increasing  — $$$a_1  \lt  a_2  \lt  \ldots  \lt  a_n$$$.</p><p>Each of the following $$$q$$$ lines contains two integers $$$l_i$$$, $$$r_i$$$ ($$$1 \leq l_i \leq r_i \leq n$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$q$$$ lines. The $$$i$$$-th of them should contain the answer to the $$$i$$$-th query.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005657073980891097" id="id005196370097367765" class="input-output-copier">Copy</div></div><pre id="id005657073980891097">4 2 5
1 2 4 5
2 3
3 4
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009630265262018389" id="id004551749234186294" class="input-output-copier">Copy</div></div><pre id="id009630265262018389">4
3
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008039821164209022" id="id009801326256152798" class="input-output-copier">Copy</div></div><pre id="id008039821164209022">6 5 10
2 4 6 7 8 9
1 4
1 2
3 5
1 6
5 5
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id002834262952556763" id="id002806455596220976" class="input-output-copier">Copy</div></div><pre id="id002834262952556763">8
9
7
6
9
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example:</p><p>In the first query there are $$$4$$$ arrays that are $$$5$$$-similar to $$$[2,4]$$$: $$$[1,4],[3,4],[2,3],[2,5]$$$.</p><p>In the second query there are $$$3$$$ arrays that are $$$5$$$-similar to $$$[4,5]$$$: $$$[1,5],[2,5],[3,5]$$$.</p></div>