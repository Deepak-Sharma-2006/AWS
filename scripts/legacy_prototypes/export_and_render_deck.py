import os
import win32com.client
import pymupdf

pptx_path = os.path.abspath("specs/presentations/CHAKRA_SIH2026_Championship_Deck.pptx")
pdf_path = os.path.abspath("specs/presentations/CHAKRA_SIH2026_Championship_Deck.pdf")
render_dir = os.path.abspath("specs/presentations/rendered/chakra")
os.makedirs(render_dir, exist_ok=True)

print(f"Opening {pptx_path} with PowerPoint...")
powerpoint = win32com.client.Dispatch("PowerPoint.Application")
try:
    deck = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
    # 32 = ppSaveAsPDF
    print(f"Saving to {pdf_path}...")
    deck.SaveAs(pdf_path, 32)
    deck.Close()
    print("Exported PDF successfully!")
finally:
    powerpoint.Quit()

print("Rendering PDF pages to PNG at 300 DPI...")
doc = pymupdf.open(pdf_path)
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=200)
    out_png = os.path.join(render_dir, f"chakra_slide_{i+1}.png")
    pix.save(out_png)
    print(f"Rendered Slide {i+1} -> {out_png} ({pix.width}x{pix.height})")

print("All slides rendered successfully!")
