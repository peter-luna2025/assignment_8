from fpdf import FPDF


def create_shirtificate_pdf():
    user_name = input("What's your name?  ")
    # path = "image (https://py-pdf.github.io/fpdf2/Images.html)"

    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=40, w=210)

    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", style="B", size=24)
    pdf.multi_cell(0, 10, f"CS50 Shirtificate", align="C")

    pdf.ln(80)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", style="B", size=24)
    pdf.cell(0, 10, f"{user_name} took CS50", align="C")

    pdf.output("shirtificate.pdf")
    print("\nSuccessfully created PDF: shirtificate.pdf")
    print("CS50 Shirtificate")


if __name__ == "__main__":
    create_shirtificate_pdf()
