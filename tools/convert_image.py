from PIL import Image
import sys
import os

def convert_bmp_to_c_array(input_file, output_file):
    # Open the image
    img = Image.open(input_file).convert('1')  # Convert to monochrome (1-bit)
    
    # Get image size
    width, height = img.size
    
    # Create a C array from the image data
    pixels = list(img.getdata())
    
    # Start generating the C array
    c_array = f"const uint8_t my_image[{width * height // 8}] = {{\n"
    
    byte = 0
    bit_count = 0
    for i, pixel in enumerate(pixels):
        # BMP stores white as 255 and black as 0, but we want 0 for white and 1 for black
        bit = 0 if pixel == 255 else 1
        byte |= (bit << (7 - bit_count))
        bit_count += 1
        
        # After collecting 8 bits, we write the byte to the C array
        if bit_count == 8:
            c_array += f"0x{byte:02X}, "
            byte = 0
            bit_count = 0
            
            # Break into new lines for readability
            if (i + 1) % width == 0:
                c_array += "\n"
    
    c_array += "};\n"
    
    # Write the C array to the output file
    with open(output_file, 'w') as f:
        f.write(f"// Image: {input_file} ({width}x{height})\n")
        f.write(c_array)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_image.py --input <input.bmp> --output <output.c>")
        sys.exit(1)
    
    input_file = sys.argv[2] if sys.argv[1] == '--input' else None
    output_file = sys.argv[4] if sys.argv[3] == '--output' else None
    
    if input_file and output_file:
        if os.path.exists(input_file):
            convert_bmp_to_c_array(input_file, output_file)
        else:
            print(f"Input file {input_file} does not exist.")
    else:
        print("Invalid arguments. Use --input and --output correctly.")
