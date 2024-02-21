#!/usr/bin/env python3

import os
import svgutils.transform as sg

# TODO: Sort all this input out into more sensible generalised args

bundle_id = 3 # 0, 1, 2, 3

output_dir = '/home/matthew/Desktop/PhD/april_tag_bundles'
output_filename = f'a4_100mm_tag_bundle_{bundle_id}.svg'
output_filepath = os.path.join(output_dir, output_filename)

tag_svg_dir = 'tag36h11/svg'

if bundle_id == 0:
    tags = [
        'tag36_11_00050_100mm.svg',
        'tag36_11_00051_100mm.svg',
        'tag36_11_00052_100mm.svg',
        'tag36_11_00053_100mm.svg'
    ]
elif bundle_id == 1:
    tags = [
        'tag36_11_00054_100mm.svg',
        'tag36_11_00055_100mm.svg',
        'tag36_11_00056_100mm.svg',
        'tag36_11_00057_100mm.svg'
    ]

elif bundle_id == 2:
    tags = [
        'tag36_11_00058_100mm.svg',
        'tag36_11_00059_100mm.svg',
        'tag36_11_00060_100mm.svg',
        'tag36_11_00061_100mm.svg'
    ]
elif bundle_id == 3:
    tags = [
        'tag36_11_00062_100mm.svg',
        'tag36_11_00063_100mm.svg',
        'tag36_11_00064_100mm.svg',
        'tag36_11_00065_100mm.svg'
    ]

# Create new SVG figure
# A4:
#    210 x 297 mm
#    793.701 x 1122.520 px

width = 210 # mm
height = 297 # mm

mm_to_px = 3.7795275591 # px/mm

width_px = width * mm_to_px
height_px = height * mm_to_px

fig = sg.SVGFigure(width=width_px, height=height_px)

# Create a background
background = sg.LineElement([(width_px / 2, 0), (width_px / 2, height_px)], width=width_px, color='white')
h_centre_line = sg.LineElement([(0, height_px / 2), (width_px, height_px / 2)], width=2, color='grey')
v_centre_line = sg.LineElement([(width_px / 2, 0), (width_px / 2, height_px)], width=2, color='grey')

# Load tags
fig0 = sg.fromfile(os.path.join(tag_svg_dir, tags[0]))
fig1 = sg.fromfile(os.path.join(tag_svg_dir, tags[1]))
fig2 = sg.fromfile(os.path.join(tag_svg_dir, tags[2]))
fig3 = sg.fromfile(os.path.join(tag_svg_dir, tags[3]))

# Get the tag objects and set their position and scale
tag0 = fig0.getroot()
tag1 = fig1.getroot()
tag2 = fig2.getroot()
tag3 = fig3.getroot()

# Played around with this and 38 seemed to work well but not sure why
# This formula seemed to make some sense but might just be coincidence...
# Seems to yield exactly the same result as the bundles I made manually in Inkscape
sf = mm_to_px * 10

tag0.moveto(5 * mm_to_px, 35 * mm_to_px, scale_x=sf, scale_y=sf)
tag1.moveto(105 * mm_to_px, 35 * mm_to_px, scale_x=sf, scale_y=sf)
tag2.moveto(5 * mm_to_px, 135 * mm_to_px, scale_x=sf, scale_y=sf)
tag3.moveto(105 * mm_to_px, 135 * mm_to_px, scale_x=sf, scale_y=sf)

# Add text labels
# Text origin
text_x = 20 * mm_to_px # 75.591
text_y = 240 * mm_to_px # 907.087

# Text spacing
ts = 20

txt0 = sg.TextElement(text_x, text_y + ts * 0, f'Bundle: {bundle_id}', size=12, weight="normal")
txt1 = sg.TextElement(text_x, text_y + ts * 1, f'Tag Family: {tag_svg_dir.split(sep="/")[0]}', size=12, weight="normal")
txt2 = sg.TextElement(text_x, text_y + ts * 2, 'Tags:', size=12, weight="normal")
txt3 = sg.TextElement(text_x + ts, text_y + ts * 3, f'TL: {tags[0].split(sep="_")[2]}', size=12, weight="normal")
txt4 = sg.TextElement(text_x + ts, text_y + ts * 4, f'TR: {tags[1].split(sep="_")[2]}', size=12, weight="normal")
txt5 = sg.TextElement(text_x + ts, text_y + ts * 5, f'BL: {tags[2].split(sep="_")[2]}', size=12, weight="normal")
txt6 = sg.TextElement(text_x + ts, text_y + ts * 6, f'BR: {tags[3].split(sep="_")[2]}', size=12, weight="normal")
txt7 = sg.TextElement(text_x, text_y + ts * 7, 'Tag images are 100x100mm or 10x10bits inc. 1 bit white border', size=12, weight="normal")
txt8 = sg.TextElement(text_x, text_y + ts * 8, 'Tags themselves are 80x80mm inc. 1 bit black border', size=12, weight="normal")

# Append everything to the figure
fig.append([background])
#fig.append([h_centre_line, v_centre_line])
fig.append([tag0, tag1, tag2, tag3])
fig.append([txt0, txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8])

# Save output to SVG file
fig.save(output_filepath)

print(f'Bundle {bundle_id}, created at: {output_filepath}')
