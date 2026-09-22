import fitz
import os

doc = fitz.open('specs/presentations/1765634791410.pdf')
out_dir = 'specs/presentations/extracted/assets'
os.makedirs(out_dir, exist_ok=True)

for i, page in enumerate(doc):
    images = page.get_images(full=True)
    print(f"Page {i+1}: {len(images)} images")
    for j, img in enumerate(images):
        xref = img[0]
        base = doc.extract_image(xref)
        fname = os.path.join(out_dir, f"p{i+1}_img{j+1}_{xref}.{base['ext']}")
        with open(fname, "wb") as f:
            f.write(base["image"])
        print(f"  Saved {fname}: {base['width']}x{base['height']}")
