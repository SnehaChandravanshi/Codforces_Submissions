<h2><a href="https://codeforces.com/contest/1409/problem/D" target="_blank" rel="noopener noreferrer">1409D — Decrease the Sum of Digits</a></h2>

| | |
|---|---|
| **Difficulty** | 1500 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1409D](https://codeforces.com/contest/1409/problem/D) |

## Topics
`greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">D. Decrease the Sum of Digits</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a positive integer $$$n$$$. In one move, you can increase $$$n$$$ by one (i.e. make $$$n := n + 1$$$). Your task is to find the minimum number of moves you need to perform in order to make the sum of digits of $$$n$$$ be less than or equal to $$$s$$$.</p><p>You have to answer $$$t$$$ independent test cases.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$t$$$ ($$$1 \le t \le 2 \cdot 10^4$$$) — the number of test cases. Then $$$t$$$ test cases follow.</p><p>The only line of the test case contains two integers $$$n$$$ and $$$s$$$ ($$$1 \le n \le 10^{18}$$$; $$$1 \le s \le 162$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the answer: the minimum number of moves you need to perform in order to make the sum of digits of $$$n$$$ be less than or equal to $$$s$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0026905226356739775" id="id0023702377493385773" class="input-output-copier">Copy</div></div><pre id="id0026905226356739775">5
2 1
1 1
500 4
217871987498122 10
100000000000000001 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0067382412879591" id="id008193146184902187" class="input-output-copier">Copy</div></div><pre id="id0067382412879591">8
0
500
2128012501878
899999999999999999
</pre></div></div></div>