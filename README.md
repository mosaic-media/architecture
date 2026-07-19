# Mosaic

A self-hosted media server that covers every format in one place — music, television, film, anime, comics, manga, audiobooks — without requiring the user to run three separate systems, or to become their own IT support.

This repository holds Mosaic's architecture and direction. The implementation lives in [`mosaic-platform`](https://github.com/mosaic-media/mosaic-platform).

---

## Read these

| Document | What it answers |
|---|---|
| **[MOSAIC.md](MOSAIC.md)** | What Mosaic is, why it exists, what has been decided, and what has deliberately not been |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | How the platform is built. Written from the source, not from a plan |
| **[ROADMAP.md](ROADMAP.md)** | What is being built next, and what is blocking it |

Three documents. That is the whole repository.

---

## How this repository works

**Code is authoritative.** Where `mosaic-platform` has built something, the code decides and these documents describe it. They do not specify it in advance and they do not contradict it. If a document disagrees with the source, the document is wrong.

**Documentation follows implementation.** Roadmaps may look forward; descriptions of the system may not. Documentation written for unbuilt software has nothing pushing back on it, which is how contradictions survive indefinitely.

**Superseded content is deleted, not annotated.** Git keeps every abandoned idea permanently, so deleting costs nothing and leaving stale material costs a great deal. A note saying "this section is out of date" does not outweigh the pages around it that still assert the old thing.

**One authoritative statement per fact.** If two documents answer the same question, a reader picks one, and the choice is arbitrary.

---

## History

This repository previously held over two hundred specification documents under a bespoke taxonomy — MDL, MDS, MEG, MAC, MIP, MOP, MAD, MDP. Most of it was generated across many AI sessions and never validated. It accumulated contradictions faster than anyone could resolve them, and eventually began producing wrong work: a roadmap built against a storage model that had been abandoned, and a transport layer the architecture explicitly forbids.

The cause was structural. The repository was serving as both memory across sessions and source of truth, and those want opposite things — memory accumulates, truth replaces. Memory won by volume, so abandoned ideas were retrieved as current architecture.

The full prior corpus is preserved at tag `pre-reset-2026-07-19` and can be recovered in whole or in part at any time.

The `docs/` directory is what remains of it. It is **legacy and not authoritative**. It is being retired as its remaining useful content is absorbed here.
