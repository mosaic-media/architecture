// Render Mermaid diagrams.
//
// Material for MkDocs has its own Mermaid integration, but it targets
// `pre.mermaid` and fails silently against mermaid v11 — it replaces the
// element with an empty div and never injects an SVG. Emitting `div.mermaid`
// instead (fence_div_format in mkdocs.yml) sidesteps that handler entirely,
// and mermaid's own auto-run handles the rest.
//
// Rendering must finish before scripts/build_pdfs.py prints the page, so the
// document is marked when every diagram has an SVG.
import mermaid from "https://unpkg.com/mermaid@11/dist/mermaid.esm.min.mjs";

mermaid.initialize({ startOnLoad: false, theme: "default", securityLevel: "strict" });

async function render() {
  const nodes = document.querySelectorAll("div.mermaid:not([data-processed])");
  if (!nodes.length) {
    document.documentElement.setAttribute("data-mermaid-ready", "true");
    return;
  }
  try {
    await mermaid.run({ nodes });
  } catch (error) {
    console.error("mermaid render failed", error);
  }
  document.documentElement.setAttribute("data-mermaid-ready", "true");
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", render);
} else {
  render();
}
