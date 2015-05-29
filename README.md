# threejs-dithershader
Based entirely on "C64 Shader" but with changes to play around with dithering and colors. 

The implementation for the color palette is computationally expensive. The dithering is ordered bayer 8x8 dithering, but I can't get it to not completely color mute by overpowering with whites and blacks. That said, the input source, be it a video or an image, greatly impacts the output, so perhaps there's no one size fits all filter.
