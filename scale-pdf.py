"""
This does not seems to reduce the size of the PDF.
"""
import PyPDF2
import argparse


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Resize pdf')
    parser.add_argument('input', help="The path of the input pdf")
    parser.add_argument('scale', type=float, help="Scale (from 0 -> 1)", )
    parser.add_argument('output', help="The path of the optimized pdf")
    args = parser.parse_args()
    # parser.print_help()
    # raise Exception("/Users/aalobaid/passport scan 17-1-2022/scan 1.pdf")
    # input = "/Users/aalobaid/passport scan 17-1-2022/Handwritten_2022-01-17_064735.pdf"
    # input = "/Users/aalobaid/passport scan 17-1-2022/scan 1.pdf"
    return args.input, args.scale, args.output


def scale_pdf(input, scale, output):
    pdf = PyPDF2.PdfFileReader(input, strict=False)
    num_pages = pdf.getNumPages()
    writer = PyPDF2.PdfFileWriter()  # create a writer to save the updated results
    for i in range(num_pages):
        page0 = pdf.getPage(i)
        page0.scaleTo(288, 397)
        #page0.scaleBy(scale)  # float representing scale factor - this happens in-place
        page0.compressContentStreams()
        writer.addPage(page0)
    with open(output, "wb+") as f:
        writer.write(f)


if __name__ == '__main__':
    inp, sc, out = parse_arguments()
    scale_pdf(inp, sc, out)

# pdf = "YOUR PDF FILE PATH.pdf"
#
# pdf = PyPDF2.PdfFileReader(pdf)
# page0 = pdf.getPage(0)
# page0.scaleBy(0.5)  # float representing scale factor - this happens in-place
# writer = PyPDF2.PdfFileWriter()  # create a writer to save the updated results
# writer.addPage(page0)
# with open("YOUR OUTPUT PDF FILE PATH.pdf", "wb+") as f:
#     writer.write(f)
