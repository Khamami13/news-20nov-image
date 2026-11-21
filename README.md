# The World in One Page — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Khamami13/news-20nov-image/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Khamami13/news-20nov-image/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that writes one image summing up the world's news of
**Friday, 20 November 2026**, built for make.fun's **"Sum up 20 November's
world news in one image"** bounty ($250, 50 paid places).

## The image

A 1024×1024 newspaper front page — *"THE WORLD IN ONE PAGE"* — drawn
with Python/PIL (`draw_news.py`), with a masthead naming the day and six
stories plus a ticker of four more, all first reported on 20 November 2026:

| Story | What the image says |
|---|---|
| **Lead — GTA VI** | $3.79 billion in day-one retail sales; 32.5 million copies sold before release — the biggest entertainment launch in history (Reuters, CNN, Barron's, 20 Nov) |
| **War in Europe** | Russian missiles and a drone land in Poland; strikes hit three Kyiv bridges — NATO calls it a grave violation; three killed in Kyiv (BBC, France 24, 20 Nov) |
| **Justice — The Hague** | World Court (ICJ) rules Myanmar committed genocide against the Rohingya |
| **Markets** | Stocks slide as the AI sell-off deepens: S&P 500 −3.7% into correction, Nikkei −5.1% |
| **Tech** | Anthropic's Nasdaq debut: shares +17%, $81.3bn raised — the largest IPO on record |
| **Europe** | UK and EU sign deals on food trade, carbon markets and youth mobility |
| **Ticker** | Houthi missile hits Riyadh tower · BepiColombo reaches Mercury · US loses measles-free status · Cyclone Akvan hits Odisha |

The footer states plainly that it is a drawn summary, not a photograph,
and names its sources.

## How it runs

`main.ts` (Node 22, standard library only) copies the committed
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
locally) and leaves it world-readable. No network, no clock, no
randomness — two runs write byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`entry.png` is 1024×1024, well under the 1 MiB limit. The generator
`draw_news.py` is kept in the repo so the image's provenance is visible;
the graded program does not run it.

## License

MIT — see [LICENSE](LICENSE).
