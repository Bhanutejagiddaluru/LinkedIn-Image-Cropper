# LinkedIn Image Cropper & Smart Band Tool

Interactive, zero-distortion image prep for LinkedIn posts and profile media.  
Move a **fixed 1200×627 (1.91:1)** crop box or save a **vertical band** between two guides—perfect for getting the key content into LinkedIn’s preview without awkward padding or losing important details.

> Works with JPG/PNG/WEBP/BMP/TIFF and **HEIC/HEIF** (with `pillow-heif`).

---

## Why this tool?

LinkedIn often crops or compresses images into a ~**1.91:1** frame (e.g., **1200×627**).  
Two common problems:
- **Cropping** cuts off important parts.
- **Padding** wastes space or looks sloppy.

This tool gives you control:
- Precisely pick the **fixed-ratio box** (exact LinkedIn frame).
- Or capture a **vertical band** (left & right aligned to the box) to preserve more width context.

---

## Features

- ✅ **Fixed-ratio box** (default 1200×627) — move/resize, save exact LinkedIn-ready image.
- ✅ **Vertical band mode** — save full-height region between two vertical guides.
- ✅ **Multi-format input** (JPG, PNG, WEBP, BMP, TIFF; HEIC/HEIF via `pillow-heif`).
- ✅ **Folder & glob** support (e.g., `folder/`, `*.jpg`).
- ✅ **Auto EXIF orientation** correction (rotated phone photos).
- ✅ **Consistent output naming**:  
  - `name_box_1200x627.jpg`  
  - `name_band_1200x627.jpg`
- ✅ **Windows-friendly paths** and interactive controls.
- ✅ Safe window cleanup (no OpenCV “NULL window” crashes).

---

## Installation

```bash
# 1) Create/activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install opencv-python pillow

# 3) (Optional) HEIC/HEIF support
pip install pillow-heif
```

---

## Quick Start

```bash
# Single file
python linkedin_crop_tool.py "path/to/image.jpg"

# Entire folder (recursively)
python linkedin_crop_tool.py "path/to/folder"

# Globs / multiple inputs
python linkedin_crop_tool.py "*.png" "more_images/*.jpg" "one_more_folder"
```

By default, outputs go to `./out` as JPEG (`.jpg`) sized **1200×627**.

---

## Usage (CLI)

```bash
python linkedin_crop_tool.py INPUTS... [--out-dir OUT] [--out-ext EXT] [--size WxH] [--quality N]
```

**Arguments**
- `INPUTS` — file(s), folder(s), or glob(s). Examples:
  - `photo.jpg`
  - `D:\Images\Campaign\`
  - `"D:\Images\*.png"`
- `--out-dir` — output directory (default: `out`)
- `--out-ext` — `.jpg` | `.jpeg` | `.png` (default: `.jpg`)
- `--size` — target size (default: `1200x627`)
- `--quality` — JPEG quality 1–100 (default: `92`)

**Examples**
```bash
# Windows: folder of images, PNG output
python linkedin_crop_tool.py "D:\KENT STATE UNIVERSITY\LinkedIn\Image resizer\myfolder" --out-dir "D:\exports" --out-ext .png

# Custom size (still fixed-ratio behavior)
python linkedin_crop_tool.py "myfolder" --size 1200x627

# Mixed inputs
python linkedin_crop_tool.py "one.jpg" "myfolder" "*.png"
```

---

## Interactive Controls

When the tool window opens:

- **Drag (mouse)**: move the **fixed-ratio box**
- **+ / -**: grow / shrink the box (ratio locked)
- **C**: save the **Fixed Box** crop → `*_box_1200x627.jpg`
- **B**: save the **Vertical Band** crop (between two guides) → `*_band_1200x627.jpg`
- **N**: proceed to the **next image**
- **Q**: quit

> The **two vertical guide lines** are always aligned to the left & right edges of the fixed box.

---

## Output Naming

For input `myphoto.png` and size `1200x627`:
- Fixed box: `myphoto_box_1200x627.jpg`
- Vertical band: `myphoto_band_1200x627.jpg`

Saved under `--out-dir` (default `./out`).

---

## Tips

- Keep important content **within the fixed box** for perfect LinkedIn framing.
- Use **Vertical Band** when you want to preserve more horizontal context across the full height.
- If LinkedIn compresses your upload, try **PNG** (`--out-ext .png`) or increase `--quality`.

---

## Troubleshooting

**OpenCV window error (NULL window)**  
Already handled in code (safe window destroy). If you still see issues, update OpenCV:
```bash
pip install --upgrade opencv-python
```

**HEIC/HEIF files don’t open**  
Install the optional plugin:
```bash
pip install pillow-heif
```

**Non-ASCII / long Windows paths**  
Wrap paths in quotes or use short paths:
```bash
python linkedin_crop_tool.py "D:\KENT STATE UNIVERSITY\LinkedIn\Image resizer\myfolder"
```

---

## Roadmap

- [ ] Horizontal band mode (two horizontal guides)
- [ ] Non-interactive batch mode (`--auto`) for center crops
- [ ] Smart padding / blurred background mode
- [ ] Save/restore last box position per image
- [ ] Simple GUI file/folder picker (no terminal needed)

---

## License

MIT License — free to use in personal and commercial projects.  
Please star the repo if it helps you!

---

## Repo Name

**Recommended:** `linkedin-image-cropper`  
(Alternative: `linkedin-media-cropper`, `linkedin-smart-cropper`)
