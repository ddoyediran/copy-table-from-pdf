import tabula

#pdf_path = "https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf"

#dfs = tabula.read_pdf(pdf_path, pages=1)

#df = tabula.read_pdf("https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf", pages="all")

pdf_path = "tables_sample.pdf"

df = tabula.read_pdf(pdf_path, pages="1")

#print(df)

# We can use these 2 methods if we are sure we only have one table on a page
df[0].to_csv("first_tb") # method 1: will create first_tb.csv 

tabula.convert_into(pdf_path, "first_tb_2", output_format="csv", pages="1") # method 2: will create first_tb_2.csv 

#print("Dami is working")