// "The World in One Page" — make.fun news-image-20261120 entry (Node 22,
// standard library only). The front page is the entry.png beside this file,
// drawn at build time by draw_news.py (PIL) from the verified news of
// Friday 20 November 2026; the program copies it to /output/entry.png.
// Copying fixed bytes is deterministic by construction: two runs write
// the same bytes. No network, no clock, no randomness.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, chmodSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const out = join(outDir, 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), out);
// The gate collects outputs as another user: leave the file world-readable.
chmodSync(out, 0o644);
